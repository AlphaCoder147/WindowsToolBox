from os import startfile, system
from os.path import isfile
from sys import exit
from time import sleep
from timeit import default_timer
from urllib.request import urlretrieve
from webbrowser import open as webopen
from platform import release
# This has to be here
start = default_timer()
try:
    # Custom / Community made libs
    from colorama import init, Fore, Back
    from lastversion import latest
    from ping3 import ping
    from psutil import cpu_count, cpu_percent, disk_usage, virtual_memory
    from XeLib import cls, printer, download, color, getmyping
    from XTLLib import fwrite, muulter, runaspowershell, SetVars
except:
    print("Fixing libraries, wait...")
    system("pip install -U psutil XeLib colorama lastversion XTLLib ping3")
    print("Libraries installed successfully!")

# This function provides some "quality of life" features to the program.
def runqol(froms, choose):
    # If the user inputs "99", exit the program.
    if choose == "99": 
        exit()
        
    # If the user inputs "h" or "H" and the `froms` parameter is not 0,
    # call the `helpe()` function with the `froms` parameter as an argument.
    elif froms != 0 and (choose == "h" or choose == "H"): 
        helpe(froms)
    else: 
        # Otherwise, print an error message and sleep for 3 seconds.
        print("No option named " + choose)
        sleep(3)

def achooser(choose, option):
    if option in choose or option.upper() in choose or option.capitalize() in choose or option.title() in choose or option.lower() in choose: return True

def linuxdl(distro):
    cls()
    if   distro == 1: tuxdl("[1] Cinnamon  ", "[2] MATE      ", "[3] Xfce      ", distro) # Linux Mint
    elif distro == 2: tuxdl("[1] Nvidia    ", "[2] RPI4      ", "[3] LTS       ", distro) # Pop!_OS
    elif distro == 3: tuxdl("[1] Ubuntu    ", "[2] Kubuntu   ", "[3] Lubuntu   ", distro) # Ubuntu
    elif distro == 4: tuxdl("[1] Latest    ", "[2] Bootstrap ", "              ", distro) # Arch Linux
    elif distro == 5: tuxdl("[1] Plasma    ", "[2] Xfce      ", "[3] MATE      ", distro) # Artix Linux OpenRC
    elif distro == 6: tuxdl("[1] Budgie    ", "[2] Plasma    ", "[3] GNOME     ", distro) # Solus
    elif distro == 7: tuxdl("[1] NetInst   ", "              ", "              ", distro) # Debian
    elif distro == 8: tuxdl("[1] DR460NIZED", "[2] GNOME     ", "[3] Xfce      ", distro) # Garuda Linux
    elif distro == 9: tuxdl("[1] Core      ", "[2] Lite      ", "              ", distro) # Zorin OS

# This function defines a function called `prep()`
# that checks the hardware requirements of the system
# and exits if they are not met.
def prep():
    # Clear the screen and print a message
    cls()
    printer.lprint("Initializing Libraries...")
    
    # Initialize the autoreset option of the colorama module
    init(autoreset=True)
    
    # Check the hardware requirements and ask the user
    # if they want to continue if the requirements are not met.
    printer.lprint("Checking hardware requirements...")
    if cpu_count(logical=True)<3 and cpu_count(logical=False)<2:
        printer.lprint("Your Processor don't meet the minimum hardware requirements (2C / 3T).\n"
                       "Do You want to continue anyways?")
        choose = input("("+Fore.GREEN+"Y"+Fore.WHITE+"/"+Fore.RED+"n"+Fore.WHITE + "): ")
        if achooser(choose, "n"): exit()

    if virtual_memory().total/1073741824<4:
        printer.lprint("Your RAM don't meet the minimum hardware requirements (4GB RAM).\n"
                       "Do You want to continue anyways?")
        choose = input("("+Fore.GREEN+"Y"+Fore.WHITE+"/"+Fore.RED+"n"+Fore.WHITE + "): ")
        if achooser(choose, "n"): exit()

    if int(release())<10:
        printer.lprint("Your windows version is older than 10, this program won't run. Upgrade to Windows 10/11 if you want to use this program.") ; exit(sleep(15))

    if not virtual_memory().total/1073741824<4 and cpu_count(logical=True)<3 and cpu_count(logical=False)<2 and int(release())<10:
        printer.lprint("All Hardware requirements met!")

# This function defines a function called `update()`
# that checks if the program is up to date and
# allows the user to update it if necessary.
def update():
    # Ask the user if they want to update the program
    print('Update?')
    doupdate = input("("+Fore.GREEN+"Y"+Fore.WHITE+"/"+Fore.RED+"n"+Fore.WHITE + "): ")
    
    # If the user does not want to update, print a message and do nothing
    if achooser(doupdate, "n"):
        print("Okey.")
        sleep(2)
        pass
    
    # If the user wants to update, try to download the latest version of the program
    # and run it. If the download fails, print an error message and exit.
    elif achooser(doupdate, "y"):
        printer.lprint("Updating...")
        try:
            # Download the latest version of the program
            download("https://github.com/xemulat/XToolbox/releases/download/v"+str(latest("xemulat/XToolbox"))+"/XTBox.exe", "XTBox."+str(latest("xemulat/XToolbox"))+".exe", "XTBox "+str(latest("xemulat/XToolbox")))
            startfile("XTBox."+str(latest("xemulat/XToolbox"))+".exe")
            exit()
        
        # If the download fails, print an error message and exit
        except:
            printer.lprint("Can't complete updates, aborting...") ; sleep(4) ; exit()

    # If the user's input is not "y" or "n", call the runqol() function and try updating again
    else: runqol(0, doupdate) ; update()

def dl(org, url, urlr, name):
    # Try and except so the program won't crash when the website isn't accesible
    try:
        if isfile(urlr) == True:
            printer.lprint("ERROR 1 - File " + urlr + " already exists!")
            chose = input(Fore.RED+"[S>] Overwrite?"+Fore.RESET+" ("+Fore.GREEN+"Y"+Fore.RESET+"/"+Fore.RED+"n"+Fore.RESET+"): ")
            if chose == "Y" or chose == "y": pass
            elif chose == "N" or chose == "n":
                if org == 1: p1()
                if org == 2: p2()
                if org == 3: p3()
            else: runqol(0, chose)
    except:
        printer.lprint("ERROR 2: Can't check for file overwrite. Missing file premissions?"); sleep(6)
    # Download module is located here.
    try:
        download(url, urlr, name)
        if name != "WindowsOnReins":
            startfile(urlr)
        if org == 1: p1()
        if org == 2: p2()
        if org == 3: p3()
        # Only `if` statements will work with this
    except:
        printer.lprint("ERROR 3: Can't download file from the server...") ; sleep(3)

# This function defines a function called `eula()`
# that prints a warning message and asks the user
# to agree to a license agreement.
def eula():
    cls()
    z = True
    
    # Run a loop as long as z is True
    while z == True:
        # Print a warning message and sleep for 3 seconds
        print("Do Not Dumb License v1\n"
              "I'm not responsible for your dumb.")
        sleep(3)
        
        # Ask the user if they agree to the license agreement
        agree = input("Do you agree? ("+Fore.GREEN+"Y"+Fore.WHITE+"/"+Fore.RED+"n"+Fore.WHITE + "): ")
        
        # If the user agrees, write "True" to the file EULA.XTB and set z to False
        if achooser(agree, "y"):
            print("You agreed to the EULA.")
            fwrite(0, 'EULA.XTB', 'True')
            z = False
        
        # If the user does not agree, exit the program
        elif achooser(agree, "n"):
            print("Ok, come back if you change your mind."); exit(sleep(3))
        
        # If the user's input is not "y" or "n", call the runqol() function
        else: runqol(0, agree)
    
    # Delete the variable z
    del z

