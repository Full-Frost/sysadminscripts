#!//usr/bin/python3
#Colin O'Rourke add_users.py 2/19/2022
import os
import csv
#import grp
usernames_d = {}            #global username dictornary to check duplicates 
eid_d = {}                  #global eid dictonary to check for duplicates 
PASSWORD = 'password'       #default password 
OFFICESHELL = '/bin/csh'    #office shell
DEFAULTSHELL = '/bin/bash'  #default shell

def file_reader():  #reads the file and controls the program
    with open('linux_users.csv') as csv_file:
        csvRead = csv.reader(csv_file, delimiter=',')#creates the list
        counter = 0#counter to skip header line
        for row in csvRead:#used to skip header line
            if counter == 0:
                counter += 1
                continue
            else:
                
                eid = row[0]#eid assignment
                first = row[2]#firstname
                last = row[1]#lastname
                office = row[3]#office
                phone = row[4]#phone
                department = row[5]#deparment
                group = row[6]#group

                

                if first == '' or last == '' or department == '' or department.isdigit():#checks to see if any errors that need to be corrected before running through program
                    print('Data entry error in the user at row '+ str(counter-1))#provides error report
                    counter +=1
                    continue
            
                useradder(first, last, eid, group, department)#program
                counter +=1

def usernameMaker(first, last):#makes username and check for duplicates 
    first = first[0]
    username = first + last#combines the username 
    disallowedcharacters = "._!\'"
    for character in disallowedcharacters:
        username = username.replace(character,"")
    if username not in usernames_d:#checks to see if username exists in the dictonary  if not it adds it 
        usernames_d[username] = 1#assigns the username the value of 1
    else:#if the username already exists 
        count = usernames_d[username] #pulls the value from dictonary 
        usernames_d[username] += 1#adds one to value 
        username = username + str(count)#adds the username and the value together 
    return username

def duplicateEID(eid):
    if eid not in eid_d:#check to see if eid exists in dictonary if not it adds it 
        eid_d[eid] = 1#assigns the eid the value of 1
    else:#if eid already exists 
        count = eid[eid]#gets the value from the dictonary
        eid_d[eid] += 1#adds 1 to value 
        eid = eid + str(count)#combines eid and value 
    return eid

def useradder(first, last, eid, group, deparment):
    username = usernameMaker(first, last)#creates the username 
    print(username)
    actualEID = duplicateEID(eid)#checks for duplicate eid
    print(actualEID)
    os.system("groupadd " + group)#creates the group
    print('Adding group: '+ group)
    os.system("mkdir -p /home/" + deparment + "/" + username)#creates the directory for the user 
    print('Directory made: /home/' + deparment + '/' + username)
    if group == 'office':#checks to see if user is in the office group 
        os.system("useradd -m -d /home/" + deparment + "/" + username + " -s " + OFFICESHELL + " -g " + group + " -u " + actualEID + " " + username)#creates the user 
        print('useradd -m -d /home/' + deparment + '/' + username + ' -s ' + OFFICESHELL + ' -g ' + group + ' -u ' + actualEID + ' ' + username)
    else:#if the user is not is the office group
        os.system("useradd -m -d /home/" + deparment + "/" + username + " -s " + DEFAULTSHELL + " -g " + group + " -u " + actualEID + " " + username)#creates the user 
        print('useradd -m -d /home/' + deparment + '/' + username + ' -s ' + DEFAULTSHELL + ' -g ' + group + ' -u ' + actualEID + ' ' + username)
    os.system("echo " + PASSWORD + ":" + username + " | chpasswd")#changes the password 
    print("echo " + PASSWORD + ":" + username + " | chpasswd")
    os.system('passwd -e ' + username)#makes the password expire after the 
    print('passwd -e ' + username)

def main():
    os.system('clear')
    file_reader()

main()


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
