import csv
import os
import os.path

#ao3_friends_ddb/part000001.csv
#id,replyto,username,forum,forum_types,discourse,title,when,annotation_link,annotation_rated,annotation_category,annotation_fandom,annotation_relationship,annotation_character,annotation_tags,annotation_status,annotation_comments,annotation_kudos,annotation_bookmarks,annotation_hits,dataset_file,post

for f in os.listdir("ao3_friends_ddb"):
    if os.path.isfile("ao3_friends_ddb/" + f):
        toolong = set()
        for row in csv.DictReader(open("ao3_friends_ddb/" + f)):
            if len(row["forum"]) > 94:
                toolong.add(row["forum"])
                print f, row["forum"].encode("utf-8","default")