def helpe(origin):
    cls()
    print(" ┌─────────────────────────────────────────────────────────────┐\n",
           "│  Keybind  │ Command                                         │\n",
           "│     H     │ Help Page (this page)                           │\n",
           "│     N     │ Next Page                                       │\n",
           "│     B     │ Back                                            │\n",
           "│     UN    │ Uninstalls The Program                          │\n",
           "│     99    │ Exit                                            │\n",
           "├─────────────────────────────────────────────────────────────┤\n",
           "│ Color     │ Meaning                                         │\n",
          f"│ {e}       │ Dangerous Option                                │\n",
          f"│ {ng}      │ Option that can f*ck up your PC                 │\n",
          f"│ {ree}     │ Recommended Option                              │\n",
           "├─────────────────────────────────────────────────────────────┤\n",
           "│ Error code │ Explanation                                    │\n",
           "│      1     │ File already exists                            │\n",
           "│      2     │ Can't check for file overwrite                 │\n",
           "│      3     │ Can't download file from the server            │\n",
           "├─────────────────────────────────────────────────────────────┤\n",
           "│ If scrips won't execute, press P                            │\n",
           "├─────────────────────────────────────────────────────────────┤\n",
           "│                   Press ENTER to go back.                   │\n",
           "└─────────────────────────────────────────────────────────────┘\n")
    d = input("> ")
    if achooser(d, 'p'): runaspowershell("Set-ExecutionPolicy Unrestricted -Scope CurrentUser", "SetExecutionPolicy")
    if origin == 1:   p1()
    elif origin == 2: p2()
    elif origin == 3: p3()

def chooseeset():
    while True:
        cls()
        print(" ┌─────────────────────────────────────────────────────────────────────┐\n"
              ' │ [1] ESET Smart Security Premium                                     │\n',
               "│ [2] ESET Internet Security                                          │\n",
               "│ [3] ESET NOD32 Antivirus                                            │\n",
               "│ [4] ESET NOD32 Antivirus Gamer Edition                              │\n",
               "│ [5] ESET Security for Small Office                                  │\n",
               "│                                                                     │\n",
               "├─────────┬──────────────────────────┬───────────┬──────────┬─────────┤\n"
              " │         │ Choose your ESET version │ 99 - Exit │ B - Back │         │\n"
              " └─────────┴──────────────────────────┴───────────┴──────────┴─────────┘\n")
        choose = input("> ")
        if choose == "1": dl(1, "https://proxy.eset.com/li-handler/?transaction_id=odcm_download|esetgwsprod|us|oks9ghjy5s2i61au5rnrfg0r1ykid0rnhqtbtnqroh93wfb7038207oeqw049nznldnid&branch=us&prod=essp", "ESETSmartSecurity.exe", "ESET Smart Security Premium")
        elif choose == "2": dl(1, "https://proxy.eset.com/li-handler/?transaction_id=odcm_download|esetgwsprod|us|oksm3adws43jeih7v7q1yzoind790asam1cuq0unxeww9d63ebma9syry3brmbass36id&branch=us&prod=eis", "ESETInternetSecurity.exe", "ESET Internet Security")
        elif choose == "3": dl(1, "https://proxy.eset.com/li-handler/?transaction_id=odcm_download|esetgwsprod|us|oksrvu6kmvzgtlav8e9m5ptig5lrtrx88hbdf3n6wqs2j3i3sniyl9slhlibh6t2vf7id&branch=us&prod=eav", "ESETNOD32.exe", "ESET NOD32 Antivirus")
        elif choose == "4": dl(1, "https://proxy.eset.com/li-handler/?transaction_id=odcm_download|esetgwsprod|us|okseuzentzl4e6u8vrufel57sww7unp7uwgtyg0na2e4o2bxmq4r8fds6qmfjz6fj6zid&branch=us&prod=eav", "ESETNOD32Gamer.exe", "ESET NOD32 Antivirus Gamer Edition")
        elif choose == "5": dl(1, "https://proxy.eset.com/li-handler/?transaction_id=odcm_download|esetgwsprod|us|okszgg8un2iekhydiszxmhrdmvxdo8aupvot9y3d5ifkm9rzslti7t5r2xitfxrefj4id&branch=us&prod=essp", "ESETForSmallOffice.exe", "ESET Security for Small Office")
        elif choose == "B" or choose == "b": p1()
        runqol(0, choose)

def choosekas():
    while True:
        cls()
        print(" ┌──────────────────────────────────────────────────────────────────────┐\n"
              ' │ [1] Kaspersky Internet Security                                      │\n',
               "│ [2] Kaspersky Anti-Virus                                             │\n",
               "│ [3] Kaspersky Total Security                                         │\n",
               "│                                                                      │\n",
               "├───────┬───────────────────────────────┬───────────┬──────────┬───────┤\n"
              " │       │ Choose your Kaspersky version │ 99 - Exit │ B - Back │       │\n"
              " └───────┴───────────────────────────────┴───────────┴──────────┴───────┘\n")
        choose = input("> ")
        if choose == "1": dl(1, "https://pdc2.fra5.pdc.kaspersky.com/DownloadManagers/68/b8/68b8f8f6-bdc4-4c66-8443-eadeca7f06b4/kis21.3.10.391en_26096.exe", "KasperskyInternetSecurity.exe", "Kaspersky Internet Security")
        elif choose == "2": dl(1, "https://pdc2.fra5.pdc.kaspersky.com/DownloadManagers/c6/25/c6250217-9ffe-44e1-8688-03b1a35548eb/kav21.3.10.391en_26075.exe", "KasperskyAnti-Virus.exe", "Kaspersky Anti-Virus")
        elif choose == "3": dl(1, "https://pdc1.fra5.pdc.kaspersky.com/DownloadManagers/51/45/51454099-c33b-41aa-955d-13965a37f561/kts21.3.10.391en_26099.exe", "KasperskyTotalSecurity.exe", "Kaspersky Total Security")
        elif choose == "B" or choose == "b": p1()
        runqol(0, choose)

def quicktweaks():
    while True:
        cls()
        print(" ┌──────────────────────────┬──────────────────────────┐\n"
             f' │ [1] {AntiTrackTi}        │ [7] NoXboxBloat         R│\n',
              f"│ [2] NoNetworkAuto-Tune   │ [8] {LimitQ}            R│\n",
              f"│ [3] {optimizess}        R│ [9] XanderTweak         R│\n",
               "│ [4] NoActionCenter      R│ [10] AddCopyPath        R│\n",
               "│ [5] NoNews              R│ [11] DarkMode           R│\n",
               "│ [6] NoOneDrive           │ [12] AddTakeOwnership   R│\n",
               "│                          │                          │\n",
               "├────┬────────────────────┬┴──────────┬──────────┬────┤\n"
              " │    │ Choose your Tweaks │ 99 - Exit │ B - Back │    │\n"
              " └────┴────────────────────┴───────────┴──────────┴────┘\n")
        choose = input("> ")

        if choose == "1": dl(99, "https://raw.githubusercontent.com/xemulat/Windows-Toolkit/main/files/AntiTrackTime.bat", "AntiTrackTime.bat", "AntiTrackTime")
        elif choose == "2": urlretrieve("https://raw.githubusercontent.com/xemulat/Windows-Toolkit/main/files/Enable%20Window%20Network%20Auto-Tuning.bat", "NoNetworkAutotuneREVERT.bat") ;  dl(99, "https://raw.githubusercontent.com/xemulat/Windows-Toolkit/main/files/Disable%20Window%20Network%20Auto-Tuning.bat", "NoNetworkAutoTune.bat", "NoNetworkAutoTune")
        elif choose == "3": dl(99, "https://raw.githubusercontent.com/tcja/Windows-10-tweaks/master/SSD_Optimizations.reg", "OptimizeSSD.reg", "OptimizeSSD")
        elif choose == "4": dl(99, "https://raw.githubusercontent.com/tcja/Windows-10-tweaks/master/Disable_Action_Center.reg", "NoActionCenter.reg", "NoActionCenter")
        elif choose == "5": dl(99, "https://raw.githubusercontent.com/tcja/Windows-10-tweaks/master/Disable_News_and_Interests_on_taskbar_feature_for_all_users.reg", "NoNews.reg", "NoNews")
        elif choose == "6": dl(99, "https://raw.githubusercontent.com/tcja/Windows-10-tweaks/master/OneDrive_Uninstaller_v1.2.bat", "NoOneDrive.bat", "NoOneDrive")
        elif choose == "7": dl(99, "https://raw.githubusercontent.com/tcja/Windows-10-tweaks/master/RemoveXboxAppsBloat.bat", "NoXboxBloat.bat", "NoXboxBloat")
        elif choose == "8": dl(99, "https://raw.githubusercontent.com/tcja/Windows-10-tweaks/master/QoS_Limiter.reg", "LimitQoS.reg", "LimitQoS")
        elif choose == "9": dl(99, "https://raw.githubusercontent.com/tcja/Windows-10-tweaks/master/other_scripts/XanderBaatzTweaks.reg", "XanderTweak.reg", "Xander Tweak")
        elif choose == "10": dl(99, "https://raw.githubusercontent.com/tcja/Windows-10-tweaks/master/Add_Copy_path_to_context_menu.reg", "AddCopyPath.reg", "AddCopyPath")
        elif choose == "11": dl(99, "https://raw.githubusercontent.com/tcja/Windows-10-tweaks/master/darkmodetoggle/darkmodeON.reg", "DarkModeON.reg", "DarkMode")
        elif choose == "12": dl(99, r"https://raw.githubusercontent.com/couleurm/couleurstoolbox/main/3%20Windows%20Tweaks/0%20Quality%20of%20life%20tweaks/Take%20Ownership%20in%20context%20menu/Add%20Take%20Ownership.reg", "AddTakeOwnership.reg", "AddTakeOwnership")
        elif choose == "B" or choose == "b": p1()
        runqol(0, choose)
    
