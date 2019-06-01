import sqlite3

def dbCreate(db):
    try:
        connection = sqlite3.connect('{}.db'.format(db))
        print("Detected database " + db + ".")
        return connection
    except:
        print("Error occurred.")

def createTable(db, name, rowTitle, rowDataType):
    cmd = [('CREATE TABLE IF NOT EXISTS ' + name + ' ( ')]
    for row in range(len(rowTitle)):
        if row != (len(rowTitle) - 1):
            end = ', '
        else:
            end = ');'
        cmd.append(rowTitle[row] + ' ')
        cmd.append(rowDataType[row] + end)
    finalCmd = ''.join(cmd)
    executeCmd(db, finalCmd)
    print("Detected table " + name + ".")

def insertData(db, table, rows, values):
    cmd = [('INSERT INTO ' + table + '(' + rows + ') VALUES(')]
    for val in range(len(values)):
        if val != (len(values) - 1):
            end = '", '
        else:
            end = '");'
        cmd.append('"' + values[val] + end)
    finalCmd = ''.join(cmd)
    executeCmd(db, finalCmd)

def retrieveData(db, item, table, limit, offset):
    if limit == 0:
        cmd = ("SELECT " + item + " FROM " + table + ";")
    else:
        cmd = ("SELECT " + item + " FROM " + table + " LIMIT " + str(limit) + " OFFSET " + str(offset) + ";")
    rows = executeCmd(db, cmd)
    return rows

def executeCmd(db, command):
    conn = dbCreate(db)
    c = conn.cursor()
    c.execute(command)
    if "SELECT" in command:
        return(c.fetchall())
    conn.commit()
    conn.close()

def testing():
    database = input("Enter name of db: ")
    dbCreate(database)
    table = input("Enter name of table: ")
    rowTitles = []
    rowDataTypes = []
    rowLen = input("How many rows?: ")
    for i in range(int(rowLen)):
        rowName = input("Enter name of row " + str(i) + ": ")
        rowData = input("Enter data type of row " + str(i) + ": ")
        rowTitles.append(rowName)
        rowDataTypes.append(rowData)
    createTable(database, table, rowTitles, rowDataTypes)
    rowInsert = input("Enter rows to insert to(separated by comma): ")
    vals = input("Enter values to insert(separated by comma): ")
    val = vals.split(",")
    insertData(database, table, rowInsert, val)
    print("Retrieving data...")
    print(retrieveData(database, "*", table, 0, 0))
#testing()