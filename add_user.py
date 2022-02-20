#!/bin/bash
#Colin O'Rourke add_users.py 2/19/2022

import os
import csv
#import grp

PASSWORD = 'password'       #default password 
OFFICESHELL = '/bin/csh'
DEFAULTSHELL = '/bin/bash'

def file_reader():
    with open('linux_users.csv') as csv_file:
        csvRead = csv.reader(csv_file, delimiter=',')#creates the list
        for row in csvRead:
            eid = row[0]
            first = row[1]
            last = row[2]
            office = row[3]
            phone = row[4]
            department = row[5]
            group = row[6]

            if first == '' or last == '' or department == '' or department.isdigit():
                print('Data entry error in the user at row '+ row)
                continue
        
            useradder(first, last, eid, group, department)

def usernameMaker(first, last):
    usernames_d = {}
    first = first[0]
    username = first + last
    if username not in usernames_d:
        usernames_d[username] = 1
    else:
        count = usernames_d[username]
        usernames_d[username] += 1
        username + str(count)
    return username

def duplicateEID(eid):
    eid_d = {}
    if eid not in eid_d:
        eid_d[eid] = 1
    else:
        count = eid[eid]
        eid_d[eid] += 1
        eid + str(count)

def useradder(first, last, eid, group, deparment):
    username = usernameMaker(first, last)
    actualEID = duplicateEID(eid)
    os.system('groupadd ' + group)
    print('Adding group: '+ group)
    os.system('mkdir -p /home/' + deparment + '/' + username)
    print('Directory made: /home/' + deparment + '/' + username)
    if group == 'office':
        os.system('useradd -m -d /home/' + deparment + '/' + username + ' -s ' + OFFICESHELL + ' -g ' + group + ' -u ' + actualEID + username)
        print('useradd -m -d /home/' + deparment + '/' + username + ' -s ' + OFFICESHELL + ' -g ' + group + ' -u ' + actualEID + username)
    else:
        os.system('useradd -m -d /home/' + deparment + '/' + username + ' -s ' + DEFAULTSHELL + ' -g ' + group + ' -u ' + actualEID + username)
        print('useradd -m -d /home/' + deparment + '/' + username + ' -s ' + DEFAULTSHELL + ' -g ' + group + ' -u ' + actualEID + username)
    os.system('echo' + PASSWORD + ':' + username + ' | chpasswd')
    print('echo' + PASSWORD + ':' + username + ' | chpasswd')
    os.system('passwd -e ' + username)
    print('passwd -e ' + username)



"""def file_reader():#reads the file and returns a nested list of all the entries while ignoring the header line 
    with open('linux_users.csv') as csv_file:
        csv_read = csv.reader(csv_file, delimiter=',')#creates the list
        counter = 0
        rows = []
        for row in csv_read:
            if counter == 0:#ignore header
                counter += 1
                continue
            else:
                print(row)
                rows.append(row)#adding the lists into the main list
                counter += 1
    #for i in rows:
    print(rows)
    return rows

#def group(rows): #Handles group creation 
#    #print(len(rows))
#    for i in range(7):
#        group_name = rows[i][6]#gets the group name 
#        try: #check to see if the group name exists 
 #           grp.getgrnam(group_name)
 #           print('group exists')
 #       except KeyError:#if it doesn't exist create it 
 #           #os.system('groupadd '+ group_name)
 ##           print('adding user group: '+ group_name)
  #      print()
    
#def username(rows): # creates the username from the nested list and puts all of them into one list does not account for duplication
#    usernames = []
#    for i in range(len(rows)):
#        username = rows[i][2][0]+rows[i][1]#combines the first letter of the first name and the last name
#        usernames.append(username)
#    return usernames

#def userid(rows):# creates the userids from the nested list and puts all of them into one list does not account for duplication
#    userids = []
#    for i in range(len(rows)):
#        user_id = rows[i][0]#retrieves the user id
#        userids.append(user_id)
#    return userids

#def duplicateUsername(usernames):#handles duplicate usernames 
#    usernames_d = {}#store the frequency of the strings 
 #   for x in range(0, len(usernames)):#iterates over the list
#        if usernames[x] not in usernames_d:#checks to see if the username has appeared before, if it hasnt adds it into the dictonary
 #           usernames_d[usernames[x]] = 1
#        else:#username already within the dictionary 
#            count = usernames_d[usernames[x]]#counts how many duplicates
 #           usernames_d[usernames[x]] += 1
 #           usernames[x] += str(count)#adds number to the username 
 #   return usernames#returns the parameter list

#def duplicateUserID(userids):
 #   userids_d = {}#store the frequency of the strings
 #   for x in range(0, len(userids)):#iterates over the list
#        if userids[x] not in userids_d:#checks to see if the userID has appeared before, if it hasnt adds it into the dictonary
#            userids_d[userids[x]] = 1
 #       else:#userID is already within the dictionary 
 #           count = userids_d[userids[x]]#counts how many duplicates
#            userids_d[userids[x]] += 1
 #           userids[x] += str(count)#adds number to the userID
 #   return userids#returns the parameter list

#def finale(userids, usernames, group):
#    pass

def main():
    #os.system('clear')
    file_reader()

main()"""
