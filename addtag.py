#!/usr/bin/env python


import os
import sys

#The following line is roughly equivalent to C++ #include directive
dbqFilename='filetagging_db_queries.py'
exec(compile(open(dbqFilename).read(),dbqFilename,'exec')) #include "filetagging_db_queries.py"

def printHelpText():
    print('Syntax:\taddtag [-v] <filename> <tag> [additional-tag] ... [additional-tagN]\n')

# The following "printXtoY" methods are only called when running in verbose mode
def printAddDirToDBMessage(target_dir):
    print(f"Adding new directory {target_dir} to database");

def printAddFileToDBMessage(target):
    print(f"Adding new file {target} to database")

def printAddTagToDBMessage(tagName):
    print(f"Adding new tag {tagName} to database")

def printAddTagToFileMessage(tagId, target):
    print(f"Applying tag {tagId} to file {target}")

verbose=False

# If user asked for help, print help text and exit successfully
if sys.argv[1] in ['--help','-h']:
    printHelpText();
    exit(0);
# Check if verbose switch was specified
elif sys.argv[1] in ['--verbose','-v']:
    verbose=True
    del sys.argv[1] #Delete the -v switch from the argument list, so the rest of the args line up

# At least 2 arguments required
if len(sys.argv) < 2:
    printHelpText();
    handleInvalidArguments("too few arguments");


target=os.path.abspath(sys.argv[1]);
target_dir=os.path.dirname(target);

if os.path.isfile(target)==False:
    handleInvalidArguments(f"{sys.argv[1]} is not a valid file");
# (no need to check if target_dir is a valid dir, because if it isn't, then target isn't a valid file)

# Query MySQL database to find the IDs of both the file and its directory
# if the file and/or dir are not in the database, add them
dirID=getDirID(target_dir);
if (dirID == None):
    # if running in verbose mode, report that a new directory is being added
    if verbose: printAddDirToDBMessage(target_dir);
    dirID=addDir(target_dir);

fileID=getFileID(target)
if (fileID == None):
    # if running in verbose mode, report that a new file is being added
    if verbose: printAddFileToDBMessage(target);
    fileID=addFile(target)

d_dbg_foreach_arg=False
taglist=sys.argv[2:len(sys.argv)];
tags=[]
for tagName in taglist:
    if d_dbg_foreach_arg or d_dbg_all:
        print(f"Processing argument {tagName}");

    tagID=getTagID(tagName);
    if tagID != None:
        tags.append(tagID);
    else:
        if verbose: printAddTagToDBMessage(tagName);
        tags.append(createTag(tagName));

for tag in tags:
    if verbose: printAddTagToFileMessage(tag, target);
    applyTag(fileID,tag)
