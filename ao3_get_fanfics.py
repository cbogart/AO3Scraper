######
#
# This script takes in (a list or csv of) fic IDs and
# writes a csv containing the fic itself, as well as the 
# metadata.
#
# Usage - python ao3_get_fanfics.py ID [--header header] [--csv csvoutfilename] 
#
# ID is a required argument. It is either a single number, 
# multiple numbers seperated by spaces, or a csv filename where
# the IDs are the first column.
# (It is suggested you run ao3_work_ids.py first to get this csv.)
#
# --header is an optional string which specifies your HTTP header
# for ethical scraping. For example, the author's would be 
# 'Chrome/52 (Macintosh; Intel Mac OS X 10_10_5); Jingyi Li/UC Berkeley/email@address.com'
# If left blank, no header will be sent with your GET requests.
# 
# --csv is an optional string which specifies the name of your
# csv output file. If left blank, it will be called "fanfics.csv"
# Note that by default, the script appends to existing csvs instead of overwriting them.
# 
# --restart is an optional string which when used in combination with a csv input will start
# the scraping from the given work_id, skipping all previous rows in the csv
#
# Author: Jingyi Li soundtracknoon [at] gmail
# I wrote this in Python 2.7. 9/23/16
# Updated 2/13/18 (also Python3 compatible)
#######

import requests
from bs4 import BeautifulSoup
import argparse
import time
import os
import pdb
import re
import csv
import sys
from unidecode import unidecode

def get_tag_info(category, meta):
    '''
    given a category and a 'work meta group, returns a list of tags (eg, 'rating' -> 'explicit')
    '''
    try:
        tag_list = meta.find("dd", class_=str(category) + ' tags').find_all(class_="tag")
    except AttributeError as e:
        return []
    return [unidecode(result.text) for result in tag_list] 
    
def get_stats(meta):
    '''
    returns a dictionary of  
    language, published, status, date status, words, chapters, comments, kudos, bookmarks, hits
    '''
    categories = ['language', 'published', 'status', 'words', 'chapters', 'comments', 'kudos', 'bookmarks', 'hits'] 

    stats = {}
    for category in categories:
        try:
            stat = unidecode(meta.find("dd", class_=category).text )
        except Exception, e:
            stat = "null"
            print type(e), e, category
        stats[category] = stat

    stats["status date"] = stats.get("status",stats["published"])
    stats["language"] = stats["language"].strip()

    #add a custom completed/updated field
    thestatus  = meta.find("dt", class_="status")
    if not thestatus: status = 'Completed' 
    else: status = thestatus.text.strip(':')
    stats["status"] = status
    
    print stats
    return stats      

def get_tags(meta):
    '''
    returns a list of lists, of
    rating, category, fandom, pairing, characters, additional_tags
    '''
    tags = ['rating', 'category', 'fandom', 'relationship', 'character', 'freeform']
    return { tag: get_tag_info(tag, meta) for tag in tags }


def access_denied(soup):
    if (soup.find(class_="flash error")):
        return True
    if (not soup.find(class_="work meta group")):
        return True
    return False

def robust_get(url, headers):
    req = None
    req_count = 10
    req_err = None
    while req_count > 0 and req is None:
        try:
            req = requests.get(url, headers=headers)
        except Exception, e:
            req = None
            req_err = e
            req_count -= 1
            print "ERROR, on ", url, " sleeping 30"
            print type(e), e
            time.sleep(30)
    if req_count == 0 and req is None:
        raise req_err
    return req

