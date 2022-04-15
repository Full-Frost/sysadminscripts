#!/usr/bin/python3
#By: Colin O'Rourke     4/1/2022

#testing: /home/student/scripts/script04/syslog.log

import os#needed to find file and clear terminal
import re#needed for regex operations 
from geoip import geolite2#used to get location from ip
from collections import Counter, OrderedDict#used to count IPs and order the dictionary 
from datetime import date#gets the date

def parser(logfile):#parses the file and then compiles report 
    iplist = []#list of all IPs pulled from regex expression
    pat = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')#regex expression to be used to find IP addresses 
    if not os.path.isfile(logfile):#checks to see if filepath entered is valid 
        print('Please enter a valid filepath')
    else:#if the file path is valid do this 
        with open(logfile) as log:#open the file 
            logger = log.readlines()#read file line by line 
        for line in logger:#for ever line 
            iplist.append(pat.findall(line))#append the line after it has been sorted by regex expression 
        ipactual = []#new list to remove empty elements 
        for element in iplist:#for every element in the earlier list 
            ip = ' '.join(element)#this is because the regex was returning the value as a list not a str, this makes each element into a string 
            if len(ip) > 0:#checks to make sure element isn't empty 
                ipactual.append(ip)#adds the new string of the ip into the new list 
        iptotal = Counter(ipactual)#creates a dictionary which has a count of the amount of times each IP appeared in the report 
        dateCurrent = date.today().strftime("%B %d, %Y")#gets the current date in string format 
        print('Attacker Report - ' + dateCurrent)#header of report
        print('IPAddress \t # of Occurences \t Location ')#header for each column 
        ipascending = OrderedDict(sorted(iptotal.items(), key=lambda x: x[1]))#sorts the list into ascending order by value 
        for ip in ipascending:#for every element in the ipascending dictionary 
            if ipascending[ip] >= 10:#checks to make sure value (how many times the IP appears) is more than 10
                match = geolite2.lookup(ip)#gets the geographical data on ip
                print(str(ip) + ' \t ' + str(ipascending[ip]) + ' \t \t \t ' + match.country)#report output, first is the ip address, then the # of occurences< then country

def main():
    os.system('clear')#clears terminal 
    filepath = input('Please enter the filepath of the log file: ')#gets file path for file 
    parser(filepath)#runs the parser function 

main()
