#!/usr/bin/env python

from enum import Enum

class FiletagConfig:
    class DatabaseConfig:
        dbName;
        username;
        usePassword=False;  #WARNING: Password functionality IS NOT SECURE!
        password;           #YOU SHOULD NOT USE A PASSWORD!
        host;

        class DatabaseType(Enum):
            #MySQL is the only supported database type right now
            MySQL='mysql'

    #Maybe not needed?
    #class MySQLConfig(DatabaseConfig):
