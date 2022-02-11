#!/usr/bin/env python


import os
import sys

def printHelpText():
    print('Syntax: addtag <filename> <tag> [additional-tag] ... [additional-tagN]\n')

#include "filetagging_db_queries.py"
dbqFilename='filetagging_db_queries.py'
exec(compile(open(dbqFilename).read(),dbqFilename,'exec'))

target=None
tags=[]

if len(sys.argv) < 2:
    printHelpText();
    handleInvalidArguments("too few arguments");

if sys.argv[1] in ['--help','-h']:
    printHelpText();
    exit(0);

target=os.path.abspath(sys.argv[1]);
target_dir=os.path.dirname(target);
print(f"Target_dir= {target_dir}");

if os.path.isfile(target)==False:
    handleInvalidArguments(f"{sys.argv[1]} is not a valid file");

dirID=getDirID(target_dir);
if (dirID == None):
    dirID=addDir(target_dir);

fileID=getFileID(target)
if (fileID == None):
    fileID=addFile(target)

d_dbg_foreach_arg=False
for arg in sys.argv[2:len(sys.argv)]:
    if d_dbg_foreach_arg or d_dbg_all:
        print(f"Processing sys.argv[x]={arg}");
    tagID=getTagID(arg);
    if tagID != None:
        tags.append(tagID);
    else:
        tags.append(createTag(arg));

d_dbg_foreach_tag=False
for tag in tags:
    if d_dbg_foreach_tag or d_dbg_all:
        print(f"Processing tag {tag}");

    applyTag(fileID,tag)
    #applyTag(fileID,tag,dirID)
