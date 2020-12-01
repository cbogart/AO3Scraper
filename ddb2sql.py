import mksql
import csv
import datetime
from dateutil.parser import parse
from collections import defaultdict

entities = defaultdict(dict)
def entityid(tablename, keyvalue):
    if keyvalue not in entities[tablename]:
        entities[tablename][keyvalue] = len(entities[tablename])
        return (entities[tablename][keyvalue], "new")
    else:
        return (entities[tablename][keyvalue], "old")

lastforum = ""
previous_row_id = ""
when = datetime.datetime.now()
def flesh_out(row, rownum, filename):
    global lastforum, previous_row_id
    fullrow = dict()
    fullrow["id"] = row.get("id", "row_" + str(rownum))
    fullrow["dataset_file"] = row.get("dataset_file", filename.replace(".csv",""))
    fullrow["dataset_name"] = row.get("dataset_name", fullrow["dataset_file"])
    fullrow["dataset_id_col"] = row.get("dataset_id_col", fullrow["id"])
    fullrow["username"] = row.get("username", "(unknown)")
    fullrow["user_email"] = row.get("user_email", "")
    fullrow["forum"] = row.get('forum', fullrow["dataset_file"])
    fullrow["forum_types"] = row.get('forum_types', "FORUM/SUBFORUM")
    if "replyto" in row:
        fullrow["replyto"] = row["replyto"]
    elif fullrow["forum"] == lastforum:
        fullrow["replyto"] = previous_row_id
    else:
        fullrow["replyto"] = ""
    lastforum = fullrow["forum"]
    previous_row_id = fullrow["id"]
    fullrow["discourse"] = row.get("discourse", fullrow["dataset_file"])
    fullrow["contribution_type"] = row.get("contribution_type", "POST")
    fullrow["title"] = row.get("title","")
    if "when" in row:
        fullrow["when"] = parse(row.get("when"))
    else:
        fullrow["when"] = when
        when += datetime.timedelta(seconds=1)
    return fullrow

ahora = datetime.datetime.now()
qahora = '"' + ahora.isoformat() + '"'
qnull = '"NULL"'
for (i,row) in enumerate(csv.DictReader(sys.argv[1])):
    fullrow = flesh_out(row, i, sys.argv[1])
    discourse, dn = entityid("discourse", fullrow["discourse"]) 
    if dn == "new": tester.insert_table("discourse", [discourse, qahora, qahora, "0", fullrow["discourse"])
    # do discourse part work
    user, dn = entityid("user", fullrow["username"]) 
    if dn == "new": tester.insert_table("user", [user, qahora, qahora,"0",qnull,qnull,qnull,fullrow["user_email"],
                                                 qnull,qnull,qnull,qnull,fullrow["username"],qnull])
    


tester = mksql.Sqlout("samplesql", "sample")
tester.insert_table("content", ["'my name'","4","'content23'", "NULL"])
tester.insert_table("content", ["'your name'","5","'content34'", "NULL"])
tester.close()
