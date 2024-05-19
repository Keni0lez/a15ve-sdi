import os
print("""
        1. Install WIFI drivers
        2. Download & Install drivers
        3. Download Drivers
        4. Custom driver (didn't work)

""")
ask = int(input("Choose action: "))
if ask == 1:
    os.system("pnputil /add-driver Wifi\\Netwtw04.INF /install")
    os.system("pnputil /add-driver Wifi\\Netwtw06.INF /install")
    os.system("pnputil /add-driver Wifi\\Netwtw6e.INF /install")
    os.system("pnputil /add-driver Wifi\\Netwtw08.INF /install")
elif ask == 2:
