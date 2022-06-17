from pyautogui import *
import pyautogui
#import time
import keyboard
from webbrowser import open
import platform
from os import name,system
import ctypes
from requests import get

hidden = bool()
version = 1.3

command = "cls"
if os.name != "nt":
    command = "clear"
os.system(command)

def newVersion():
    response = get("https://api.github.com/repos/runningwinterberry/Genshin-Daily-Check-in/releases/latest")
    lv = float(response.json()["tag_name"].replace('v',''))
    if version < lv:
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 5)
        hidden = False
        print("**********************************\nVersion "+ str(lv) +" Available, Currently Running "+ str(version) +"\nWould you like to go to the releases page? \nhttps://github.com/runningwinterberry/Genshin-Daily-Check-in/releases \n**********************************")

newVersion()
    
print("You \033[91m must \033[0m be logged in and have browser remember you \nso I can go directly to the daily check-in screen.\nAlso, please insure you browser opens in full screen.")

print("\n\nPaste the url of the daily login screen and click enter")
url = input()
if url == "":
    url = "https://act.hoyolab.com/ys/event/signin-sea-v3/index.html?act_id=e202102251931481&mhy_auth_required=true&mhy_presentation_style=fullscreen&lang=en-us&bbs_theme=dark&bbs_theme_device=1"

print("Please enter RGB value of orange seperated by commas without spaces \nthen click enter OR click enter to use defult (208,100,47)")
a = input()
if a == "":
    a = "208,100,47"
color = tuple(map(int, a.split(',')))

print("Please enter your system of 'Mac', 'Windows', or 'Linux'\n(for this purpose there is no differnce between Windows and Linux) \nthen click enter OR click enter to use defult (Windows)")
sys = input()
if sys == "":
    sys = "Windows"

print("How long shall I wait (in seconds) till I collect your daily check-in? \nI will then collect it every 24 hours after")
wait = input()
if wait == "":
    wait = "2"
print("\033[1;32mSetup complete \033[0m")
sleep(2)
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
hidden = True
sleep(int(wait)-2)

def click(x, y):
    pyautogui.moveTo(x, y)
    sleep(0.1)
    pyautogui.click()

while 1:
    open(url, new=1)
    sleep(10)
        
    s = pyautogui.screenshot()
    for x in range(s.width):
        for y in range(s.height):
            if s.getpixel((x, y)) == color:
                ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
                hidden = True
                click(x, y)
                sleep(10)
                newVersion()
                if sys == "Mac":
                    pyautogui.hotkey('command', 'w')
                else:
                    pyautogui.hotkey('ctrl', 'w')
                break
        else:
            continue
        break
    else:
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 5)
        hidden = False
        os.system(command)
        print("\033[91mColor not found!\033[0m")
        newVersion()
    for i in range(1440):
        sleep(60)
        if keyboard.is_pressed('`'):
            if hidden == True:
                ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 5)
                hidden = False
            else:
                ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
                hidden == True
        








        
