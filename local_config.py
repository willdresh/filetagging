#!/usr/bin/env python

#include 'FiletagConfig.h.py'
filetagConfigFilename='FiletagConfig.h.py'
exec(compile(open(filetagConfigFilename).read(),filetagConfigFilename,'exec'))

myLocalConfig=FiletagConfig(
        FiletagConfig.DatabaseConfig(
            FiletagConfig.DatabaseConfig.DatabaseType.MySQL,
            "filetagging",
            "ragnar",
            "localhost")
        )
