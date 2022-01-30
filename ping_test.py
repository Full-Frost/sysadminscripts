#!/bin/bash
#Colin O'Rourke ping_test.py 2/4/2022
import os
import subprocess


hostname = "www.google.com" #For testing DNS 
remoteIP = "129.21.3.17" #RIT DNS 

def pingGoogle():
    pingTest = os.system("ping -c 1 " + hostname)#Does the pinging by using the hardcoded address and the ping command (only sends one ping), used to determine if the ping can reach the outside internet
    if pingTest == 0: #if pingTest is 0 that means the ping was successful
        print("Able to connect to the remote IP")#Letting the user know they wer able to ping google successfully 
    else:
        print("Not able to connect to the remote IP")#The user was not able to ping google

def pingIP():
    pingTest = os.system("ping -c 1 " + remoteIP)#Pings the hardcoded DNS server to determine if DNS is up only sends one ping
    if pingTest == 0:#if pingTest is 0 that means the ping was successful
        print("DNS is up")#Letting the user know DNS is up
    else:
        print("DNS is down")#Letting the user know they could not ping the RIT DNS server. 

def gatewayTest():
    addr = subprocess.Popen(["ip r"], stdout=subprocess.PIPE, shell=True)#Opens up a subprocess which will extract network information from the computer it is being run in byte form
    output = addr.stdout.read().decode()#reads the bytes and converts it into a string
    sep = output.split(" ")#converts the string into a list which is able to hold each piece of information from the strin ginto a single list element
    gate = sep[2]#The gateway will always be held at element 2 of the list
    print("default gateway = " + gate)#Letting the user know what their default gateway is
    pingTest = os.system("ping -c 1 " + gate)#Actually pings the default gateway from the information that was taken earlier and only sends out a single ping
    if pingTest == 0:#if pingTest is 0 that means the ping was successful
        print("Able to connect to the default gateway")#Letting the user know they could ping their default gateway
    else:
        print("Not able to connect to the default gateway")#Letting the user know they couldn't ping their default gateway

def main():
    os.system('clear')#Clears terminal before running the scripts 
    print('Welcome to the ping_test.py')#user menu which provides options 
    print('The following options are available')
    print('|1| ping remote IP ')
    print('|2| DNS test')
    print('|3| ping default gateway')
    print('|4| All 3 tests')
    print('|5| to exit the program')#exits the program for the user so they don't have to do a keyboard interrupt
    while(1):#Makes sure the program doesnt end unless the user selects the end command
        option = input("Please enter the number for the corresponding option you which to use. (1-5)")
        if(option == '1'):
            pingGoogle()
        elif(option == '2'):
            pingIP()
        elif(option == '3'):
            gatewayTest()
        elif(option == '4'):
            pingGoogle()
            pingIP()
            gatewayTest()
        elif(option == '5'):
            quit()
        else:
            print("Please enter a number 1-5")#In case they dont put in a correct number 
        
        

if __name__ == "__main__":
    main()
