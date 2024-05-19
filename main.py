import os
import ctypes
from download import bluetooth, IMED, IntelVGA, NvidiaVGA, TP, LAN, Chipset, Chipset2, Chipset3
from install import ibluetooth, iIMED, iIntelVGA, iNvidiaVGA, iTP, iLAN, iChipset, iChipset2, iChipset3

def start():
    print("""
        **********************************************************
        
       \033[31m Install Wifi drivers before using program (1)\033[0m
          
        **********************************************************
    """)

    print("""
            1. Install WIFI drivers
            2. Download & Install drivers
            3. Download Drivers
            4. \033[31mInstall one driver [✘]\033[0m
    """)

    ask = int(input("Choose action: "))
    if ask == 1:
        os.system("pnputil /add-driver Wifi\\Netwtw04.INF /install")
        os.system("pnputil /add-driver Wifi\\Netwtw06.INF /install")
        os.system("pnputil /add-driver Wifi\\Netwtw6e.INF /install")
        os.system("pnputil /add-driver Wifi\\Netwtw08.INF /install")
        os.system("cls")
        start()
    elif ask == 2:
        os.system("cls")
        bluetooth(), IMED(), TP(), Chipset(), Chipset2(), Chipset3(), LAN(), IntelVGA(), NvidiaVGA()
        ibluetooth(), iIMED(), iTP(), iChipset(), iChipset2(), iChipset3(), iLAN(), iIntelVGA(), iNvidiaVGA()
    elif ask == 3:
        os.system("cls")
        bluetooth(), IMED(), TP(), Chipset(), Chipset2(), Chipset3(), LAN(), IntelVGA(), NvidiaVGA()
    elif ask == 4:
        os.system("cls")
        start()
        
if ctypes.windll.shell32.IsUserAnAdmin():
    start()
else:
    print("""
    ****************************************************
          
        PLEASE RUN PROGRAM AS ADMINISTRATOR!
          
    ****************************************************
 """)


