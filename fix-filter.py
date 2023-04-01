import random
import time
import os
from os import system
from time import sleep
import sys
import datetime
import requests
system("clear")
os.system("")
class color:
    green = "\033[32m"
    red = "\033[31m"
    blue = "\033[36m"
    pink = "\033[35m"
    yellow = "\033[93m"
    darkblue = "\033[34m"
    white = "\033[00m"
    mark = '\x1b[38;5;4m'
    mark1 = '\x1b[48;5;15m'
    mark2 = '\x1b[0m'
print(color.mark+f"INSTALLING",end='')
sleep(1)
print(color.green+f".",end='',flush=True)
sleep(1)
print(color.green+f".",end='',flush=True)
sleep(1)
print(color.green+f".",end='',flush=True)
sleep(1)
print(f"\033[34m")
banner = (f"""
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⠃⠀⠀⠀⠀⢀⠀⣴⣿⣿⠇⠀⠀⠀⠀⠀⠀⣴⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⡇⠀⠀⢀⡰⣡⣾⣿⣿⡟⠀⠀⠀⠀⠀⢀⣴⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⡁⠀⡠⢋⣼⣿⣿⣿⢸⠁⠀⠀⠀⠀⣠⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⡿⡄⢈⣴⣿⣿⣿⣿⣽⡏⠀⠀⠀⢀⣾⣿⣿⢿⡇⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⠃
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣠⣿⣿⣿⣿⣿⣿⣿⡇⠀⢀⣠⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⠇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢠⠀⣠⣼⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⣠⣼⣿⣿⠃⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣸⣼⣿⣿⣿⣿⣿⣿⡟⡇⠀⠀⠀⣠⣾⣿⣿⡿⠃⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣬⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢠⠃⢀⣠⣾⣿⣿⣿⡿⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣰⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⡏⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⡿⣟⠋⠀⠈⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣟⡿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣾⣿⣿⣿⣿⡿⡿⢿⡽⠁⠀⠀⠀⠀⠀⠀⠉⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⣿⣿⣿⣿⣿⣿⣧⣾⠂⢵⡆⠀⠀⠀⠤⠀⠀⠀⠀⠀⠀⠈⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣟⣞⡆⣾⠀⢀⣀⣤⣶⣦⣤⣄⣀⠠⡀⠀⠀⠀⠊⠙⠻⢿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢐⣿⣿⣿⣿⣿⣿⣿⣾⣾⣾⣿⠋⣠⣿⣿⣿⣿⣿⣿⣿⣿⢷⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣯⢹⠙⡏⢿⠁⣈⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠀⣠⠶⢓⣠⣄⠀⠠⣹⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣼⢠⠇⠀⡀⠻⣿⣿⣿⣿⣿⣿⣿⣿⠃⢀⠾⣫⣾⣿⣿⣿⣿⢰⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣼⣿⣿⣿⣿⣿⣿⣿⣿⠃⡿⣷⣴⣌⠀⠈⠙⢿⣿⣿⣿⡿⠋⢀⣇⢧⢹⣿⣿⣿⣿⢿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣏⡏⢯⣿⣻⣷⣾⣯⠦⠄⠀⠈⠉⣁⣠⣴⣾⣿⣾⢽⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠟⣿⣿⣿⣿⣿⡛⣿⣧⡄⢰⣾⣿⣿⣿⣿⣷⠞⠛⠻⠟⣷⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣸⣿⣿⣿⣛⣿⢦⣝⠃⠈⠝⠟⢋⡉⢺⡿⠏⠹⣷⣶⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⡌⠻⣯⣿⣿⣻⢦⣞⡿⣦⣤⢀⢻⢋⣴⡚⠋⣴⣾⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣆⠙⡻⡿⣷⣿⡿⣿⡛⣿⢻⣿⣷⣭⣥⣼⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠉⣿⣿⣟⣿⣷⣿⣿⣻⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⢇⠀⠀⠻⠻⣷⣾⣵⣻⣫⣿⣯⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣤⣤⣤⣀⠈⠉⢉⣡⣾⣿⣿⣿⣿⣿⣿⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

█▀▀ █ ▀▄▀   █▀▀ █ █░░ ▀█▀ █▀▀ █▀█   █▀█ █░█ █▄▄ █ █▄▀ ▄▀█
█▀░ █ █░█   █▀░ █ █▄▄ ░█░ ██▄ █▀▄   █▀▄ █▄█ █▄█ █ █░█ █▀█ v1.1
""")
for bnr in banner:
        sys.stdout.write(bnr)
        sys.stdout.flush()
        time.sleep(0.009)
yty=""" 
1.code with id 
2.code not id
 """
for i in yty:
    sleep(0.05)
    print(color.pink+i,end='',flush=True)
get=input(color.pink+'inter  number here>>> ')
if get == 1:
    time.sleep(0.3)
    sistem("clear")
    sistem("python code-fix.py")
    
if get == 2:
    time.sleep(0.3)
    sistem("clear")
    sistem("python code-fix-mini.py")

        
        


coderize = random.choice(repoestsrub)
repoestsrub = ['Rubika.ir/raf-filter','Rubika.ir/fixing-filter','Rubika.ir/Account-liberation','Rubika.ir/rf-fil-rubuk','Rubika.ir/Please-unfilter-this-account','Rubika.ir/plase-fix-filter-this-account','Rubika.ir/fix-fix-fil','Rubika.ir/fixing-fil','Rubika.ir/moslim-account','Rubika.ir/Religious-account','Rubika.ir/Support-fix-filter','Rubika.ir/This-Account-Undertone-Do-Not','Rubika.ir/This-Account-Mistake-Filtered','Rubika.ir/This-Account-must-fix-Filter','Rubika.ir/Bring-this-account-from-the-sanctuary','Rubika.ir/rf-filtering','Rubika.ir/raf-filter','Rubika.ir/fixing-filter','Rubika.ir/Account-liberation','Rubika.ir/rf-fil-rubuk','Rubika.ir/Please-unfilter-this-account','Rubika.ir/plase-fix-filter-this-account','Rubika.ir/fix-fix-fil','Rubika.ir/fixing-fil','Rubika.ir/moslim-account','Rubika.ir/Religious-account','Rubika.ir/Support-fix-filter','Rubika.ir/This-Account-Undertone-Do-Not','Rubika.ir/This-Account-Mistake-Filtered','Rubika.ir/This-Account-must-fix-Filter','Rubika.ir/Bring-this-account-from-the-sanctuary','Rubika.ir/rf-filtering']