def tuxdl(line1ddddddd, line2ddddddd, line3ddddddd, distro):
    while True:
        print(f" ┌───────────────────────────────┐\n",
               f'│ {line1ddddddd}                │\n',
               f"│ {line2ddddddd}                │\n",
               f"│ {line3ddddddd}                │\n",
               f"│                               │\n",
               f"├───────────────────────────────┤\n",
               f"│    Choose your Distro Type    │\n",
               f"└───────────────────────────────┘\n")
        choose = input("> ")

        if   distro == 1: # Linux Mint 21 - Vanessa
            if   choose == "1":  dl(2, "https://mirror.rackspace.com/linuxmint/iso/stable/21/linuxmint-21-cinnamon-64bit.iso", "LinuxMint-21.3-Cinnamon.iso", "Linux Mint Cinnamon")
            elif choose == "2":  dl(2, "https://mirror.rackspace.com/linuxmint/iso/stable/21/linuxmint-21-mate-64bit.iso", "LinuxMint-21.3-MATE.iso", "Linux Mint MATE")
            elif choose == "3":  dl(2, "https://mirror.rackspace.com/linuxmint/iso/stable/21/linuxmint-21-xfce-64bit.iso", "LinuxMint-21.3-Xfce.iso", "Linux Mint Xfce")
            runqol(0, choose)

        elif distro == 2: # Pop!_OS - 19
            if   choose == "1":  dl(2, "https://iso.pop-os.org/22.04/amd64/nvidia/19/pop-os_22.04_amd64_nvidia_19.iso", "PopOS-Nvidia.iso", "Pop!_OS Nvidia")
            elif choose == "2":  dl(2, "https://iso.pop-os.org/22.04/arm64/raspi/2/pop-os_22.04_arm64_raspi_2.img.xz", "PopOS-RPI4.img.xz", "Pop!_OS RPI 4 Tech Previwe")
            elif choose == "3":  dl(2, "https://iso.pop-os.org/22.04/amd64/intel/19/pop-os_22.04_amd64_intel_19.iso", "PopOS-LTS.iso", "Pop!_OS LTS")
            runqol(0, choose)

        elif distro == 3: # Ubuntu - 22.10 Kinetic Kudu
            if   choose == "1":  dl(2, "https://releases.ubuntu.com/22.10/ubuntu-22.10-desktop-amd64.iso", "Ubuntu.iso", "Ubuntu")
            elif choose == "2":  dl(2, "https://cdimage.ubuntu.com/kubuntu/releases/22.10/release/kubuntu-22.10-desktop-amd64.iso", "Kubuntu.iso", "Kubuntu")
            elif choose == "3":  dl(2, "https://cdimage.ubuntu.com/lubuntu/releases/22.10/release/lubuntu-22.10-desktop-amd64.iso", "Lubuntu.iso", "Lubuntu")
            runqol(0, choose)

        elif distro == 4: # Arch Linux - 2022.10.01
            if   choose == "1":  dl(2, "https://mirror.rackspace.com/archlinux/iso/2022.10.01/archlinux-2022.10.01-x86_64.iso", "Arch-2022.10.iso", "Arch 2022.10")
            elif choose == "2":  dl(2, "https://mirror.rackspace.com/archlinux/iso/2022.10.01/archlinux-x86_64.iso", "Arch-Old.iso", "Arch Old")
            runqol(0, choose)

        elif distro == 5: # Artix Linux OpenRC - 20220713
            if   choose == "1":  dl(2, "https://mirrors.dotsrc.org/artix-linux/iso/artix-plasma-openrc-20220713-x86_64.iso", "Artix-Plasma.iso", "Artix Plasma")
            elif choose == "2":  dl(2, "https://mirrors.dotsrc.org/artix-linux/iso/artix-xfce-openrc-20220713-x86_64.iso", "Artix-Xfce.iso", "Artix Xfce")
            elif choose == "3":  dl(2, "https://mirrors.dotsrc.org/artix-linux/iso/artix-mate-openrc-20220713-x86_64.iso", "Artix-MATE.iso", "Artix MATE")
            runqol(0, choose)

        elif distro == 6: # Solus - 4.3
            if   choose == "1":  dl(2, "https://mirrors.rit.edu/solus/images/4.3/Solus-4.3-Budgie.iso", "Solus-Budgie.iso", "Solus Budgie")
            elif choose == "2":  dl(2, "https://mirrors.rit.edu/solus/images/4.3/Solus-4.3-Plasma.iso", "Solus-Plasma.iso", "Solus Plasma")
            elif choose == "3":  dl(2, "https://mirrors.rit.edu/solus/images/4.3/Solus-4.3-GNOME.iso", "Solus-GNOME.iso", "Solus GNOME")
            runqol(0, choose)

        elif distro == 7: # Debian - 11.5.0
            if   choose == "1":  dl(2, "https://cdimage.debian.org/debian-cd/current/amd64/iso-cd/debian-11.5.0-amd64-netinst.iso", "Debian-NetInst.iso", "Debian NetInstall")
            runqol(0, choose)

        elif distro == 8: # Garuda Linux - Auto-Updates
            if   choose == "1":  dl(2, "https://iso.builds.garudalinux.org/iso/latest/garuda/dr460nized-gaming/latest.iso?fosshost=1", "Garuda-DR460NIZED.iso", "Garuda DR460NIZED Gaming")
            elif choose == "2":  dl(2, "https://iso.builds.garudalinux.org/iso/latest/garuda/gnome/latest.iso?fosshost=1", "Garuda-GNOME.iso", "Garuda GNOME")
            elif choose == "3":  dl(2, "https://iso.builds.garudalinux.org/iso/latest/garuda/xfce/latest.iso?fosshost=1", "Garuda-Xfce.iso", "Garuda Xfce")
            runqol(0, choose)
        
        elif distro == 9: # Zorin OS - 16.2
            if   choose == "1":  dl(2, "https://mirrors.edge.kernel.org/zorinos-isos/16/Zorin-OS-16.2-Core-64-bit.iso", "ZorinOS-Core.iso", "Zorin OS Core")
            elif choose == "2":  dl(2, "https://mirrors.edge.kernel.org/zorinos-isos/16/Zorin-OS-16.2-Lite-64-bit.iso", "ZorinOS-Lite.iso", "Zorin OS Lite")
            runqol(0, choose)

