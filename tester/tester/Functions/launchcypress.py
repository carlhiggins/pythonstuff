def cypress_start():
    p = subprocess.Popen(["powershell.exe", 
                r'C:\Users\localadmin\Desktop\CineTest\test1\startcypress.ps1'], 
                  stdout=sys.stdout)
    p.communicate()

