import requests
import zipfile
import io
import os
from tqdm import tqdm

home = os.path.expanduser('~')
downloads = os.path.join(home, 'Downloads')

success = "Unarchived!"
notsuccess = "Download Error"

def bluetooth():
    url = "https://download.msi.com/nb_drivers/bt/PHBTW65817_22.180.0.2G_22.180.0.2_0x6c0c33e9.zip"  
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        total_size = int(response.headers.get('content-length', 0))
        block_size = 1024
        progress_bar = tqdm(total=total_size, unit='iB', unit_scale=True)
        with open(downloads + "\\bluetooth.zip", 'wb') as f:
            for data in response.iter_content(block_size):
                progress_bar.update(len(data))
                f.write(data)
        progress_bar.close()
        with zipfile.ZipFile(downloads + "\\bluetooth.zip") as zip_ref:
            zip_ref.extractall(downloads + "\\bluetooth")
        os.remove(downloads + "\\bluetooth.zip")
        print(success)
        os.system(downloads + "\\bluetooth\\Win10_UWD\\WirelessSetup.exe")
    else:
        print(notsuccess)
    IMED()

def IMED():
    url = "https://download.msi.com/nb_drivers/me/Intel_CSME_SW_2242.3.34.0_Consumer_2240.3.4.0_0x7fdbbd2a.zip"  
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        total_size = int(response.headers.get('content-length', 0))
        block_size = 1024  # 1 Kibibyte
        progress_bar = tqdm(total=total_size, unit='iB', unit_scale=True)
        with open(downloads + "\\IMED.zip", 'wb') as f:
            for data in response.iter_content(block_size):
                progress_bar.update(len(data))
                f.write(data)
        progress_bar.close()
        with zipfile.ZipFile(downloads + "\\IMED.zip") as zip_ref:
            zip_ref.extractall(downloads + "\\IMED")
        os.remove(downloads + "\\IMED.zip")
        print(success)
        os.system(downloads + "\\IMED\\Intel_CSME_SW_2242.3.34.0_Consumer\\Installers\\Main_DCH\\SetupME.exe")
    else:
        print(notsuccess)
    TP()

def TP():
    url = "https://download.msi.com/nb_drivers/tp/Intel_SerialIO_30.100.2237.26_30.100.2237.26_0xdf27a9fc.zip"  
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        total_size = int(response.headers.get('content-length', 0))
        block_size = 1024  # 1 Kibibyte
        progress_bar = tqdm(total=total_size, unit='iB', unit_scale=True)
        with open(downloads + "\\TouchPad.zip", 'wb') as f:
            for data in response.iter_content(block_size):
                progress_bar.update(len(data))
                f.write(data)
        progress_bar.close()
        with zipfile.ZipFile(downloads + "\\TouchPad.zip") as zip_ref:
            zip_ref.extractall(downloads + "\\TouchPad")
        os.remove(downloads + "\\TouchPad.zip")
        print(success)
        os.system(downloads + "\\TouchPad\\install.bat")
    else:
        print(notsuccess)
    LAN()

def LAN():
    url = "https://download.msi.com/nb_drivers/lan/Install_PCIE_Win11_11.10.0720.2022_08232022_1168.10.720.2022_0xbf2bb9f0.zip"  
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        total_size = int(response.headers.get('content-length', 0))
        block_size = 1024  # 1 Kibibyte
        progress_bar = tqdm(total=total_size, unit='iB', unit_scale=True)
        with open(downloads + "\\LAN.zip", 'wb') as f:
            for data in response.iter_content(block_size):
                progress_bar.update(len(data))
                f.write(data)
        progress_bar.close()
        with zipfile.ZipFile(downloads + "\\LAN.zip") as zip_ref:
            zip_ref.extractall(downloads + "\\LAN")
        os.remove(downloads + "\\LAN.zip")
        print(success)
        os.system(downloads + "\\LAN\\Install_PCIE_Win11_11.10.0720.2022_08232022.exe")
    else:
        print(notsuccess)

