import utilities
import dependency
import osdetect
import encryption
import networking
import pwns

utilities.clear()
utilities.print_title()

# if osdetect.get_euid()==0:
#     print("\nUSR:\t\troot")
# else:
#     print("Run as root!")
#     exit(0)
osdetect.get_cpu()
print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>=")

# dependency.check()

while True:
    print('\n___Main___')
    print('[0] tools')
    print('[1] pwns')
    print('[2] ')
    print('[=] autoinstall')
    print('[-] exit')
    cmd=input('< ')

    if cmd=='0':
        print("\n[0] encrytion")
        print("[1] networking")
        print("[2] custom")
        cmd=input('< ')
        if cmd=='0':
            encryption.menu()
        elif cmd=='1':
            networking.menu()
        else:
            pass
        

    elif cmd=='1':
        print('\n[0] fuxstick')
        print('[1]')
        print('[2] ')
        print('[3] ')
        cmd=input('< ')
        if cmd=='0':
            pwns.fuxstick()
        elif cmd=='1':
            pass
        elif cmd=='2':
            pass
        else:
            pass

    elif cmd=='2':
        pass

    elif cmd=='=':
        dependency.autoinstall()

    elif cmd=='-':
        print('exiting!')
        exit()

    else:
        print('Input Unrecognized.')

