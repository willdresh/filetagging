#!/usr/bin/env python


import os
import sys

def printHelpText():
    print('Syntax: listtags < -a | filename>\n');

l_dbg_all=False

#include "filetagging_db_queries.py"
dbqFilename='filetagging_db_queries.py'
exec(compile(open(dbqFilename).read(),dbqFilename,'exec'))

l_dbg_listTagNames=False
def listTagNames(tags):
    result=[]
    nextTName=None;
    for tag in tags:
        if len(tag) == 2:
            nextTName=tag[1]
            if l_dbg_listTagNames or d_dbg_all or l_dbg_all:
                print(f"Appending tag tag[1]={tag}[1]={tag[1]}...");
        else:
            nextTName=getTagName(tag[0])
            if l_dbg_listTagNames or d_dbg_all or l_dbg_all:
                print(f"Appending tag getTagName(tag[0])=getTagName({tag}[0])=getTagName({tag[0]})=  {nextTName}");
        result.append(nextTName);

    return result;

l_dbg_listAllTags=False
def listAllTags(file=None):

    #if no file is specified, list all available tags
    if (file == None):
        queryStr=f"SELECT * FROM TAGS;"
    else:
        isInt=False
        fid=None
        try:
            fid=int(file)
            queryStr=f"SELECT tag FROM FILE_TAGS WHERE fileId={fid};"
        except ValueError:
            queryStr=f"SELECT tag FROM FILE_TAGS WHERE fileId={getFileID(os.path.abspath(file))};"

    if l_dbg_listAllTags or d_dbg_all or l_dbg_all:
        print(f"listAllTags: queryStr={queryStr}");

    query=queryDatabase(queryStr,
            lambda cnx,cur: cur.fetchall());

    if l_dbg_listAllTags or d_dbg_all or l_dbg_all:
        print(f"listAllTags: result={query[1]}");

    return query[1];

myTags=None
if (len(sys.argv) < 2): myTags=listAllTags()
else: myTags=listAllTags(sys.argv[1])

print(f"{listTagNames(myTags)}")
