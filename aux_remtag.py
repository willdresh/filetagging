#!/usr/bin/env python

def printRemTagHelpText():
    print('Syntax:\tremtag [-v] <filename> <tag> [additional-tag] ... [additional-tagN]\n')

def printFileNotInDBMessage(file):
    print(f'remtag: err: file {file} not in database!');

def printTagNotInDBMessage(tag):
    print(f'remtag: err: tag {tag} not in database!');

