import ctypes, sys, subprocess, webbrowser

import os.path
import time

path=(r'C:\Users\localadmin\Downloads\CineNet.Installer_3.6.0-dev.350.exe')
time_to_wait = 10
time_counter = 0

def download():
    webbrowser.open('http://teamcity/guestAuth/repository/download/CinemassiveMain_InstallCreatorForMaster/74479:id/CineNet.Installer_3.6.0-dev.350.exe');
    def isthedldone():
        while not os.path.exists(path):
            time.sleep(1)
            time_counter += 1
            if time_counter > time_to_wait:break
            if os.path.isfile(path):
                return is_admin()
        else:
            raise ValueError("%s isn't a file!" % path)
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    subprocess.run([r'C:\Users\localadmin\Downloads\CineNet.Installer_3.6.0-dev.350.exe'])
else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1);

print("done")
