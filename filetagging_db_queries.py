import mysql.connector

#include 'filetagging_helper_functions.py'
helperFilename='filetagging_helper_functions.py'
exec(compile(open(helperFilename).read(),helperFilename,'exec'))



d_dbg_all=False
def queryDatabase(qry, func=None):
    #Connect to mysql database
    cnx = mysql.connector.connect(user='ragnar', host='localhost', database='filetagging');
    result=[None,None];
    exception=None;

    try:
        cur = cnx.cursor(buffered=True);

        try:
            result[0]=cur.execute(qry)
            if (func != None):
                result[1]=func(cnx,cur)
        except mysql.connector.errors.IntegrityError as ierr:
            raise Exception(ierr); #Let caller handle this one
        except mysql.connector.Error as err:
            exception=err;
        finally: #Close cursor connection
            cur.close()

    except mysql.connector.Error as err:
        exception=err;

    finally: #Close connection to mysql
        cnx.close()
        if (exception != None):
            handleDatabaseError(exception)

    if result[0] == None:
        result[0]=(exception != None);

    return tuple(result)


d_dbg_getTagID=False
def getTagID(tagName):
    query=queryDatabase(f"SELECT id FROM TAGS WHERE name='{tagName}'",
            lambda cnx,cur: cur.fetchone())

    res=None

    if (query[1] != None):
        res=query[1][0]

    if d_dbg_all or d_dbg_getTagID:
        print(f"result of getTagID({tagName})= {res}")

    return res

d_dbg_createTag=False
def createTag(tagName):
    query=queryDatabase(f"INSERT INTO TAGS VALUES (NULL, '{tagName}')",
            lambda cnx,cur: cnx.commit())

    res=getTagID(tagName)

    if d_dbg_all or d_dbg_createTag:
        print(f"query from createTag({tagName}) returned {query}")
        print(f"result of createTag({tagName})= {res}")

    return res

d_dbg_getTagName=False
def getTagName(tagId):
    query=queryDatabase(f"SELECT name FROM TAGS WHERE id={tagId}",
            lambda cnx,cur: cur.fetchone());

    res=None
    if query[1] != None:
        res=query[1][0];

    if d_dbg_all or d_dbg_getTagName:
        print(f"Result of getTagName({tagId})={res}")

    return res;


d_dbg_getFileID=False
def getFileID(fileName):
    query=queryDatabase(f"SELECT id FROM TAGGED_FILES WHERE name='{fileName}';",
            lambda cnx, cur: cur.fetchone())

    res = None

    if query[1] != None:
       res=query[1][0]

    if d_dbg_all or d_dbg_getFileID:
        print(f"Result of getFileID({fileName})={res}")

    return res

d_dbg_addFile=False
def addFile(fileName):
    query=queryDatabase(f"INSERT INTO TAGGED_FILES VALUES (NULL, '{fileName}');",
        lambda cnx, cur: cnx.commit())

    res=getFileID(fileName)

    if d_dbg_all or d_dbg_addFile:
        print(f"Result of addFile({fileName})= {res}")

    return res

d_dbg_getDirID=False
def getDirID(dirPath):
    query=queryDatabase(f"SELECT id FROM TAGGED_DIRECTORIES WHERE path='{dirPath}'",
        lambda cnx, cur: cur.fetchone())

    res = None

    if query[1] != None:
       res=query[1][0]

    if d_dbg_all or d_dbg_getDirID:
        print(f"Result of getDirId({dirPath})= {res}")

    return res;
    
d_dbg_addDir=False
def addDir(dirPath):
    query=queryDatabase(f"INSERT INTO TAGGED_DIRECTORIES VALUES (NULL, '{dirPath}');",
        lambda cnx, cur: cnx.commit())

    res=getDirID(dirPath)

    if d_dbg_all or d_dbg_addDir:
        print(f"Result of addDir({dirPath})= {res}")

    return res;

d_dbg_applyTag=False
def applyTag(fileID, tagID):
    try:
        query_s=f"INSERT INTO FILE_TAGS VALUES ({tagID}, {fileID})";
        if d_dbg_all or d_dbg_applyTag:
            print(f"applyTag query: {query_s}")

        query=queryDatabase(f"INSERT INTO FILE_TAGS VALUES ({tagID}, {fileID}, {dirID})",
                lambda cnx,cur: cnx.commit())
    except Exception as ierr:
        handleDatabaseError(ierr,False)