def multidl(file):
    if   file == "ReviOS": muulter(2, "https://archive.org/download/revi-os-11-22.10/ReviOS-11-22.10.iso", "ReviOS 11", "ReviOS 11", "ReviOS-11.iso", 
                                      "https://archive.org/download/revi-os-10-22.10/ReviOS-10-22.10.iso", "ReviOS 10", "ReviOS 10", "ReviOS-10.iso", False, False, False, False)

    elif file == "AtlasOS": muulter(2, "https://github.com/Atlas-OS/atlas-releases/releases/download/20H2-v0.5.2/Atlas_v0.5.2_21H2.iso", "21H2 + Faceit", "AtlasOS 21H2", "AtlasOS-21H2.iso",
                                       "https://github.com/Atlas-OS/atlas-releases/releases/download/20H2-v0.5.2/Atlas_v0.5.2.iso", "20H2 + Better than Old", "AtlasOS 20H2", "AtlasOS-20H2.iso",
                                       "https://github.com/Atlas-OS/atlas-releases/releases/download/1803/Atlas_1803_v0.2.iso", "1803 + Old version", "AtlasOS 1803", "AtlasOS-1803.iso")

    elif file == "SimplifyWindows": muulter(2, "https://github.com/WhatTheBlock/WindowsSimplify/releases/download/iso/22621.525_221014.iso", "1.66GB - Extreme Lite with Store", "WindowsSimplify-1.66GB", "WindowsStimplfy-1.iso", 
                                               "https://github.com/WhatTheBlock/WindowsSimplify/releases/download/iso/22623.746_221018.iso", "1.73GB - No Windows Update", "WindowsSimplify-1.73GB", "WindowsSimplify-2.iso",
                                               "https://archive.org/download/simplify-windows-v2/22621.317_220811-2.iso", "1.83GB - Max Debloat", "WindowsSimplify-1.83GB", "WindowsStimplfy-3.iso")

    elif file == "Prism": muulter(3, "https://github.com/PrismLauncher/PrismLauncher/releases/download/"+str(latest("PrismLauncher/PrismLauncher"))+"/PrismLauncher-Windows-Portable-"+str(latest("PrismLauncher/PrismLauncher"))+".zip", "PrismLauncher Portable", "Portable", "PrismLauncher-Portable.zip", 
                                     "https://github.com/PrismLauncher/PrismLauncher/releases/download/"+str(latest("PrismLauncher/PrismLauncher"))+"/PrismLauncher-Windows-Setup-"+str(latest("PrismLauncher/PrismLauncher"))+".exe", "PrismLauncher Setup", "Setup", "PrismLauncher-Setup.exe", False, False, False, False)
    
    elif file == "GDLauncher": muulter(3, "https://github.com/gorilla-devs/GDLauncher/releases/download/v"+str(latest("gorilla-devs/GDLauncher"))+"/GDLauncher-win-portable.zip", "GDLauncher Portable", "Portable", "GDLauncher-Portable.zip", 
                                          "https://github.com/gorilla-devs/GDLauncher/releases/download/v"+str(latest("gorilla-devs/GDLauncher"))+"/GDLauncher-win-setup.exe", "GDLauncher Setup", "Setup", "GDLauncher-Setup.exe", False, False, False, False)

    elif file == "OpenAsar":
        fwrite(1, 'openasar.bat', r'@echo off\n'
                                  r'C:\Windows\System32\TASKKILL.exe /f /im Discord.exe' + "\n"
                                  r'C:\Windows\System32\TASKKILL.exe /f /im Discord.exe' + "\n"
                                  r'C:\Windows\System32\TASKKILL.exe /f /im Discord.exe' + "\n"
                                  r'C:\Windows\System32\TIMEOUT.exe /t 5 /nobreak' + "\n"
                                  r'copy /y "%localappdata%\Discord\app-1.0.9007\resources\app.asar" "%localappdata%\Discord\app-1.0.9007\resources\app.asar.backup"' + "\n"
                                  r'powershell -Command "Invoke-WebRequest https://github.com/GooseMod/OpenAsar/releases/download/nightly/app.asar -OutFile \"$Env:LOCALAPPDATA\Discord\app-1.0.9007\resources\app.asar\""' + "\n"
                                  r'start "" "%localappdata%\Discord\Update.exe" --processStart Discord.exe' + "\n"
                                  r'goto 2>nul & del "%~f0"')

