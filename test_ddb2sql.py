import mksql


tester = mksql.Sqlout("samplesql", "sample")
tester.insert_table("content", ["'my name'","4","'content23'", "NULL"])
tester.insert_table("content", ["'your name'","5","'content34'", "NULL"])
tester.close()
