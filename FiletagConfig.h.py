#!/usr/bin/env python

import os
from enum import Enum
import mysql.connector

# TODO set this up to check for the -v command line argument
FILETAG_VERBOSE=True

ft_helperFilename='filetagging_helper_functions.py'
exec(compile(open(ft_helperFilename).read(),ft_helperFilename,'exec')) #this is a "#include" directive

HL_DEFAULT_ENABLED=True
HL_DEFAULT_SUBDIRECTORY_NAME=".filetag-links"
HL_DEFAULT_ON_PERMISSION_DENIED=handlePermissionDenied
#HL_DEFAULT_ON_NOREAD_PERMISSION=handlePermissionDenied(f"read or execute hardlink subdirectory");
#HL_DEFAULT_ON_NOWRITE_PERMISSION=handlePermissionDenied(f"write to hardlink subdirectory")

class HardlinkTrackingConfig:
    subdirectoryName=HL_DEFAULT_SUBDIRECTORY_NAME
    #onNoReadPermission=HL_DEFAULT_ON_NOREAD_PERMISSION
    #onNoWritePermission=HL_DEFAULT_ON_NOWRITE_PERMISSION
    onNoReadPermission=HL_DEFAULT_ON_PERMISSION_DENIED
    onNoWritePermission=HL_DEFAULT_ON_PERMISSION_DENIED
#end class hardlinkTrackingConfig

class DatabaseConfig:
    class DatabaseType(Enum):
        #MySQL is the only supported database type right now
        MySQL='mysql'

    dbType=DatabaseType.MySQL;
    dbName="";
    username="";
    host="";
    usePassword=False;  #WARNING: Password functionality IS NOT SECURE!
    password="";           #YOU SHOULD NOT USE A PASSWORD!

    def __init__(self,
            _dbType=DatabaseType.MySQL,
            _dbName="",
            _username="",
            _host="",
            _usePassword=False,
            _password=""):
        self.dbType=_dbType
        self.dbName=_dbName
        self.username=_username
        self.host=_host
        self.usePassword=_usePassword
        self.password=_password
    #end def __init__

    def Connect(self):


        if self.dbType == DatabaseConfig.DatabaseType.MySQL:
            if self.usePassword:
                return mysql.connector.connect(user=self.username,password=self.password,host=self.host,database=self.dbName)
            else:
                return mysql.connector.connect(user=self.username,host=self.host,database=self.dbName);
        #elsif self.dbType == SomeOtherType ...

    #end def Connect
#end class DatabaseConfig

class FiletagConfig:

    dbConfig=DatabaseConfig();
    useHardlinkTracking=True
    hltConfig=HardlinkTrackingConfig();

    def __init__(self,
            _dbConfig,
            _useHardlinkTracking=True,
            _hltConfig=HardlinkTrackingConfig()):
        self.dbConfig=_dbConfig;
        self.useHardlinkTracking=_useHardlinkTracking;
        self.hltConfig=_hltConfig;
    #end def __init__
#end class FiletagConfig
