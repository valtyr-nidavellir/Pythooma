import subprocess
import utilities
import os

def check():
    print('Checking dependencies...')

    try:
        directory=os.getcwd()+'/data/installed.txt'
        os.system('apt list --installed > '+directory)
    except:
        print('ERR: Package regestry collection failed!')
        exit(1)
    
    # try:
    #     counter=0
    #     for line in utilities.readlines('data/installed.txt','r'):
    #         if line.find('aircrack-ng'):
    #             print(line)
    #             print('Found:\taircrack-ng')
            
    #     if counter==1:
    #         if input('Missing dependencies detected! Use autoinstaller? Y/N: ').lower()=='y':
    #             subprocess.run(['python3','autoinstaller.py'])
    #         else:
    #             print('Please install the required dependencies.')
    #             exit(1)
    #     else:
    #         print('All dependecies found!')       
    # except:
    #     print('asdf')

def autoinstall():
    subprocess.run(['python3', 'autoinstaller.py'])