def write_fic_to_csv(fic_id, only_first_chap, writer, errorwriter, columns, header_info=''):
    '''
    fic_id is the AO3 ID of a fic, found every URL /works/[id].
    writer is a csv writer object
    the output of this program is a row in the CSV file containing all metadata 
    and the fic content itself.
    header_info should be the header info to encourage ethical scraping.
    '''
    print('Scraping ', fic_id)
    url = 'http://archiveofourown.org/works/'+str(fic_id)+'?view_adult=true'
    if not only_first_chap:
        url = url + '&amp;view_full_work=true'
    headers = {'user-agent' : header_info}
    req = robust_get(url, headers)
    src = req.text
    soup = BeautifulSoup(src, 'lxml')
    if (access_denied(soup)):
        print('Access Denied')
        open("err_" + str(fic_id) + ".err.txt", "w").write(src)
        error_row = [fic_id] + ['Access Denied']
        errorwriter.writerow(error_row)
    else:
        meta = soup.find("dl", class_="work meta group")
        tags = get_tags(meta)
        stats = get_stats(meta)
        title = unidecode(soup.find("h2", class_="title heading").string).strip()
        author = unidecode(soup.find(class_="byline").text).strip()
        href = soup.find(class_="byline").find("a")["href"]
        author_key = href.split("/")[2]
        author_pseudo = href.split("/")[4]
        #get the fic itself
        content = soup.find("div", id= "chapters")
        chapters = content.findAll("div", id=re.compile('^chapter-'))
            
        #chaptertext = '\n\n'.join([unidecode(chapter.text) for chapter in chapters])
        for ch, chall in enumerate(chapters):
            chapter_title = unidecode(chall.find("div", class_="preface").text).strip()
            paras = " ".join([para.text for para in chall.find("div", class_="userstuff").select("p")])
            chapter_text = unidecode(chall.find("div", class_="userstuff").text).strip()
            chapter_text = chapter_text[13:] if chapter_text[0:13] == "Chapter Text "
            row = dict(stats,**tags)
            otherparts = { "work_id": fic_id,
                    "title": title,
                    "chapter_title": chapter_title,
                    "additional tags": tags["freeform"],
                    "page": ch+1,
                    "author": author_pseudo,
                    "author_key": author_key,
                    "title": title,
                    "chapter_text": chapter_text}
            row = dict(row,**otherparts)
            try:
                writer.writerow([row.get(k,"null") for k in columns])
            except:
                print('Unexpected error: ', sys.exc_info()[0])
                error_row = [fic_id] +  [sys.exc_info()[0]]
                errorwriter.writerow(error_row)
        print('Done.')

def get_args(): 
    parser = argparse.ArgumentParser(description='Scrape and save some fanfic, given their AO3 IDs.')
    parser.add_argument(
        'ids', metavar='IDS', nargs='+',
        help='a single id, a space seperated list of ids, or a csv input filename')
    parser.add_argument(
        '--csv', default='fanfics.csv',
        help='csv output file name')
    parser.add_argument(
        '--header', default='',
        help='user http header')
    parser.add_argument(
        '--restart', default='', 
        help='work_id to start at from within a csv')
    parser.add_argument(
        '--firstchap', default='', 
        help='only retrieve first chapter of multichapter fics')
    args = parser.parse_args()
    fic_ids = args.ids
    is_csv = (len(fic_ids) == 1 and '.csv' in fic_ids[0]) 
    csv_out = str(args.csv)
    headers = str(args.header)
    restart = str(args.restart)
    ofc = str(args.firstchap)
    if ofc != "":
        ofc = True
    else:
        ofc = False
    return fic_ids, csv_out, headers, restart, is_csv, ofc

'''

'''
def process_id(fic_id, restart, found):
    if found:
        return True
    if fic_id == restart:
        return True
    else:
        return False

def main():
    fic_ids, csv_out, headers, restart, is_csv, only_first_chap = get_args()
    delay = 5
    os.chdir(os.getcwd())
    columns = ['work_id', 'title', 'author', 'author_key', 'rating', 'category', 'fandom', 'relationship', 'character', 'additional tags', 'language', 'published', 'status', 'status date', 'words', 'comments', 'kudos', 'bookmarks', 'hits', 'page', 'chapter_title', 'chapters', 'chapter_text']
    with open(csv_out, 'a') as f_out:
        writer = csv.writer(f_out)
        with open("errors_" + csv_out, 'a') as e_out:
            errorwriter = csv.writer(e_out)
            #does the csv already exist? if not, let's write a header row.
            if os.stat(csv_out).st_size == 0:
                print('Writing a header row for the csv.')
                writer.writerow(columns)
            if is_csv:
                csv_fname = fic_ids[0]
                with open(csv_fname, 'r+') as f_in:
                    reader = csv.reader(f_in)
                    if restart is '':
                        for row in reader:
                            if not row:
                                continue
                            write_fic_to_csv(row[0], only_first_chap, writer, errorwriter, columns, headers)
                            print "Sleeping ", delay
                            time.sleep(delay)
                    else: 
                        found_restart = False
                        for row in reader:
                            if not row:
                                continue
                            found_restart = process_id(row[0], restart, found_restart)
                            if found_restart:
                                write_fic_to_csv(row[0], only_first_chap, writer, errorwriter, columns, headers)
                                print "Sleeping ", delay
                                time.sleep(delay)
                            else:
                                print('Skipping already processed fic')

            else:
                for fic_id in fic_ids:
                    write_fic_to_csv(fic_id, only_first_chap, writer, errorwriter, columns, headers)
                    print "Sleeping ", delay
                    time.sleep(delay)

main()
