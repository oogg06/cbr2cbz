#!/usr/bin/env python

import sys
import os
import tempfile


def execute(command):
    os.system(command)
    
def print_err(message):
    execute(">&2 echo \""+message+"\"")
    
def print_usage():
    usage="cbr2cbz A script utility to convert a directory with CBR files into CBZ files"
    usage+="\n\t Usage: cbr2cbz <directory>"
    usage+="\n\t\n\t (Please don't use non-free formats like RAR/CBR)"
    print_err(usage)

def convert(filename):
    CONVERT="./cbr2cbz.py"
    command=" ".join([CONVERT, filename])
    execute(command)

if len(sys.argv)!=2:
    print_usage();
    sys.exit(-1)




directory=os.path.abspath(sys.argv[1])

for f in os.listdir(directory):
    filename_with_path=os.path.join(directory, f)
    print(filename_with_path)
    convert(filename_with_path)