# ==========< Main program loops
def p1():
    while True:
        cls()
        print(f" ┌───────────────────────────────────────────────────┬─────────────────────────────────────────────────────────────────┐\n", 
               f"│ {xtoolboxvv1asdfghjzz}                            │ Made by {xemulatddddd}         │ Internet: {qwert}              │\n",
               f"│ Update Status: {Errorhd} │ RAM: {ramavailz}       │ CPU: {cpuavailifffff} | {c}    │ Disk: {dusagehebeded}          │\n",
               f"├──────────────────────────┼────────────────────────┼────────────────────────────────┼────────────────────────────────┤\n", 
               f"│ [D] Debloat              │ [T] Tweaks             │ [A] Apps                       │ [C] Cleaning / Antiviruses     │\n",
               f"├──────────────────────────┼────────────────────────┼────────────────────────────────┼────────────────────────────────┤\n", 
               f"│ [1] EchoX                │ [1] {posttweaksjfjfjf} │ [1] Chocholatey                │ [1] ADW Cleaner                │\n",
               f"│ [2] {neCtrl}             │ [2] Insider Enroller   │ [2] {rav}                      │ [2] ATF Cleaner                │\n",
               f"│ [3] ShutUp10             │ [3] Windows11Fixer     │ [3] {firef}                    │ [3] Defraggler                 │\n",
               f"│ [4] Optimizer            │ [4] AntiRoundCorners   │ [4] Lively Wallpaper           │ [4] {malwarebyt}               │\n",
               f"│ [5] PyDebloatX           │ [5] FixDrag&Drop       │ [5] LibreWolf                  │ [5] ESET Online Scanner        │\n",
               f"│ [6] {windowsonreinddddd} │ [6] Winaero Tweaker    │ [6] qBittorrent                │ [6] ESET                       │")
        print(f" │ [7] QuickBoost           │ [7] CTT WinUtil        │ [7] Rainmeter                  │ [7] Kaspersky                  │\n",
               f"│ [8] Win10Debloater       │ [8] REAL               │ [8] 7-Zip                      │ [8] CleanMGR+                  │\n",
               f"│ [9] SadCoy               │ [9] NVSlimmer          │ [9] Memory Cleaner             │ [9] Glary Utilities            │\n",
               f"│ [10] {sweetyli}          │                        │ [10] Compact Memory Cleaner    │                                │\n",
               f"│ [11] {ohdwindowwwwwwwww} │                        │                                │                                │\n",
               f"│ [12] WindowsSpyBlocker   │                        │                                │                                │\n",
               f"│ [13] PrivateZilla        │                        │                                │                                │\n",
               f"│ [14] ZusierAIO           │                        │                                │                                │\n",
               f"│ [15] Azurite             │ [QT] {quicktwea}       │                                │                                │\n",
               f"│                          │                        │                                │                                │\n",
               f"├──────────────────────────┴────────────────────────┴────────────────────────────────┴────────────────────────────────┤\n",
               f"│                           Ex.: 'D2' ─ HoneCtrl │ N ─ Next Page │ 99 ─ Exit │ H - Help                           1/3 │\n",
               f"└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘")
        choose = input("> ")

        # =============< Debloat
        if   achooser(choose, "d1"):  dl(1, "https://github.com/UnLovedCookie/EchoX/releases/latest/download/EchoX.bat", "EchoX.bat", "EchoX")
        elif achooser(choose, "d2"):  dl(1, "https://github.com/auraside/HoneCtrl/releases/latest/download/HoneCtrl.bat", "HoneCtrl.bat", "HoneCtrl")
        elif achooser(choose, "d3"):  dl(1, "https://dl5.oo-software.com/files/ooshutup10/OOSU10.exe", "ShutUp10.exe", "ShutUp10")
        elif achooser(choose, "d4"):  dl(1, "https://github.com/hellzerg/optimizer/releases/latest/download/Optimizer-" + str(latest("hellzerg/optimizer")) + ".exe", "Optimizer.exe", "Optimizer")
        elif achooser(choose, "d5"):  dl(1, "https://github.com/Teraskull/PyDebloatX/releases/latest/download/PyDebloatX_portable.exe", "PyDebloatX.exe", "PyDebloatX")
        elif achooser(choose, "d6"):  dl(1, "https://raw.githubusercontent.com/gordonbay/Windows-On-Reins/master/wor.ps1", "WindowsOnReins.ps1", "WindowsOnReins")
        elif achooser(choose, "d7"):  dl(1, "https://github.com/SanGraphic/QuickBoost/releases/latest/download/QuickBoost.exe", "QuickBoost.exe", "QuickBoost")
        elif achooser(choose, "d8"):  runaspowershell("iwr -useb https://git.io/debloat|iex", "Win10Debloat")
        elif achooser(choose, "d9"):  dl(1, "https://github.com/Jisll/Sadcoy/releases/latest/download/Sadcoy.exe", "Sadcoy.exe", "Sadcoy")
        elif achooser(choose, "d10"): dl(1, "https://raw.githubusercontent.com/xemulat/MyFilesForDDL/main/SweetyLite2.bat", "SweetyLite.bat", "SweetyLite")
        elif achooser(choose, "d11"): runaspowershell("iwr -useb 'https://simeononsecurity.ch/scripts/windowsoptimizeandharden.ps1'|iex", "OHDWindows")
        elif achooser(choose, "d12"): dl(1, "https://github.com/crazy-max/WindowsSpyBlocker/releases/latest/download/WindowsSpyBlocker.exe", "WindowsSpyBlocker.exe", "WindowsSpyBlocker")
        elif achooser(choose, "d13"): dl(1, "https://github.com/builtbybel/privatezilla/releases/latest/download/privatezilla.zip", "PrivateZilla.zip", "PrivateZilla")
        elif achooser(choose, "d14"): dl(1, "https://raw.githubusercontent.com/Zusier/Zusiers-optimization-Batch/master/Zusier%20AIO.bat", "ZusierAIO.bat", "ZusierAIO")
        elif achooser(choose, "d15"): dl(1, r"https://archive.org/download/azurite-v1.1.7-setup/Azurite%20Setup%201.1.7.exe", "Azurite.exe", "Azurite")

        # =============< Tweaks
        elif achooser(choose, "t1"):   dl(1, "https://raw.githubusercontent.com/ArtanisInc/Post-Tweaks/main/PostTweaks.bat", "PostTweaks.bat", "PostTweaks")
        elif achooser(choose, "t2"):   dl(1, "https://github.com/Jathurshan-2019/Insider-Enroller/releases/latest/download/Insider_Enrollerv" + str(latest("Jathurshan-2019/Insider-Enroller")) + ".zip", "InsiderEnroller.zip", "InsiderEnroller")
        elif achooser(choose, "t3"):   dl(1, "https://github.com/99natmar99/Windows-11-Fixer/releases/latest/download/Windows.11.Fixer.v" + str(latest("99natmar99/Windows-11-Fixer")) + ".Portable.zip", "Windows11Fixer.zip", "Windows11Fixer")
        elif achooser(choose, "t4"):   dl(1, "https://github.com/valinet/Win11DisableRoundedCorners/releases/latest/download/Win11DisableOrRestoreRoundedCorners.exe", "AntiRoundCorners.exe", "AntiRoundCorners")
        elif achooser(choose, "t5"):   dl(1, "https://github.com/HerMajestyDrMona/Windows11DragAndDropToTaskbarFix/releases/latest/download/Windows11DragAndDropToTaskbarFix.exe", "FixDragAndDrop.exe", "Fix Drag&Drop")
        elif achooser(choose, "t6"):   dl(1, "https://winaerotweaker.com/download/winaerotweaker.zip", "WinaeroTweaker.zip", "Winaero Tweaker")
        elif achooser(choose, "t7"):   runaspowershell("irm christitus.com/win | iex", "CTT")
        elif achooser(choose, "t8"):   dl(1, "https://github.com/miniant-git/REAL/releases/latest/download/REAL.exe", "REAL.exe", "REAL")
        elif achooser(choose, "t9"):   dl(1, "https://files1.majorgeeks.com/10afebdbffcd4742c81a3cb0f6ce4092156b4375/drivers/NVSlimmer_v0.13.zip", "NVSlimmer.zip", "NVSlimmer") # Mirror provided by majorgeeks
        elif choose == "QT" or choose == "qt" or choose == "Qt" or choose == "qT": quicktweaks()

        # =============< Apps
        elif achooser(choose, "a1"):  dl(1, "https://raw.githubusercontent.com/xemulat/Windows-Toolkit/main/files/choco.bat", "choco.bat", "Choco")
        elif achooser(choose, "a2"):  dl(1, "https://referrals.brave.com/latest/BraveBrowserSetup.exe", "Brave.exe", "Brave Browser")
        elif achooser(choose, "a3"):  dl(1, "https://download-installer.cdn.mozilla.net/pub/firefox/releases/105.0.3/win32/en-US/Firefox%20Installer.exe", "Firefox.exe", "Firefox")
        elif achooser(choose, "a4"):  dl(1, "https://github.com/rocksdanister/lively/releases/latest/download/lively_setup_x86_full_v" + str(latest("rocksdanister/lively")).replace(".", "") + ".exe", "LivelyWallpaper.exe", "Lively Wallpaper")
        elif achooser(choose, "a5"):  dl(1, "https://gitlab.com/librewolf-community/browser/windows/uploads/0d58d5bec60813087b17a865533914d5/librewolf-106.0.5-1.en-US.win64-setup.exe", "LibreWolf.exe", "LibreWolf")
        elif achooser(choose, "a6"):  dl(1, "https://github.com/c0re100/qBittorrent-Enhanced-Edition/releases/latest/download/qbittorrent-enhanced-" + str(latest("c0re100/qBittorrent-Enhanced-Edition")) + "-Qt6-setup.exe", "qBittorrent.exe", "qBittorrent")
        elif achooser(choose, "a7"):  dl(1, "https://github.com/rainmeter/rainmeter/releases/download/v4.5.16.3687/Rainmeter-4.5.16.exe", "Rainmeter.exe", "Rainmeter")
        elif achooser(choose, "a8"):  dl(1, "https://www.7-zip.org/a/7z2201-x64.exe", "7Zip.exe", "7-Zip")
        elif achooser(choose, "a9"):  dl(1, "https://www.koshyjohn.com/software/MemClean.exe", "MemoryCleaner.exe", "Memory Cleaner")
        elif achooser(choose, "a10"): dl(1, "https://github.com/qualcosa/Compact-RAM-Cleaner/releases/latest/download/Compact.RAM.Cleaner.exe", "CompactMemoryCleaner.exe", "Compact Memory Cleaner")

        # =============< Cleanup
        elif achooser(choose, "c1"):  dl(1, "https://adwcleaner.malwarebytes.com/adwcleaner?channel=release", "ADW-Cleaner.exe", "ADW Cleaner")
        elif achooser(choose, "c2"):  dl(1, "https://files1.majorgeeks.com/10afebdbffcd4742c81a3cb0f6ce4092156b4375/drives/ATF-Cleaner.exe", "ATF-Cleaner.exe", "ATF Cleaner")
        elif achooser(choose, "c3"):  dl(1, "https://download.ccleaner.com/dfsetup222.exe", "Defraggler.exe", "Defraggler")
        elif achooser(choose, "c4"):  dl(1, "https://www.malwarebytes.com/api/downloads/mb-windows?filename=MBSetup-37335.37335.exe", "Malwarebytes.exe", "Malwarebytes")
        elif achooser(choose, "c5"):  dl(1, "https://download.eset.com/com/eset/tools/online_scanner/latest/esetonlinescanner.exe", "ESETOnlineScanner.exe", "ESET Online Scanner")
        elif achooser(choose, "c6"):  chooseeset()
        elif achooser(choose, "c7"):  choosekas()
        elif achooser(choose, "c8"):  dl(1, "https://github.com/builtbybel/CleanmgrPlus/releases/latest/download/cleanmgrplus.zip", "CleanmgrPlus.zip", "CleanmgrPlus")
        elif achooser(choose, "c9"):  dl(1, "https://download.glarysoft.com/gu5setup.exe", "GlaryUtilities.exe", "Glary Utilities")

        # =============< QOL Lines
        elif choose == "n" or choose == "N": p2()
        elif choose == "b" or choose == "B": p3()
        else: runqol(1, choose)

