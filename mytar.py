#!/usr/bin/env python

#***The Above line must be included for UNIX, it is a she-bang.
#--------------------------------------------------------------------------------------------
# Gilbert I. Guzman -- 88769422
# CS 4375 -- CRN: 24866 -- Dr. Fruedenthal
#--------------------------------------------------------------------------------------------
# Lab 1 - Student Code Submission -- 'mytar.py'
# Due: 2/13/23 -- Present to TA -- [2:10-2:30]
#--------------------------------------------------------------------------------------------
# LEARNING OUTCOMES REFLECTION:
    #1. File Descriptors. [NO]
        #Can read and write from stdin, stdout, stderr;
            #and named files using system calls.
    #2. Interpreted Programs. [NO]
        #Made code that works directly from the command line.
        #Knows how to grant permission to execute, use shebang, 
            #and pass parameters using argv.
    #3. Framing. [NO]
        #Made code that embed and extract multiple byte arrays, which includes files
            #that contain headers that are used to decribe the file that are NOT
            #the file itself.
#--------------------------------------------------------------------------------------------
# Assignment Instructions: Build a toy version of tar. (Tape Archiver)
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
#--------------------------------------------------------------------------------------------
# BRAINSTORMING (REAL WORK):
# RESEARCH USING UTF-8 ENCODING SINCE THAT IS BYTES AUTOMATICALLY.
    #Main Function:
        #Must be able to take the system arguments the user inputs into it, 
        #[mytar] [c or x] [file(s) or folder] [< or >] [new.tar or extracted.tar]
    #***WE WILL DO THIS USING IF/ELSE FORMING A MENU SYSTEM.***
        #Logic:
            #If the system args =< 3: (3 since thats in example; tar x < /dev/mt0)
            #Print message on how its supposed to work, then kill the program.
        #Else:
            #if operand == [c]:
                #Call create_function.
            #elif operand == [x]:
                #Call extract_function.
            #else
                #Print out message about not using a real operation, kill program.
    
    #Create_function:
    #DOESN'T Actually create anything, just reads the source file and writes to stdout.

    #Extract_function:


#--------------------------------------------------------------------------------------------
# STUDENT RESEARCH:
    #Tar (.tar) stands for Tape Archive Files.
    #It keeps many files in a single file, similar to a .zip.
    #You can take stuff out of it, or put stuff in using directors (< or >).
#--------------------------------------------------------------------------------------------
# USING UBUNTU-LINUX:
    #***You Can Drag And Drop files From Windows ---> UBUNTU!!!! [DR. FRUEDENTHAL TIP]***
    #1. Start Ubuntu using the installed app.
    #2. Find the file.
        #cd /tmp/
        #Opens tmp directory, where I will be putting code for a while.
    #3. Change File Permissions.
        #chmod +(x or r or w) <file>.py
            #x is for execute.
            #r is for run.
            #w is for write.
    #4. Run the file.
        #$_ python3 mytar.py
        #Will run the file now, compilation errors because I dont know how linux works.
#--------------------------------------------------------------------------------------------

#Default Imports. (WE ARE ONLY ALLOWED THESE 2 TO MY KNOWLEGE).
    #[from os import read, write]
import os
import sys

#Print Default Code Messages.
print("------")

#Name of file input.
progName = sys.argv[0]
#Name of file output.
oFileName = sys.argv[1]      



#--------------------------------------------------------------------------------------------
# END OF CODE.
 