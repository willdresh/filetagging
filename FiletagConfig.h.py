#!/usr/bin/env python

from enum import Enum

class FiletagConfig:
    class DatabaseConfig:
        class DatabaseType(Enum):
            #MySQL is the only supported database type right now
            MySQL='mysql'

        dbType=DatabaseType.MySQL;
        dbName="";
        username="";
        usePassword=False;  #WARNING: Password functionality IS NOT SECURE!
        password="";           #YOU SHOULD NOT USE A PASSWORD!
        host="";


    #Maybe not needed?
    #class MySQLConfig(DatabaseConfig):
