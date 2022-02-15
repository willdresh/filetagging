

def printAddTagHelpText():
    print('Syntax:\taddtag [-v] <filename> <tag> [additional-tag] ... [additional-tagN]\n')

def reportTagAlreadyApplied(exc):
    print('\tNon-Fatal Exception: requested tag already applied');
    print('\tContinuing...');

# The following "printXtoY" methods are only called when running in verbose mode
def printAddDirToDBMessage(target_dir):
    print(f"Adding new directory {target_dir} to database");

def printAddFileToDBMessage(target):
    print(f"Adding new file {target} to database")

def printAddTagToDBMessage(tagName):
    print(f"Adding new tag {tagName} to database")

def printAddTagToFileMessage(tagId, target):
    print(f"Applying tag {tagId} to file {target}")

