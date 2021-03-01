import os
import subprocess
import threading
import osdetect

#########FILE

def print_title():
    for line in readlines('data/title.txt','r'):
        print(line.strip('\n'))

def read(name,op):
    try:
        return open(name,op).read()
    except:
        print('ERR: Read operation failed!')
        exit(1)

def readlines(name,op):
    try:
        return open(name,op).readlines()
    except:
        print('ERR: Readlines operation failed!')
        exit(1)

def write(name,op,data):
    try:
        return open(name,op).write(data)
    except:
        print('ERR: Write operation failed!')
        exit(1)

def writelines(name,op,data):
    try:
        return open(name,op).writelines(data)
    except:
        print('ERR: Writelines operation failed!')
        exit(1)

#########TERMINAL

def clear():
    if osdetect.get_system()=='Windows':
        try:
            os.system('cls') 
        except:
            pass
    else:
        try:
            os.system('clear')
        except:
            pass