def p2():
    while True:
        cls()
        print(f" ┌───────────────────────────────────────────────────┬────────────────────────────────┬────────────────────────────────┐\n", 
               f"│ {xtoolboxvv1asdfghjzz}                            │ Made by {xemulatddddd}         │ Internet: {qwert}              │\n",
               f"│ Update Status: {Errorhd} │ RAM: {ramavailz}       │ CPU: {cpuavailifffff} | {c}    │ Disk: {dusagehebeded}          │\n",
               f"├──────────────────────────┼────────────────────────┼────────────────────────────────┼────────────────────────────────┤\n", 
               f"│ [L] Linux Distros        │ [W] Windows versions   │ [M] Modded Windows versions    │ [T] Tools                      │\n",
               f"├──────────────────────────┼────────────────────────┼────────────────────────────────┼────────────────────────────────┤\n", 
               f"│ [1] {minttuxe}           │ [1] {window11}         │ [1] {rectify}                  │ [1] {ruf}                      │\n",
               f"│ [2] Pop!_OS              │ [2] Windows 10         │ [2] {atlaso}                   │ [2] Balena Etcher              │\n",
               f"│ [3] Ubuntu               │ [3] Windows 8.1        │ [3] Ghost Spectre              │ [3] {unetboot}                 │")
        print(f" │ [4] Arch Linux           │ [4] Windows 8          │ [4] ReviOS                     │ [4] HeiDoc Iso Downloader      │\n",
               f"│ [5] Artix Linux          │ [5] Windows 7          │ [5] GGOS                       │                                │\n",
               f"│ [6] Solus                │                        │ [6] {windowssimpli}            │                                │\n",
               f"│ [7] Debian               ├────────────────────────┤ [7] {aero}                     ├────────────────────────────────┤\n",
               f"│ [8] Garuda               │ [O] Other              │ [8] Tiny10                     │ [A] Apps                       │\n",
               f"│ [9] {zorino}             ├────────────────────────┤ [9] KernelOS                   ├────────────────────────────────┤\n",
               f"│                          │ [1] .NET 4.8 SDK       │ [10] Windows 7 Super Nano      │ [1] KeePassXC                  │\n",
               f"│                          │ [2] DirectX AIO        │ [11] Windows 11 Debloated      │ [2] PowerToys                  │\n",
               f"│                          │ [3] VisualCppRedist    │                                │ [3] Alacritty                  │\n",
               f"│                          │ [4] XNA Framework      │                                │ [4] PowerShell                 │\n",
               f"│                          │ [5] Python             │                                │ [5] Motrix                     │\n",
               f"│                          │                        │                                │ [6] Files                      │\n",
               f"│                          │                        │                                │                                │\n",
               f"├──────────────────────────┴────────────────────────┴────────────────────────────────┴────────────────────────────────┤\n",
               f"│                           Ex.: 'D2' ─ HoneCtrl │ N ─ Next Page │ 99 ─ Exit │ H - Help                           2/3 │\n",
               f"└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘")
        choose = input("> ")

        # =============< TUX BLOCK | BOTTOM TEXT
        if   achooser(choose, "l1"): linuxdl(1) # Linux Mint 21         Vanessa
        elif achooser(choose, "l2"): linuxdl(2) # Pop!_OS               22.04
        elif achooser(choose, "l3"): linuxdl(3) # Ubuntu                22.10 Kinetic Kudu
        elif achooser(choose, "l4"): linuxdl(4) # Arch Linux            2022.10.01
        elif achooser(choose, "l5"): linuxdl(5) # Artix Linux           20220713
        elif achooser(choose, "l6"): linuxdl(6) # Solus                 4.3
        elif achooser(choose, "l7"): linuxdl(7) # Debian                11.5.0
        elif achooser(choose, "l8"): linuxdl(8) # Garuda Linux          Auto-Updates
        elif achooser(choose, "l9"): linuxdl(9) # Zorin OS              16.2

        # =============< Windows isos
        elif achooser(choose, "w1"): webopen("https://www.microsoft.com/software-download/windows11"); p2()
        elif achooser(choose, "w2"): webopen("https://www.microsoft.com/software-download/windows10"); p2()
        elif achooser(choose, "w3"): dl(2, r"https://dl.malwarewatch.org/windows/Windows%208.1%20%28x64%29.iso", "Windows-8.1.iso", "Windows 8.1")
        elif achooser(choose, "w4"): dl(2, r"https://dl.malwarewatch.org/windows/Windows%208%20%28x64%29.iso", "Windows-8.iso", "Windows 8")
        elif achooser(choose, "w5"): dl(2, r"https://dl.malwarewatch.org/windows/Windows%207%20%28x64%29.iso", "Windows-7.iso", "Windows 7")

        # =============< Other
        elif achooser(choose, "o1"): dl(2, "https://download.visualstudio.microsoft.com/download/pr/6f083c7e-bd40-44d4-9e3f-ffba71ec8b09/d05099507287c103a91bb68994498bde/ndp481-web.exe", ".NET-4.8-SDK.exe", ".NET 4.8 SDK")
        elif achooser(choose, "o2"): dl(2, "https://download.microsoft.com/download/1/7/1/1718CCC4-6315-4D8E-9543-8E28A4E18C4C/dxwebsetup.exe", "DirectX-AIO.exe", "DirectX AIO")
        elif achooser(choose, "o3"): dl(2, "https://github.com/abbodi1406/vcredist/releases/download/v0.64.0/VisualCppRedist_AIO_x86_x64_64.zip", "VisualCppRedist.zip", "VisualCppRedist")
        elif achooser(choose, "o4"): dl(2, "https://download.microsoft.com/download/A/C/2/AC2C903B-E6E8-42C2-9FD7-BEBAC362A930/xnafx40_redist.msi", "XNAF.msi", "XNAF")
        elif achooser(choose, "o4"): dl(2, "https://www.python.org/ftp/python/3.11.1/python-3.11.1-amd64.exe", "Python.exe", "Python")

        # =============< Modded isos
        elif achooser(choose, "m1"): dl(2, r"https://archive.org/download/rectify-11-v-2/Rectify11%20%28v2%29.iso", "Rectify11.iso", "Rectify11 v2")
        elif achooser(choose, "m2"): multidl("AtlasOS")
        elif achooser(choose, "m3"): webopen("https://www.mediafire.com/file/2z30tuoy3ojsp3h/WIN10.PRO.20H2.SUPERLITE%2BCOMPACT.U3.X64.GHOSTSPECTRE.%28W%29.iso")
        elif achooser(choose, "m4"): multidl("ReviOS")
        elif achooser(choose, "m5"): dl(2, r"https://archive.org/download/ggos-0.8.20/ggos-0.8.20.iso", "GGOS.iso", "GGOS 0.8.20")
        elif achooser(choose, "m6"): multidl("SimplifyWindows")
        elif achooser(choose, "m7"): dl(2, r"https://dl.malwarewatch.org/windows/mods/Aero%2010%20%28x64%29.iso", "Aero10.iso", "Aero10")
        elif achooser(choose, "m8"): dl(2, r"https://dl.malwarewatch.org/windows/mods/Tiny%2010.iso", "Tiny10.iso", "Tiny10")
        elif achooser(choose, "m9"): dl(2, r"https://archive.org/download/kernel-os-22-h-2-beta/KernelOS%2022H2%20BETA.iso", "KernelOS.iso", "KernelOS")
        elif achooser(choose, "m10"): dl(2, r"https://dl.malwarewatch.org/windows/Windows%207%20%28SuperNano%29.iso", "Windows-7-SuperNano.iso", "Windows 7 Super Nano")
        elif achooser(choose, "m11"): dl(2, r"https://archive.org/download/windows-11-debloated/Windows%2011%20Debloated.iso", "Windows-11-Debloated.iso", "Windows 11 Debloated")

        # =============< Tools
        elif achooser(choose, "t1"): dl(2, "https://github.com/pbatard/rufus/releases/latest/download/rufus-"+str(latest("pbatard/rufus"))+".exe", "Rufus.exe", "Rufus")
        elif achooser(choose, "t2"): dl(2, "https://github.com/balena-io/etcher/releases/latest/download/balenaEtcher-Portable-"+str(latest("balena-io/etcher"))+".exe", "Etcher-Portable.exe", "Balena Etcher")
        elif achooser(choose, "t3"): dl(2, "https://github.com/unetbootin/unetbootin/releases/latest/download/unetbootin-windows-"+str(latest("unetbootin/unetbootin"))+".exe", "UNetBootin.exe", "UNetBootin")
        elif achooser(choose, "t4"): dl(2, "https://www.heidoc.net/php/Windows-ISO-Downloader.exe", "HeiDoc-ISO-Downloader.exe", "HeiDoc Ios Downloader")

        # =============< Tools
        elif achooser(choose, "a1"): dl(2, "https://github.com/keepassxreboot/keepassxc/releases/latest/download/KeePassXC-"+str(latest('keepassxreboot/keepassxc'))+"-Win64.msi", "KeePassXC.msi", "KeePassXC")
        elif achooser(choose, "a2"): dl(2, "https://github.com/microsoft/PowerToys/releases/latest/download/PowerToysSetup-"+(str(latest('microsoft/PowerToys'))).replace("v", "")+"-x64.exe", "PowerToys.exe", "PowerToys")
        elif achooser(choose, "a3"): dl(2, "https://github.com/alacritty/alacritty/releases/latest/download/Alacritty-"+str(latest('alacritty/alacritty'))+"-installer.msi", "", "Alacritty")
        elif achooser(choose, "a4"): dl(2, "https://github.com/PowerShell/PowerShell/releases/latest/download/PowerShell-"+(str(latest('PowerShell/PowerShell'))).replace("v", "")+"-win-x64.msi", "PowerShell.msi", "PowerShell")
        elif achooser(choose, "a5"): dl(2, "https://github.com/agalwood/Motrix/releases/latest/download/Motrix-Setup-"+(str(latest('agalwood/Motrix'))).replace("v", "")+".exe", "", "Motrix")
        elif achooser(choose, "a6"): dl(2, "https://files.community/appinstallers/Files.stable.appinstaller", "Files.appinstaller", "Files")

        # =============< QOL
        # Lines repeated every fucking time
        elif achooser(choose, "n"): p3()
        elif achooser(choose, "b"): p1()
        else: runqol(2, choose)

