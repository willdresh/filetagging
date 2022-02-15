#!/usr/bin/env python

l_dbg_all=False

#include "filetagging_db_queries.py"
dbqFilename='filetagging_db_queries.py'
exec(compile(open(dbqFilename).read(),dbqFilename,'exec'))

def printListTagsHelpText():
    print('Syntax: listtags < -a | filename>\n');

l_dbg_listTagNames=False
def listTagNames(tags):
    if l_dbg_listTagNames or d_dbg_all or l_dbg_all: print(f"Debugging call to listTagNames(tags={tags})")

    if (tags == None):
        return set();

    result=set()
    nextTName=None;
    for tag in tags:
        if len(tag) == 2:
            nextTName=tag[1]
            if l_dbg_listTagNames or d_dbg_all or l_dbg_all: print(f"\tAppending tag tag[1]={tag}[1]={tag[1]}...");
        else:
            nextTName=getTagName(tag[0])
            if l_dbg_listTagNames or d_dbg_all or l_dbg_all: print(f"\tAppending tag getTagName(tag[0])=getTagName({tag}[0])=getTagName({tag[0]})=  {nextTName}");

        result.add(nextTName);

    return result;

l_dbg_listAllTags=False
def listAllTags(file=None):
    if l_dbg_listAllTags or d_dbg_all or l_dbg_all:
        print(f"Debugging call to listAllTags(file={file})");

    #if no file is specified, list all available tags
    if (file == None):
        queryStr=f"SELECT * FROM TAGS;"
    else:
        fid=None
        try:
            fid=int(file)
        except ValueError:
            fid=getFileID(getStandardizedFile(file));
            if (fid == None):
                # If the file is not in the database, then
                # return None (as it has no tags)
                return None

        queryStr=f"SELECT tag FROM FILE_TAGS WHERE fileId={fid};"


    if l_dbg_listAllTags or d_dbg_all or l_dbg_all:
        print(f"\tlistAllTags: queryStr={queryStr}");

    query=queryDatabase(queryStr,
            lambda cnx,cur: cur.fetchall());

    res = None
    if (query[1] != None):
        res=set(query[1]);

    if l_dbg_listAllTags or d_dbg_all or l_dbg_all:
        print(f"\tlistAllTags: result={res}");

    return res;
# End def listAllTags

