# A simple CLI tool to compress specified files in a target zip file 
# Author : Ramesh Vyas

from zipfile import ZipFile
from pathlib import Path
import sys
import os

argc = len(sys.argv)
#Variable for directory filter (*.txt / *.py etc..)
filter=""
# Count number of files zipped
count=0
if(argc==4):
    if(Path(sys.argv[1]).is_dir and os.path.exists(sys.argv[1])):        
        if(sys.argv[2] == ""):                
            filter="*.*"
        else:    
            filter = sys.argv[2]    

        with ZipFile(sys.argv[3],"w") as zip:            
            for path in Path(sys.argv[1]).rglob(filter):
                count+=1
                zip.write(path)
                
        print(f"{count} files zipped to {sys.argv[3]}")
    else:
        print(f"{sys.argv[1]} is not a valid directory")    
else:
    print("Invalid use of zip utility")    
    print("USAGE: zip.py <source folder> <filter eg. *.py / *.txt / *.*> <target .zip filename>")