def p3():
    while True:
        cls()
        print(f" ┌───────────────────────────────────────────────────┬────────────────────────────────┬────────────────────────────────┐\n", 
               f"│ {xtoolboxvv1asdfghjzz}                            │ Made by {xemulatddddd}         │ Internet: {qwert}              │\n",
               f"│ Update Status: {Errorhd} │ RAM: {ramavailz}       │ CPU: {cpuavailifffff} | {c}    │ Disk: {dusagehebeded}          │\n",
               f"├──────────────────────────┼────────────────────────┼────────────────────────────────┼────────────────────────────────┤\n", 
               f"│ [L] Minecraft Launchers  │ [G] Game Launchers     │ [C] Minecraft Clients          │ [I] Misc                       │\n",
               f"├──────────────────────────┼────────────────────────┼────────────────────────────────┼────────────────────────────────┤\n", 
               f"│ [1] {offici}             │ [1] {ste}              │ [1] Tecknix                    │ [1] Achivment Watcher          │\n",
               f"│ [2] {prismlaunch}        │ [2] {upl}              │ [2] Salwyrr                    │ [2] {disco}                    │\n",
               f"│ [3] ATLaucnher           │ [3] Origin             │ [3] LabyMod                    │ [3] Spotify                    │\n",
               f"│ [4] {hm}                 │ [4] Epic Games         │ [4] {feath}                    │                                │\n",
               f"│ [5] XMCL                 │ [5] GOG Galaxy         │ [5] {lunarclien}               │                                │\n",
               f"│ [6] GDLauncher           │ [6] Paradox            │ [6] {cheatbreake}              │                                │\n",
               f"│                          │ [7] Roblox             │ [7] Badlion                    ├────────────────────────────────┤")
        print(f" │                          │                        │ [8] Crystal Client             │ [T] Tools                      │\n",
               f"│                          │                        │                                ├────────────────────────────────┤\n",
               f"│                          │                        │                                │ [1] {openas}                   │\n",
               f"│                          │                        │                                │ [2] Spicefy                    │\n",
               f"│                          │                        │                                │ [3] VenCord                    │\n",
               f"│                          │                        │                                │ [4] BetterDiscord              │\n",
               f"│                          │                        │                                │                                │\n",
               f"│                          │                        │                                │                                │\n",
               f"│                          │                        │                                │ // Sorry for so little tools   │\n",
               f"├──────────────────────────┴────────────────────────┴────────────────────────────────┴────────────────────────────────┤\n",
               f"│                           Ex.: 'D2' ─ HoneCtrl │ N ─ Next Page │ 99 ─ Exit │ H - Help                           3/3 │\n",
               f"└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘")
        choose = input("> ")

        # =============< Minecraft Launchers
        if   achooser(choose, "l1"): dl(3, "https://launcher.mojang.com/download/MinecraftInstaller.exe", "MinecraftInstaller.exe", "Minecraft Launcher")
        elif achooser(choose, "l2"): multidl("Prism")
        elif achooser(choose, "l3"): dl(3, "https://github.com/ATLauncher/ATLauncher/releases/latest/download/ATLauncher-"+str(latest("ATLauncher/ATLauncher"))+".exe", "ATLauncher.exe", "ATLauncher")
        elif achooser(choose, "l4"): dl(3, "https://github.com/huanghongxun/HMCL/releases/latest/download/HMCL-"+str(latest("huanghongxun/HMCL"))+".exe", "HMCL.exe", "HMCL")
        elif achooser(choose, "l5"): dl(3, "https://github.com/Voxelum/x-minecraft-launcher/releases/latest/download/xmcl-"+str(latest("Voxelum/x-minecraft-launcher"))+"-win32-x64.zip", "XMCL.zip", "XMCL")
        elif achooser(choose, "l6"): multidl("GDLauncher")

        # =============< Game Launchers
        elif achooser(choose, "g1"): dl(3, "https://cdn.cloudflare.steamstatic.com/client/installer/SteamSetup.exe", "Steam.exe", "Steam")
        elif achooser(choose, "g2"): dl(3, "https://ubistatic3-a.akamaihd.net/orbit/launcher_installer/UbisoftConnectInstaller.exe", "Uplay.exe", "Uplay")
        elif achooser(choose, "g3"): dl(3, "https://origin-a.akamaihd.net/EA-Desktop-Client-Download/installer-releases/EAappInstaller.exe", "Origin.exe", "Origin")
        elif achooser(choose, "g4"): dl(3, "https://launcher-public-service-prod06.ol.epicgames.com/launcher/api/installer/download/EpicGamesLauncherInstaller.msi", "Epic-Games.msi", "Epic Games")
        elif achooser(choose, "g5"): dl(3, "https://webinstallers.gog-statics.com/download/GOG_Galaxy_2.0.exe", "GOG-Galaxy.exe", "GOG Galaxy")
        elif achooser(choose, "g6"): dl(3, "https://launcher.paradoxinteractive.com/v2/paradox-launcher-installer-2022_12.msi", "Paradox.msi", "Paradox")
        elif achooser(choose, "g7"): dl(3, "https://setup.roblox.com/Roblox.exe", "Roblox.exe", "Roblox")

        # =============< Minecraft Clients
        elif achooser(choose, "c1"): dl(3, "https://tecknix.com/client/TecknixClient.exe", "Tecknix.exe", "Tecknix Client")
        elif achooser(choose, "c2"): dl(3, r"https://www.salwyrr.com/4/download/Salwyrr%20Launcher%20Installer.exe", "Salwyrr.exe", "Salwyrr CLients")
        elif achooser(choose, "c3"): dl(3, "https://dl.labymod.net/latest/install/LabyMod3_Installer.exe", "LabyMod.exe", "LabyMod")
        elif achooser(choose, "c4"): dl(3, r"https://launcher.feathercdn.net/dl/Feather%20Launcher%20Setup%201.4.4.exe", "FeatherLauncher.exe", "Feather Launcher")
        elif achooser(choose, "c5"): dl(3, r"https://launcherupdates.lunarclientcdn.com/Lunar%20Client%20v2.14.0.exe", "LunarClient.exe", "Lunar Client")
        elif achooser(choose, "c6"): dl(3, "https://github.com/Offline-CheatBreaker/Launcher/releases/latest/download/Offline_CheatBreaker_Setup.exe", "Offline-CheatBreaker.exe", "Offline CheatBreaker")
        elif achooser(choose, "c7"): dl(3, r"https://client-updates-cdn77.badlion.net/Badlion%20Client%20Setup%203.12.0.exe", "BadlionClient.exe", "Badlion Client")
        elif achooser(choose, "c8"): dl(3, "https://github.com/Crystal-Development-LLC/launcher-releases/releases/latest/download/crystal-client-launcher-setup.exe", "CrystalClient.exe", "Crystal Client")
        
        # =============< Misc
        elif achooser(choose, "i1"): dl(3, "https://github.com/xan105/Achievement-Watcher/releases/latest/download/Achievement.Watcher.Setup.exe", "Achievement-Watcher.exe", "Achievement Watcher")
        elif achooser(choose, "i2"): dl(3, "https://discord.com/api/downloads/distributions/app/installers/latest?channel=stable&platform=win&arch=x86", "Discord.exe", "Discord")
        elif achooser(choose, "i3"): dl(3, "https://download.scdn.co/SpotifySetup.exe", "Spotify.exe", "Spotify")
        
        # =============< Tools
        elif achooser(choose, "t1"): multidl("OpenAsar")
        elif achooser(choose, "t2"): runaspowershell("iwr -useb https://raw.githubusercontent.com/spicetify/spicetify-cli/master/install.ps1 | iex && iwr -useb https://raw.githubusercontent.com/spicetify/spicetify-marketplace/main/resources/install.ps1 | iex", "Spicefy")
        elif achooser(choose, "t3"): dl(3, "https://github.com/Vendicated/VencordInstaller/releases/latest/download/VencordInstaller.exe", ".exe", "VenCord")
        elif achooser(choose, "t4"): dl(3, "https://github.com/BetterDiscord/Installer/releases/latest/download/BetterDiscord-Windows.exe", "BetterDiscord.exe", "BetterDiscord")

        # =============< QOL
        elif achooser(choose, "n"): p1()
        elif achooser(choose, "b"): p2()
        else: runqol(3, choose)

