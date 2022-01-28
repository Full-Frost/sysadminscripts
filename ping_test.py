#!/bin/bash
#Colin O'Rourke ping_test.py 2/4/2022
import os
import subprocess

hostname = "www.google.com" #For testing DNS 
remoteIP = "129.21.3.17" #RIT DNS 

def pingGoogle():
    pingTest = os.system("ping -c 1 " + hostname)
    if pingTest == 0:
        print("Able to connect to the remote IP")
    else:
        print("Not able to connect to the remote IP")

def pingIP():
    pingTest = os.system("ping -c 1" + remoteIP)
    if pingTest == 0:
        print("DNS is up")
    else:
        print("DNS is down")

def gatewayTest():
    addr = subprocess.Popen(["ip r"], stdout=subprocess.PIPE, shell=True)
    output = addr.subprocess.read()
    print("default gateway = " + output)
    pingTest = os.system("ping -c 1" + output)
    if pingTest == 0:
        print("Able to connect to the default gateway")
    else:
        print("Not able to connect to the default gateway")

def main():
    print('Welcome to the ping_test.py')
    print('The following options are available')
    print('|1| DNS test')
    print('|2| ping remote IP')
    print('|3| ping default gateway')
    print('|4| All 3 tests')
    while(1):
        option = input("Please enter the number for the corresponding option you which to use.")
        if(option == 1):
            pingGoogle()
        elif(option == 2):
            pingIP()
        elif(option == 3):
            gatewayTest()
        elif(option == 4):
            pingGoogle()
            pingIP()
            gatewayTest()
        else:
            print("Please enter a number 1-4")
        os.system('clear')

if __name__ == "__main__":
    main()