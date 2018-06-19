#!/usr/bin/env python

import sys
import os
import tempfile


def execute(command):
    os.system(command)
    
def print_err(message):
    execute(">&2 echo \""+message+"\"")
    
def print_usage():
    usage="cbr2cbz A script utility to convert CBR files into CBZ files"
    usage+="\n\t Usage: cbr2cbz <filename_without_spaces.cbr>"
    usage+="\n\t\n\t (Please don't use non-free formats like RAR/CBR)"
    print_err(usage)

#Extract images from a CBR file into a directory
def uncompress(filename, directory):
    UNRAR="unrar-nonfree e"
    command=" ".join([UNRAR, "\""+filename+"\"", directory])
    #print_err(command)
    execute(command)

#Compress a folder with images into a CBZ/ZIP file
def compress (directory, zip_filename):
    ZIP="zip"
    directory=directory+"/*"
    command=" ".join([ZIP, "\""+zip_filename+"\"", directory ])
    execute (command)

def get_filename_without_extension(filename):
    return filename[:-4]

    

if len(sys.argv)!=2:
    print_usage();
    sys.exit(-1)




cbr_filename=sys.argv[1]
cbz_filename=get_filename_without_extension(cbr_filename)+".cbz"
temp_dir=tempfile.mkdtemp("cbr2cbz")

print_err("Processing "+cbr_filename)

#Extract images from CBR/RAR into a directory
uncompress(sys.argv[1], temp_dir)

#Compress images and put them into a CBZ/ZIP
compress(temp_dir, cbz_filename)
execute("".join(["rm -Rf ", temp_dir]))



def extract (cbr_filename, dir_name):
    pass
    







#execute ("dir")