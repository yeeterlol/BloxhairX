import shutil
from os import *
from os.path import * 
from urllib.request import urlopen, urlretrieve
from json import load

def get_latest_version():
    ver = load(urlopen("https://clientsettingscdn.roblox.com/v2/client-version/WindowsPlayer/channel/zflag"))["clientVersionUpload"]
    return ver

# Variables
img = "crosshair.png"
ver = get_latest_version()
filepath = getenv("LOCALAPPDATA")+"\\Roblox\\Versions\\"

def main():
    global img, filepath, crosshairpath, texturespath, ver
    print("Bloxhair X")
    # Credits to https://github.com/lolmanurfunny/Roblox-Launcher-minus-the-app fir the code
    # Most of the code is skidded from them since I'm a fucking lazy ass retard
    # If lolmanurfunny wants code to be removed, I'll rewrite my own shitty solution 

    if exists(filepath):
        filepath+=ver
        crosshairpath = filepath+"\\content\\textures\\Cursors\\KeyboardMouse"
        texturespath = filepath+"\\content\\textures"
        if exists(filepath):
            shutil.copy("crosshair.png", f"{crosshairpath}\\ArrowCursor.png")
            shutil.copy("crosshair.png", f"{crosshairpath}\\ArrowFarCursor.png")
            shutil.copy("crosshair.png", f"{crosshairpath}\\IBeamCursor.png")
            shutil.copy("crosshair.png", f"{texturespath}\\MouseLockedCursor.png")
            shutil.copy("crosshair.png", f"{texturespath}\\Cursors\\CrossMouseIcon.png")
            print("[!] Crosshair applied, restart your client!")
        else:
            print("[!] Couldn't find client!")
            exit(1)
    else:
        print("[!] Couldn't find versions folder")
        exit(1)


    print("[!] Applying Crosshairs")

if __name__ == "__main__":
    main()