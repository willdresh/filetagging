import sys
import mysql.connector.errors

getStandardizedFile=os.path.abspath
getStandardizedDirectory=os.path.dirname
chkValidFileStandardized=os.path.isfile

def reportError(msg):
    sys.stderr.write(msg)

def handleInvalidArguments(msg="",thenExit=True,exitCode=1):
    reportError(f"{sys.argv[0]}: Invalid Arguments\n")
    reportError(f"Syntax error: {msg}\n")
    if thenExit: 
        reportError(f"Exiting with code {exitCode}\n")
        exit(exitCode)

def handleDatabaseError(err, thenExit=False, exitCode=2):
    reportError(f"Database Error: {err}\n")
    if thenExit:
        reportError(f"Exiting with code {exitCode}\n")
        exit(exitCode)
    else:
        reportError("Non-fatal error; continuing\n")

def printNothingToDoMessage(strPrefix):
    print(f"{strPrefix} Nothing to do...");
