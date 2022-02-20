#!//usr/bin/python3
#Colin O'Rourke add_users.py 2/19/2022
import os
import csv
#import grp
usernames_d = {}
PASSWORD = 'password'       #default password 
OFFICESHELL = '/bin/csh'
DEFAULTSHELL = '/bin/bash'

def file_reader():
    with open('linux_users.csv') as csv_file:
        csvRead = csv.reader(csv_file, delimiter=',')#creates the list
        counter = 0
        for row in csvRead:
            if counter == 0:
                counter += 1
                continue
            else:
                
                eid = row[0]
                first = row[2]
                last = row[1]
                office = row[3]
                phone = row[4]
                department = row[5]
                group = row[6]

                

                if first == '' or last == '' or department == '' or department.isdigit():
                    print('Data entry error in the user at row '+ str(counter-1))
                    counter +=1
                    continue
            
                useradder(first, last, eid, group, department)
                counter +=1

def usernameMaker(first, last):
    
    first = first[0]
    username = first + last
    if username not in usernames_d:
        usernames_d[username] = 1
    else:
        count = usernames_d[username]
        
        usernames_d[username] += 1
        username = username + str(count)
    return username

def duplicateEID(eid):
    eid_d = {}
    if eid not in eid_d:
        eid_d[eid] = 1
    else:
        count = eid[eid]
        eid_d[eid] += 1
        eid + str(count)
    return eid

def useradder(first, last, eid, group, deparment):
    username = usernameMaker(first, last)
    print(username)
    actualEID = duplicateEID(eid)
    print(actualEID)
    os.system('groupadd ' + group)
    print('Adding group: '+ group)
    os.system('mkdir -p /home/' + deparment + '/' + username)
    print('Directory made: /home/' + deparment + '/' + username)
    if group == 'office':
        os.system('useradd -m -d /home/' + deparment + '/' + username + ' -s ' + OFFICESHELL + ' -g ' + group + ' -u ' + actualEID + ' ' + username)
        print('useradd -m -d /home/' + deparment + '/' + username + ' -s ' + OFFICESHELL + ' -g ' + group + ' -u ' + actualEID + ' ' + username)
    else:
        os.system('useradd -m -d /home/' + deparment + '/' + username + ' -s ' + DEFAULTSHELL + ' -g ' + group + ' -u ' + actualEID + ' ' + username)
        print('useradd -m -d /home/' + deparment + '/' + username + ' -s ' + DEFAULTSHELL + ' -g ' + group + ' -u ' + actualEID + ' ' +username)
    os.system('echo ' + PASSWORD + ':' + username + ' | chpasswd')
    print('echo ' + PASSWORD + ':' + username + ' | chpasswd')
    os.system('passwd -e ' + username)
    print('passwd -e ' + username)

def main():
    os.system('clear')
    file_reader()

main()
