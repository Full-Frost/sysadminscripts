#!//usr/bin/python3
#Colin O'Rourke sym_link.py 3/4/2022

#from importlib.resources import path
import os
import subprocess

PWD = os.getcwd()#gets the pwd of the user
DESKTOP = '/Desktop/' #potentially allows to cd into desktop

def builder(): #builds the symlinks
    source = input("Please enter the filepath of the source file. ")#enter the file path of the file that is the source of the symlink
    dest = input("Please enter the filename of the destination file. ")#enter the name of what you would like to link the source to 
    destPath = os.path.expanduser('~') + DESKTOP + dest#get the users home directory add desktop to it and then add the filename to essentially create a filepath
    if os.path.isfile(source):#checks that the source file exists
        if os.path.exists(destPath) and os.path.islink(destPath):#makes sure that the destination is not already created 
            print('There already exists a symlink on the destination file that is not broken')
        else:#if destination does not exist 
            os.system('ln -s ' + source + ' ' + destPath)#creates the symlink 
            if os.path.exists(destPath) and os.path.islink(destPath):#checks to make sure the symlink was made 
                #os.system('mv ' + dest + ' ' + DESKTOP)#moves the file to desktop
                print('The file ' + destPath + 'now points to ' + os.readlink(destPath))#letting the user know it was made
            else:
                print('The symlink was not successfully made')#letting the user know that the symlink failed
    else:
        print('Source file does not exist')#filepath to source does not exist 

def remover():
    target = input('Please provide the filepath of the symlink that you would like to remove. ')#user enters the name of the filepath they want to remove 
    if os.path.exists(target) and os.path.islink(target):#makes sure that the symlink exists 
        os.system('unlink ' + target) #removes the symlink 
        print('symlink has been removed')#letting the user know that the symlink has been removed
    else:
        print('This is an invalid target')#filepath to the symlink is invalid 

def logger():
    os.chdir(os.path.expanduser('~') + DESKTOP)#makes sure we are in desktop
    #report = subprocess.run('find -L . -xtype l -exec ls -al {} \;', stdout=subprocess.PIPE)#finds the symlinks in the Desktop directory
    print('SymLink Report Generator\n')
    os.system('find -L . -xtype l -exec ls -al {} \;')#get the symlinks in the directory
    count = 0#counter
    for root, dir, files in os.walk(os.path.expanduser('~') + DESKTOP):#iterate through desktop
        for filename in files:#iterate through all the files 
            if os.path.islink(os.path.join(os.path.expanduser('~') + DESKTOP, filename)):##checks to see if the file is a link 
                count += 1#adds to counter if it is
    print('The number of symlinks in the desktop directory is ' + str(count) + '\n')#prints the number of symlinks in the directory 
    #reportGen = report.stdout.decode('utf-8').split('\n')#reads the output of the command and splits it into a list 
    #print(len(reportGen))
    #counter = 0 #counter 
    #for i in reportGen:#navigates through the list
    #    if os.is_symlink(reportGen[i]):#checks to determine if list entry is a symlink 
    #        print('The file ' + reportGen[i] + ' is a symlink that points to ' + os.readlink(reportGen[i]))#if is is it reads out the output and the filepath that the link points to 
    #        count += 1#adds 1 to the counter 
    #print('The total number of available symlinks in the Desktop directory is %d', counter)#prints the total number of symlinks at the end 


def main():
    os.system('clear')#clears terminal
    print('Your current directory is: ' + PWD)#displays current directory
    while(1):#infinite loop unless quit is called
        path = input('[b] to build a symlink between two files.\n[r] in order to remove a symlink.\n[l] for a list of all active symlinks.\n[quit] to exit the program.\n')#menu
        if path == 'b':
            builder()#run builder function
        elif path == 'r':
            remover()#run remover function
        elif path == 'l':
            logger()#run reporter function
        elif path == 'quit':
            print("Thanks")
            quit()#quit the program
        else:
            print('Invalid input')#invalid input 
        

main()
