import os
from os import system as install
from datetime import datetime

def p():
    ct = datetime.now().strftime("%H:%M:%S")
    print(f"[{ct}]\033[32m Installed! \033[0m")

home = os.path.expanduser('~')
downloads = os.path.join(home, 'Downloads')

def ibluetooth():
    install(downloads + "\\bluetooth\\Win10_UWD\\WirelessSetup.exe")
    p()
def iIMED():
    install(downloads + "\\IMED\\Intel_CSME_SW_2242.3.34.0_Consumer\\Installers\\Main_DCH\\SetupME.exe")
    p()

def iTP():
    install(downloads + "\\TouchPad\\install.bat")
    p()

def iLAN():
    install(downloads + "\\LAN\\Install_PCIE_Win11_11.10.0720.2022_08232022.exe")
    p()

def iIntelVGA():
    install(downloads + "\\IntelVGA\\install.bat")
    p()

def iNvidiaVGA():
    install(downloads + "\\NvidiaVGA\\install.bat")
    p()

def iChipset():
    install(downloads + "\\Chipset\\install.bat")
    p()

def iChipset2():
    install(f"pnputil /add-driver {downloads}\\Chipset2\\drivers\\x64\\HidEventFilter.inf  /install")
    p()

def iChipset3():
    install(f"pnputil /add-driver {downloads}\\Chipset3\\gna.inf  /install")
    p()