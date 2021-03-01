import os
import platform
import psutil

def get_cpu():
    uname = platform.uname()
    print(f"\nName:\t\t"+uname.node.upper())
    print(f"System:\t\t"+uname.system)
    print(f"Release:\t"+uname.release)
    print(f"Machine:\t"+uname.machine)
    #CPU cores
    print("Phy Cores:\t" + str(psutil.cpu_count(logical=False)))
    print("Log Cores:\t"+str(psutil.cpu_count(logical=True))+'\n')
    #CPU frequencies
    # cpufreq = psutil.cpu_freq()
    # print(f"Max Freq: {cpufreq.max:.2f}Mhz")
    # print(f"Min Freq: {cpufreq.min:.2f}Mhz")
    # print(f"Cur Freq: {cpufreq.current:.2f}Mhz")
    return

def get_system():
    return platform.uname().system
