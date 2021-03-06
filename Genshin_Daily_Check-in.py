from pyautogui import *
import pyautogui
import keyboard
from webbrowser import open
import platform
from os import name,system
from requests import get
import sys
from datetime import datetime, timezone
import schedule

version = 1.7

command = "cls"
if os.name != "nt":
    command = "clear"
os.system(command)

def newVersion():
    response = get("https://api.github.com/repos/runningwinterberry/Genshin-Daily-Check-in/releases/latest")
    lv = float(response.json()["tag_name"].replace('v',''))
    if version < lv:
        print("**********************************\n\033[1;33mVersion "+ str(lv) +" Available, Currently Running "+ str(version) +"\n\033[0mWould you like to go to the releases page? \nhttps://github.com/runningwinterberry/Genshin-Daily-Check-in/releases \n**********************************")

newVersion()

print("You \033[91m must \033[0m be logged in and have browser remember you \nso I can go directly to the daily check-in screen.\nAlso, please insure you browser opens in full screen.")

print("\n\nPaste the url of the daily login screen and click enter OR click enter to use defult")
url = input()
if url == "":
    url = "https://act.hoyolab.com/ys/event/signin-sea-v3/index.html?act_id=e202102251931481&mhy_auth_required=true&mhy_presentation_style=fullscreen&lang=en-us"

print("Please enter RGB value of orange seperated by commas without spaces \nthen click enter OR click enter to use defult (208,100,47)")
a = input()
if a == "":
    a = "208,100,47"
color = tuple(map(int, a.split(',')))

print("Please enter your system of 'Mac', 'Windows', or 'Linux'(case sensitive)\n(for this purpose there is no differnce between Windows and Linux) \nthen click enter OR click enter to use defult (Windows)")
sys = input()
if sys == "":
    sys = "Windows"
if sys != "Windows" and sys != "Mac" and sys != "Linux":
    print("\033[91munknowen system\033[0m" + " " + sys)
    sleep(2)
    sys.exit()

print("How long shall I wait (in hours) till I collect your daily check-in? \nI will then collect it every 24 hours after")
wait = input()
print("\033[1;32mSetup complete \033[0m")
sleep(2)
if wait != "":
    sleep((float(wait)*60)*60)

def click(x, y):
    pyautogui.moveTo(x, y)
    sleep(0.1)
    pyautogui.click()

def job():
    open(url, new=1)
    sleep(10)
        
    s = pyautogui.screenshot()
    for x in range(s.width):
        for y in range(s.height):
            if s.getpixel((x, y)) == color:
                click(x, y)
                newVersion()
                today = datetime.now().strftime("%m"+"-"+"%d"+"-"+"%Y %H:%M")
                print("\033[0;36mSuccessfully collected rewards for: " + str(today) + "\033[0m" + "\nRewards will be collected again in 24 hours")
                sleep(10)
                if sys == "Mac":
                    pyautogui.hotkey('command', 'w')
                else:
                    pyautogui.hotkey('ctrl', 'w')
                break
        else:
            continue
        break
    else:
        os.system(command)
        print("\033[91mColor not found!\033[0m")
        newVersion()

job()
schedule.every(1).days.do(job)
while 1:
    schedule.run_pending()
    sleep(1)
        








        
