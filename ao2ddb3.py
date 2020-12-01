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
parser.add_argument("--recs_per_file", help="Number of records per file", default=1000)
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

cr_columns = "id,replyto,username,forum,forum_type,discourse,title,when,dataset_file,post".split(",")
dp_columns = "forum,forum_name,forum_parent,forum_types,discourse,annotation_language,annotation_link,annotation_rated,annotation_category,annotation_fandom,annotation_relationship,annotation_character,annotation_tags,annotation_status,annotation_comments,annotation_kudos,annotation_bookmarks,annotation_hits,dataset_file".split(",")

ddbfile_part = 1
def new_ddbfile(kind,cols):
    global ddbfile_part
    outf = csv.DictWriter(open(ddbfile + "/" + kind + "_part" + str(ddbfile_part).zfill(6) + ".csv","wb"), fieldnames=cols)
    outf.writeheader()
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
recs_per_file = int(args.recs_per_file)
post_outf = new_ddbfile("post", cr_columns)
forum_outf = new_ddbfile("forum", dp_columns)
forum_unique = set()
def write_forum_unique(row):
    if row["forum"] not in forum_unique:
        forum_outf.writerow(row)
        forum_unique.add(row["forum"])
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
    if row_count > recs_per_file:
        post_outf = new_ddbfile("post", cr_columns)
        row_count = 0
    for paragraph in csv.DictReader(open(pagefile,"r")):
        para_id = int(paragraph["para_id"])
        row_count += 1
        write_forum_unique({
            "forum": forum_hier([args.fandom, story["title"], chapter["chapter_title"]]),
            "forum_name": chapter["chapter_title"],
            "forum_parent": forum_hier([args.fandom, story["title"]]),
            "forum_types": "FORUM/DOCUMENT/PARAGRAPH",
            "discourse": "AO3 " + args.fandom,
            "dataset_file": "AO3_" + args.fandom
        })
        write_forum_unique({
            "forum": forum_hier([args.fandom]),
            "forum_name": args.fandom,
            "forum_types": "FORUM",
            "discourse": "AO3 " + args.fandom,
            "dataset_file": "AO3_" + args.fandom
        })
        write_forum_unique({
            "forum": forum_hier([args.fandom, story["title"]]),
            "forum_name": story["title"],
            "forum_parent": forum_hier([args.fandom]),
            "forum_types": "FORUM/DOCUMENT",
            "annotation_language": story["language"],
            "annotation_link": link,
            "annotation_rated": story["rating"],
            "annotation_category": story["category"],
            "annotation_fandom": story["fandom"],
            "annotation_relationship": story["relationship"],
            "annotation_character": story["character"],
            "annotation_tags": story["additional tags"],
            "annotation_status": story["status"],
            "annotation_comments": story["comments"],
            "annotation_kudos": story["kudos"],
            "annotation_bookmarks": story["bookmarks"],
            "annotation_hits": story["hits"],
            "discourse": "AO3 " + args.fandom,
            "dataset_file": "AO3_" + args.fandom
        })
        post_outf.writerow({
	    "id": str(story["fic_id"])+"_"+str(page).zfill(4)+"_"+str(para_id).zfill(5),
	    "replyto": (str(story["fic_id"])+"_"+str(page).zfill(4)+"_"+str(int(para_id)-1).zfill(5)) if int(para_id)>1 else "",
            "username": story["author_key"],
            "forum": forum_hier([args.fandom, story["title"], chapter["chapter_title"]]),
            "forum_type": "FORUM/DOCUMENT/PARAGRAPH",
            "dataset_file": "AO3_" + args.fandom,
            "discourse": "AO3 " + args.fandom,
            "title": "",   # no title
            "when": when,
                    # NB: we could get chapter-by-chapter release dates wiht a different query
                    # https://archiveofourown.org/works/13540809/navigate
            "post": paragraph["text"]})
