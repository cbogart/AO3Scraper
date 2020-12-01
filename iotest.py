import csv

csv1 = csv.writer(open("junk.csv","w"))
payload = '\\x\\y\\z\\'
assert len(payload) == 7
csv1.writerow(["one","two"])
csv1.writerow([payload,payload])
csv1 = None


csv2 = csv.DictReader(open("junk.csv"))
for row in csv2:
    print len(row["one"]), len(row["two"]), row["one"], row["two"]
