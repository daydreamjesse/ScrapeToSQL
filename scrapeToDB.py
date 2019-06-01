from Databases import dbhandling as db
from Webscraping import scraper as sc

def scraping():
    url = sc.getURL()
    req = sc.getRequest(url)
    tag = input("Enter tag: ")
    target = input("Enter class: ")
    find = input("Find all?[Y/N]: ")
    if find is "Y":
        findBool = True
    else:
        findBool = False
    scrapeData = sc.scrapeByClass(req, tag, target, findBool)
    return(scrapeData)

def infoToDB(data):
    dbPath = "./Databases/"
    database = input("Enter name of database: ")
    database = dbPath + database
    db.dbCreate(database)
    table = input("Enter name of table: ")
    rowTitles = []
    rowDataTypes = []
    rowLen = input("How many rows?: ")
    for i in range(int(rowLen)):
        rowName = input("Enter name of row " + str(i+1) + ": ")
        rowData = input("Enter data type of row " + str(i+1) + ": ")
        rowTitles.append(rowName)
        rowDataTypes.append(rowData)
    db.createTable(database, table, rowTitles, rowDataTypes)
    rowInsert = input("Enter rows to insert to(separated by comma): ")
    db.insertData(database, table, rowInsert, data)

data = scraping()
infoToDB(data)