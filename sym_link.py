#!//usr/bin/python3
#Colin O'Rourke sym_link.py 3/4/2022

from importlib.resources import path
import os
import subprocess

PWD = os.getcwd()#gets the pwd of the user
DESKTOP = '/~/Desktop' #potentially allows to cd into desktop

def builder(): #builds the symlinks
    source = input("Please enter the filepath of the source file. ")#enter the file path of the file that is the source of the symlink
    dest = input("Please enter the filename of the destination file. ")#enter the name of what you would like to link the source to 
    if os.path.isfile(source):#checks that the source file exists
        if os.path.exists(dest) and os.path.islink(dest):#makes sure that the destination is not already created 
            print('There already exists a symlink on the destination file that is not broken')
        else:#if destination does not exist 
            os.system('ln -s ' + source + ' ' + dest)#creates the symlink 
            if os.path.exists(dest) and os.path.islink(dest):#checks to make sure the symlink was made 
                os.system('mv ' + dest + ' ' + DESKTOP)#moves the file to desktop
                print('The file ' + dest + 'now points to ' + os.readlink(dest))#letting the user know it was made
            else:
                print('The symlink was not successfully made')#letting the user know that the symlink failed
    else:
        print('Source file does not exist')#filepath to source does not exist 

def remover():
    target = input('Please provide the name of the symlink that you would like to remove. ')#user enters the name of the file pathe they want to remove 
    if os.path.exists(target) and os.path.islink(target):#makes sure that the symlink exists 
        os.system('unlink ' + target) #removes the symlink 
        print('symlink has been removed')#letting the user know that the symlink has been removed
    else:
        print('This is an invalid target')#filepath to the symlink is invalid 

def reporter():
    os.chdir(DESKTOP)#makes sure we are in desktop
    report = subprocess.run('find . -type l', stdout=subprocess.PIPE)#finds the symlinks in the Desktop directory
    print('SymLink Report Generator\n')
    reportGen = report.stdout.decode('utf-8').split('/')#reads the output of the command and splits it into a list 
    counter = 0#counter 
    for i in reportGen:#navigates through the list
        if os.is_symlink(reportGen[i]):#checks to determine if list entry is a symlink 
            print('The file ' + reportGen[i] + ' is a symlink that points to ' + os.readlink(reportGen[i]))#if is is it reads out the output and the filepath that the link points to 
            count += 1#adds 1 to the counter 
    print('The total number of available symlinks in the Desktop directory is %d', counter)#prints the total number of symlinks at the end 

def main():
    os.system('clear')#clears terminal
    print('Your current directory is: ' + PWD)#displays current directory
    while(1):#infinite loop unless quit is called
        path = input('[b] to build a symlink between two files.\n[r] in order to remove a symlink.\n[l] for a list of all active symlinks.\n[quit] to exit the program.')#menu
        if path == 'b':
            builder()#run builder function
        elif path == 'r':
            remover()#run remover function
        elif path == 'l':
            reporter()#run reporter function
        elif path == 'quit':
            print("Thanks")
            quit()#quit the program
        else:
            print('Invalid input')#invalid input 
