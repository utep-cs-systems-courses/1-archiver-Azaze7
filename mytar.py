#---------------------------------------------------------------------------------
# Gilbert I. Guzman -- 88769422
# CS 4375 -- CRN: 24866 -- Dr. Fruedenthal
#---------------------------------------------------------------------------------
# Lab 1 - Student Code Submission -- 'mytar.py'
# Due: 2/13/23 -- Present to TA
#---------------------------------------------------------------------------------
# Assignment: Build a toy version of tar. (Tape Archiver)
    #2 MAJOR FUNCTIONS:
        #1.(c) Create
            #Creates a new archive on the 'tape' we are working with.
            #NOT ACTUALLY CREATE, JUST WRITES TO STDOUT
                #For example, the following command would "create" a new 
                #archive on tape /dev/mt0 containing the files foo and goo:
                    #tar c foo goo > /dev/mt0
        #2.(x) Extract
            #Extracts the contents of a file to the parent directory.
                #The following command will extract the archived files on
                #/dev/mt0 to tar's current directory:
                    #tar c foo goo > foogoo.tar
    #IMPORTANT CONSIDERATIONS:
        #MUST USE POSIX SYSTEM CALLS FOR OUR INPUT AND OUTPUT.
        #WE MUST CHUNK FILES IN BYTES SO WE CAN SEND IT FAST.
        #IT MUST BE ABLE TO ERROR REPORT, THAT BEING, RETURN A 2 = ERROR;
            #INSTEAD OF JUST 0 = IN AND 1 = OUT. A MESSAGE SHOULD BE PRINTED TOO!
#---------------------------------------------------------------------------------

#Default Imports. (WE ARE ONLY ALLOWED THESE 2).
    #[from os import read, write]
import os
import sys

#Name of file input.
progName = sys.argv[0]
#Name of file output.
oFileName = sys.argv[1]      

#CAT COMPONENETS (beta, stolen from example code via Dr. Fruedenthal)
#Demo of os file open/read/close semantics.

def printFromFd(ifd):
    numReads = 1
    while True:
        ibuf = os.read(ifd, 100)
        if not len(ibuf): break
        numReads += 1
        os.write(1, ibuf)
     # summary to stderr
    os.close(ifd)
    os.write(2, f"EOF on {numReads}th call to read()\n".encode())
    

filesToPrint = sys.argv[1:]     # all params are file names

if len(filesToPrint):
    for fname in filesToPrint:
        os.write(2, f"copying file: {fname}\n".encode()) # to stderr
        fd = os.open(fname, os.O_RDONLY)
        printFromFd(fd)
else:
    os.write(2, "copying from stdin\n".encode()) # to stderr
    printFromFd(0)              # stdin by default (no files)