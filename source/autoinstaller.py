#valtyr

import subprocess

pip=[
    "python3",
    "-m",
    "pip",
    "install",
    "--upgrade",
    "--user",
    "pip"
]

print('Running autoinstaller...')
print('Interupting this process may cause unintentional damage...please be patient...')

print('Checking pip...')
try:
    subprocess.run(['python3','-m','pip','--version'])

except:
    print('No pip detected...aborting...')
    exit(1)

choice=input('Upgrade pip? Y/N: ')
if(choice.lower()=='y'):
    print("Upgrading...")
    subprocess.run(pip)

print('Continuing execution...')

try:
    subprocess.run(["python3","-m","pip","install",'-r','data/requirements.txt'])
    print('Autoinstaller has completed execution!')
except:
    print("ERR: Autoinstaller failed!")