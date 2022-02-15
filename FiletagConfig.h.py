#!/usr/bin/env python

from enum import Enum
import mysql.connector

class FiletagConfig:
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
            match self.dbType:
                case DatabaseType.MySQL:
                    if usePassword:
                        return mysql.connector.connect(user=self.username,password=self.password,host=self.host,database=self.dbName)
                    else:
                        return mysql.connector.connect(user=self.username,host=self.host,database=self.dbName);
                    #end if-else
                #end case DatabaseType.MySQL
            #end match
        #end def Connect
    #end class DatabaseConfig

    #Maybe not needed?
    #class MySQLConfig(DatabaseConfig):

    dbConfig=DatabaseConfig();

    def __init(self,
            _dbConfig=DatabaseConfig()):
        self.dbConfig=_dbConfig;
    #end def __init__
#end class FiletagConfig
