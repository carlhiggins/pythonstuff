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

