#!//usr/bin/python3
#Colin O'Rourke sym_link.py 3/4/2022

from importlib.resources import path
import os
import subprocess

PWD = os.getcwd()
DESKTOP = '/~/Desktop'

def builder():
    source = input("Please enter the filepath of the source file. ")
    dest = input("Please enter the filename of the destination file. ")
    if os.path.isfile(source):
        if os.path.exists(dest) and os.path.islink(dest):
            print('There already exists a symlink on the destination file that is not broken')
        else:
            os.system('ln -s ' + source + ' ' + dest)
            if os.path.exists(dest) and os.path.islink(dest):
                os.system('mv ' + dest + ' ' + DESKTOP)
                print('The file ' + dest + 'now points to ' + os.readlink(dest))
            else:
                print('The symlink was not successfully made')
    else:
        print('Source file does not exist')

def remover():
    pass

def reporter():
    os.chdir(DESKTOP)
    report = subprocess.run('find . -type l', stdout=subprocess.PIPE)
    print('SymLink Report Generator\n')
    reportGen = report.stdout.decode('utf-8').split('/')
    for i in reportGen:
        if os.is_symlink(reportGen[i]):
            print('The file ' + reportGen[i] + ' is a symlink that points to ' + os.readlink(reportGen[i]))

def main():
    os.system('clear')
    print('Your current directory is: ' + PWD)
    while(1):
        path = input('[b] to build a symlink between two files.\n[r] in order to remove a symlink.\n[l] for a list of all active symlinks.\n[quit] to exit the program.')
        if path == 'b':
            builder()
        elif path == 'r':
            remover()
        elif path == 'l':
            reporter()
        elif path == 'quit':
            quit()
        else:
            print('Invalid input')
    
