#fic_id,title,author,author_key,rating,category,fandom,relationship,character,additional tags,language,published,status,status date,words,comments,kudos,bookmarks,hits,chapter_count
#"""15951461""","""The Joey Project""","""casketofsunflowers""","""casketofsunflowers""","[""Mature""]","[""F/M"", ""M/M""]","[""Friends (TV)""]","[""Chandler Bing/Joey Tribbiani""]","[""Joey Tribbiani"", ""Chandler Bing"", ""Rachel Green"", ""Monica Geller"", ""Phoebe Buffay"", ""Ross Geller"", ""Janice Litman"", ""Kathy (Friends)"", ""Carol Willick"", ""Susan Bunch"", ""Gloria Tribbiani"", ""Joey Tribbiani Sr.""]","[""Joey POV"", ""Catholic Joey"", ""Sexuality Crisis"", ""Catholic Guilt"", ""Joey Needs a Hug"", ""and a sandwich"", ""preferably both at the same time"", ""Phoebe is a Good Bro"", ""Rachel is a Good Bro"", ""Monica is a Good Bro"", ""the girls are all the bros that joey needs in his life""]","""English""","""2018-09-10""","""Updated""","""2018-09-12""","""2780""","""6""","""19""","""3""","""145""",2

import csv
import json

def maybe_json(s):
    if type(s) is list: return json.dumps(s)
    if type(s) is dict: return json.dumps(s)
    if type(s) is unicode: return s.encode("utf-8")
    else: return s

stout = csv.writer(open("stories2.csv","w"))
dr = csv.DictReader(open("stories.csv"))
cols = dr.fieldnames
stout.writerow(cols)

for row in dr:
    for k in row.keys():
        row[k] = maybe_json(json.loads(row[k]))
    stout.writerow([row[k] for k in cols])
