import pdb
import csv
import os
import json
import datetime
import argparse
from dateutil.parser import parse

parser = argparse.ArgumentParser("Convert archiveofourown files to csv for DiscourseDB import")
parser.add_argument("--fandom", help="Name of fandom (from which directory name et al are derived")
parser.add_argument("--limit", help="Only prepare <limit> stories", default=None)
parser.add_argument("--no_crossover", help="Skip crossover stories", default = False)
parser.add_argument("--ddbfiles", help="output csv file directory for input into discoursedb", default="X")
args,unknown = parser.parse_known_args()
download_dir = "ao3_" + args.fandom + "_text"
if args.ddbfiles == "X":
    ddbfile = "ao3_" + args.fandom + "_ddb"
else:
    ddbfile = args.ddbfiles
try:
    os.makedirs(ddbfile)
except Exception, e:
    print type(e), e
    pass
stories = download_dir + "/stories.csv"
chapters = download_dir + "/chapters.csv"
textdir = download_dir + "/stories/"

columns = "id,replyto,username,forum,forum_types,discourse,title,when,dpparent.dpparent.annotation_language,dpparent.dpparent.annotation_link,dpparent.dpparent.annotation_rated,dpparent.dpparent.annotation_category,dpparent.dpparent.annotation_fandom,dpparent.dpparent.annotation_relationship,dpparent.dpparent.annotation_character,dpparent.dpparent.annotation_tags,dpparent.dpparent.annotation_status,dpparent.dpparent.annotation_comments,dpparent.dpparent.annotation_kudos,dpparent.dpparent.annotation_bookmarks,dpparent.dpparent.annotation_hits,dataset_file,post".split(",")

ddbfile_part = 1
def new_ddbfile():
    global ddbfile_part
    outf = csv.writer(open(ddbfile + "/part" + str(ddbfile_part).zfill(6) + ".csv","wb"))
    outf.writerow(columns)
    ddbfile_part += 1
    return outf

stories = {row["fic_id"]: row for row in csv.DictReader(open(stories)) }
#for f in stories:
    #for k in stories[f]:
        #if "\\" in stories[f][k]:
        #    stories[f][k] = stories[f][k].replace("\\","\\\\")
        #try:
            #stories[f][k] = json.loads(stories[f][k])
        #except:
            #pass

def wrap_list(ls):
    return json.dumps(ls)

def forum_hier(parts):
    return "/".join([p.replace("/","_") for p in parts])

row_count = 0
outf = new_ddbfile()
storylist = set()
for chapter in csv.DictReader(open(chapters)):
    story = stories[chapter["fic_id"]]
    if chapter["fic_id"] not in storylist: 
        print len(storylist), chapter["title"]
        storylist.add(chapter["fic_id"])
    if args.limit is not None and len(storylist) > int(args.limit):
        break
    if args.no_crossover == 'True' and len(json.loads(story["fandom"])) > 1:
        continue
    chapter_name = chapter["chapter_title"]
    rated = story["rating"]
    page = int(chapter["chapter_num"])
    pagefile = textdir + str(story["fic_id"]) + "_" + str(page).zfill(4) + ".csv"
    when = story["status date"] if story["status date"] != "null" else story["published"]
    link = "<a href=\"https://archiveofourown.org/works/" + chapter["fic_id"] + "\">original</a>"
    try:
        when = parse(when).isoformat()
    except:
        when = ""
    if row_count > 100:
        outf = new_ddbfile()
        row_count = 0
    for paragraph in csv.DictReader(open(pagefile,"r")):
        para_id = int(paragraph["para_id"])
        row_count += 1
        outf.writerow([
	    str(story["fic_id"])+"_"+str(page).zfill(4)+"_"+str(para_id).zfill(5),
	    (str(story["fic_id"])+"_"+str(page).zfill(4)+"_"+str(int(para_id)-1).zfill(5)) if int(para_id)>1 else "",
            story["author_key"],
            forum_hier([args.fandom, story["title"], chapter["chapter_title"]]),
            "FORUM/DOCUMENT/PARAGRAPH",
            "AO3 " + args.fandom,
            "",   # no title
            when,
                    # NB: we could get chapter-by-chapter release dates wiht a different query
                    # https://archiveofourown.org/works/13540809/navigate
            story["language"],
            link,
            story["rating"],
            story["category"],
            story["fandom"],
            story["relationship"],
            story["character"],
            story["additional tags"],
            story["status"],
            story["comments"],
            story["kudos"],
            story["bookmarks"],
            story["hits"],
            "ao3_" + args.fandom,
            paragraph["text"]])
