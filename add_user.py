#!/bin/bash
#Colin O'Rourke add_users.py 2/19/2022
import os
import csv
import pwd
import grp

PASSWORD = 'password'       #default password 
OFFICE_SHELL = '/bin/csh'   #office group shell

def file_reader():#reads the file and returns a nested list of all the entries while ignoring the header line 
    with open('linux_users.csv') as csv_file:
        csv_read = csv.reader(csv_file, delimiter=',')#creates the list
        counter = 0
        rows = []
        for row in csv_read:
            if counter == 0:#ignore header
                counter += 1
                continue
            else:
                #print(row)
                rows.append(row)#adding the lists into the main list
                counter += 1
    #for i in rows:
    #print(rows)
    return rows

def group(rows): #Handles group creation 
    #print(len(rows))
    for i in range(7):
        group_name = rows[i][6]#gets the group name 
        try: #check to see if the group name exists 
            grp.getgrnam(group_name)
            print('group exists')
        except KeyError:#if it doesn't exist create it 
            #os.system('groupadd '+ group_name)
            print('adding user group: '+ group_name)
        
    
def username(rows): # creates the username from the nested list and puts all of them into one list does not account for duplication
    usernames = []
    for i in range(len(rows)):
        try:
            username = rows[i][2][0]+rows[i][1]#combines the first letter of the first name and the last name
            usernames.append(username)
        except IndexError:
            print("invalid username entry")
            usernames.append("INVALID")
    return usernames

def userid(rows):# creates the userids from the nested list and puts all of them into one list does not account for duplication
    userids = []
    for i in range(len(rows)):
        try:
            user_id = rows[i][0]#retrieves the user id
            userids.append(user_id)
        except IndexError:
            print("invalid userid entry")
            user_id.append("INVALID")
    return userids

def duplicateUsername(usernames):#handles duplicate usernames 
    usernames_d = {}#store the frequency of the strings 
    for x in range(0, len(usernames)):#iterates over the list
        if usernames[x] != 'INVALID': 
            if usernames[x] not in usernames_d:#checks to see if the username has appeared before, if it hasnt adds it into the dictonary
                usernames_d[usernames[x]] = 1
            else:#username already within the dictionary 
                count = usernames_d[usernames[x]]#counts how many duplicates
                usernames_d[usernames[x]] += 1
                usernames[x] += str(count)#adds number to the username 
        else:
            continue
    return usernames#returns the parameter list

def duplicateUserID(userids):
    userids_d = {}#store the frequency of the strings
    for x in range(0, len(userids)):#iterates over the list
        if userids[x] != 'INVALID':
            if userids[x] not in userids_d:#checks to see if the userID has appeared before, if it hasnt adds it into the dictonary
                userids_d[userids[x]] = 1
            else:#userID is already within the dictionary 
                count = userids_d[userids[x]]#counts how many duplicates
                userids_d[userids[x]] += 1
                userids[x] += str(count)#adds number to the userID
        else:
            continue
    return userids#returns the parameter list

def finale(userids, usernames, rows):
    for i in range(len(rows)):#iterate through all the rows also used to determine what the username/userid is 
        group_name = rows[i][6]#get the groupname 
        department = rows[i][5]#get the department 
        try:
            if department[0].isdigit():#check to make sure the department is not a number 
                department == 'INVALID'
        except IndexError:#if the department field is empty will raise error 
            print("invalid department entry")
            department == 'INVALID'
        for x in range(7):
            if rows[i][x] == 'INVALID' or usernames[i] == 'INVALID' or userids[i] == 'INVALID':#checks to make sure the user data was correct
                print("User was not able to be created due to improper data entry.")#message to user about improper data
            else:
                directory = '/home/' + department + '/' + usernames[i]
                os.system("mkdir -p "+ directory)#creates the directory 
                if group_name == 'office':#checks to see if the group name is office
                    os.system("useradd -m -d "+ directory + ' -g ' + group_name + ' ' + usernames[i])
                    os.system('echo' + PASSWORD + ':' + usernames[i] + ' | chpasswd')
                    os.system('passwd -e ' + username[i])
                    os.system('usermod --shell ' + OFFICE_SHELL + ' ' + usernames[i])#sets the default shell to /bin/csh
                else:#every other group is added normally below 
                    os.system("useradd -m -d "+ directory + ' -g ' + group_name + ' ' + usernames[i])
                    os.system('echo' + PASSWORD + ':' + usernames[i] + ' | chpasswd')
                    os.system('passwd -e ' + username[i])


def main():
    os.system('clear')
    finale(duplicateUserID(userid(file_reader())), duplicateUsername(username(file_reader())), file_reader())



main()
