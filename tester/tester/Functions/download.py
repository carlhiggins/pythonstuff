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
