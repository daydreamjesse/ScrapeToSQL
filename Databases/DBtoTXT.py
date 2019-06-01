import dbhandling as db
import time
import sys

print("This script retrieves data from the table you enter and puts it into a line-delimited .txt file.")
fileText = input("Enter file name to send data to: ")
master_file = ("./DBTXT/" + fileText)
database = input("Enter database to convert: ")
table = input("Enter table to pull from: ")
item = input("Enter items to pull(* is not acceptable in this case): ")

def deTuple(tup):
    return ("\n".join(tup))

while True:
    limit = input("Please enter the LIMIT: ")
    if "break" in limit:
        sys.exit()
    offset = input("Please enter the offset: ")
    print("Retrieving data...")
    start = time.time()
    data = db.retrieveData(database, item, table, limit, offset)
    end = time.time()
    print("Retrieved data in " + str(round((end - start), 4)) + "s.")
    mf = open(master_file, "a+")
    print("Writing to files...")
    start2 = time.time()
    for i in range(len(data)):
        print((deTuple(data[i])), file=mf)
    end2 = time.time()
    print("Finished writing file in " + str(round((end2 - start2), 4)) + "s.")
    mf.close()