def IntelVGA():
    url = "https://download.msi.com/nb_drivers/vga/Intel_VGA_31.0.101.4314_31.0.101.4314_0x26f4cecd.zip"  
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        total_size = int(response.headers.get('content-length', 0))
        block_size = 1024  # 1 Kibibyte
        progress_bar = tqdm(total=total_size, unit='iB', unit_scale=True)
        with open(downloads + "\\IntelVGA.zip", 'wb') as f:
            for data in response.iter_content(block_size):
                progress_bar.update(len(data))
                f.write(data)
        progress_bar.close()
        with zipfile.ZipFile(downloads + "\\IntelVGA.zip") as zip_ref:
            zip_ref.extractall(downloads + "\\IntelVGA")
        os.remove(downloads + "\\IntelVGA.zip")
        print(success)
        # os.system(downloads + "\\LAN\\Install_PCIE_Win11_11.10.0720.2022_08232022.exe")
    else:
        print(notsuccess)
def NvidiaVGA():
    url = "https://download.msi.com/nb_drivers/vga/1107254_537.24_GameReady_WHQL_31.0.15.3724_0x30e04b3b.zip"  
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        total_size = int(response.headers.get('content-length', 0))
        block_size = 1024  # 1 Kibibyte
        progress_bar = tqdm(total=total_size, unit='iB', unit_scale=True)
        with open(downloads + "\\NvidiaVGA.zip", 'wb') as f:
            for data in response.iter_content(block_size):
                progress_bar.update(len(data))
                f.write(data)
        progress_bar.close()
        with zipfile.ZipFile(downloads + "\\NvidiaVGA.zip") as zip_ref:
            zip_ref.extractall(downloads + "\\NvidiaVGA")
        os.remove(downloads + "\\NvidiaVGA.zip")
        print(success)
        # os.system(downloads + "\\LAN\\Install_PCIE_Win11_11.10.0720.2022_08232022.exe")

def Chipset():
    url = "https://download.msi.com/nb_drivers/cs/Intel_Chipset_10.1.19468.8385_10.1.19468.8385_0xcd599de1.zip"  
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        total_size = int(response.headers.get('content-length', 0))
        block_size = 1024  # 1 Kibibyte
        progress_bar = tqdm(total=total_size, unit='iB', unit_scale=True)
        with open(downloads + "\\Chipset.zip", 'wb') as f:
            for data in response.iter_content(block_size):
                progress_bar.update(len(data))
                f.write(data)
        progress_bar.close()
        with zipfile.ZipFile(downloads + "\\Chipset.zip") as zip_ref:
            zip_ref.extractall(downloads + "\\Chipset")
        os.remove(downloads + "\\Chipset.zip")
        print(success)
        # os.system(downloads + "\\LAN\\Install_PCIE_Win11_11.10.0720.2022_08232022.exe")

def Chipset2():
    url = "https://download.msi.com/nb_drivers/hdi/HIDEventFilterDriver-2.2.2.1_v3_RS5_19H1_20H1_21H2_22H2_Certified_2.2.2.1_0x185b20cf.zip"  
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        total_size = int(response.headers.get('content-length', 0))
        block_size = 1024  # 1 Kibibyte
        progress_bar = tqdm(total=total_size, unit='iB', unit_scale=True)
        with open(downloads + "\\Chipset2.zip", 'wb') as f:
            for data in response.iter_content(block_size):
                progress_bar.update(len(data))
                f.write(data)
        progress_bar.close()
        with zipfile.ZipFile(downloads + "\\Chipset2.zip") as zip_ref:
            zip_ref.extractall(downloads + "\\Chipset2")
        os.remove(downloads + "\\Chipset2.zip")
        print(success)
        # os.system(downloads + "\\LAN\\Install_PCIE_Win11_11.10.0720.2022_08232022.exe")

def Chipset3():
    url = "https://download.msi.com/nb_drivers/gna/gna-03.00.00.1457-win-3_0_sv2_resign-20220819_3.0.0.1457_0x9a3a0aa1.zip"  
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        total_size = int(response.headers.get('content-length', 0))
        block_size = 1024  # 1 Kibibyte
        progress_bar = tqdm(total=total_size, unit='iB', unit_scale=True)
        with open(downloads + "\\Chipset3.zip", 'wb') as f:
            for data in response.iter_content(block_size):
                progress_bar.update(len(data))
                f.write(data)
        progress_bar.close()
        with zipfile.ZipFile(downloads + "\\Chipset3.zip") as zip_ref:
            zip_ref.extractall(downloads + "\\Chipset3")
        os.remove(downloads + "\\Chipset3.zip")
        print(success)
        # os.system(downloads + "\\LAN\\Install_PCIE_Win11_11.10.0720.2022_08232022.exe")
bluetooth()