# Basically a main function
cls()
printer.lprint("Starting...")
# Runs EULA check before prep to prevent issues.
if isfile("EULA.XTB") == False:
    eula()
prep()

# Set vars pre startup
printer.lprint("Running Pre-Startup tasks...")

# Updater
pre = ""
version = "2.1"
if pre == "": pre = "         "
# Sets `pre` to this long space to prevent some sort of bugs
# Can't be a defined function
printer.lprint("Checking updates...")
# Check for internet connection BEFORE trying to update the program.
# This should fix some issues with the updater.

isdev = False

if ping("github.com") == None or False:
    # No internet access, the program will not crash.
    Errorhd = color("NoNet    ", 2)

# Checks for the `noupdates` file 
if isfile("noupdates.xtb") == True:
    printer.lprint("NoUpdates Detected, not checking for updates.")
    Errorhd = color("NoUpdates", 3)

# Checks for DEV version  
if isdev == True:
    printer.lprint("DevBuild Detected, not checking for updates.")
    Errorhd = color("DevBuild ", 3)

else:
    # After all the checks
    newver = latest("xemulat/xtoolbox")
    if version == str(newver):
        Errorhd = color("UpToDate ", 1)

    elif str(newver) > version:
        # Triggers the update after outdated version is detected
        Errorhd = color("Outdated ", 2)
        update()

    else:
        Errorhd = color("DevBuild ", 3)

# Set color vars
printer.lprint("Setting vars...")
xtoolboxvv1asdfghjzz = color("XToolBox v"+version+pre, 2)
# ISSUES FIXED, STOP ASKING
# Un-Fucked, don't touch
try:    ramavailz = SetVars.rama()
except: ramavailz = "error"

try:    cpuavailifffff = SetVars.cpup()
except: cpuavailifffff = "error"

try:    dusagehebeded = SetVars.dusage()
except: dusagehebeded = "error"

try:    qwert = SetVars.qwert() + "   "
except: qwert = "error"

try:    c = SetVars.c()
except: c = "error"
xemulatddddd = color("xemulated#2622", 2)

# Page 1 Vairables
windowsonreinddddd = color("WindowsOnReins  DNGR", 2)
ohdwindowwwwwwwww = color("OHD Windows    DNGR", 2)
posttweaksjfjfjf = color("PostTweaks    DNGR", 2)
malwarebyt = color("Malwarebytes", 1)
quicktwea = color("QuickTweaks", 1)
sweetyli = color("SweetyLite", 1)
neCtrl = color("HoneCtrl", 1)
firef = color("Firefox", 1)
rav = color("Brave", 1)

# Page 2 Vairables
windowssimpli = color("WindowsSimplify", 2)
unetboot = color("UNetBootin", 2)
aero = color("Aero10", 2)
window11 = color("Windows 11", 1)
minttuxe = color("Linux Mint", 1)
rectify = color("Rectify11", 1)
zorino = color("Zorin OS", 1)
atlaso = color("Atlas OS", 1)
ruf = color("Rufus", 1)

# Page 3 Variables
cheatbreake = color("Cheat Breaker", 2)
offici = color("Official", 2)
upl = color("Uplay", 2)
hm = color("HMCL", 2)
prismlaunch = color("PrismLauncher", 1)
lunarclien = color("Lunar Client", 1)
openas = color("OpenAsar", 1)
disco = color("Discord", 1)
feath = color("Feather", 1)
ste = color("Steam", 1)

# Help Page Vars
e = Back.RED+"Red"+Back.RESET
ng = Back.RED+"DNGR"+Back.RESET
ree = Back.GREEN+"Green"+Back.RESET

# QuickTweaks Page Vars
LimitQ = color("LimitQoS", 2)
optimizess = color("Optimize SSD", 2)
AntiTrackTi = color("AntiTrackTime", 1)

# Run normal UI (Page 1)
printer.lprint("Starting...")
printer.lprint("Loaded in " + str(str(default_timer() - start).split(".")[0]) + "s")
sleep(0.55)
p1()
