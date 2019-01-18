
import os
import random
from platform import system as system_name # Returns the system/OS name
from os import system as system_call       # Execute a shell command

from datetime import datetime


# O   ۰
# L ; I   ۱
# Z   ۲
# E   ۳
# A   ۴
# S   ۵
# G   ۶
# T   ۷
# B   ۸
# L ; I   |
# at   @
# S   $
# H   )(
# H   }{
# N   / \ /
# W   \ / \ /
# M   / \ / \
# P ; D   | >
# K   | <
# F   P H
# S   Z





def  clear_screen():

        """
        Clears the terminal screen.
        """

        # Clear command as function of OS
        command = "cls" if system_name().lower()=="windows" else "clear"

         # Action
        system_call(command)



clear_screen()

#current_month = datetime.now().strftime('%m') # 02 //This is 0 padded

# current_month_text = datetime.now().strftime('%h') # Feb
# current_month_text = datetime.now().strftime('%B') # February
# current_day = datetime.now().strftime('%d')   # 23 //This is also padded
# current_day_text = datetime.now().strftime('%a')  # Fri
# current_day_full_text = datetime.now().strftime('%A')  # Friday

# current_weekday_day_of_today = datetime.now().strftime('%w') #5  Where 0 is Sunday and 6 is Saturday.

#current_year_full = datetime.now().strftime('%Y')  # 2018
# current_year_short = datetime.now().strftime('%y')  # 18 without century

# current_second= datetime.now().strftime('%S') #53
# current_minute = datetime.now().strftime('%M') #38 
# current_hour = datetime.now().strftime('%H') #16 like 4pm
# current_hour = datetime.now().strftime('%I') # 04 pm

# current_hour_am_pm = datetime.now().strftime('%p') # 4 pm

# current_microseconds = datetime.now().strftime('%f') # 623596 Rarely we need.

# current_timzone = datetime.now().strftime('%Z') # UTC, EST, CST etc. (empty string if the object is naive).




# currentdate = current_year_full + current_month

# password = input("Please Enter Your Username:\n>>").upper()
# password = "["+ password + currentdate + "@123" + "]"

# print(password)



characters = ["!","@","#","$","%","^","&","*","_","+"]
allphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
         "n","o","p","q","r","s","t","u","v","w","x","y","z"]
allphabet_map = ["@","8","c","|>","3","ph","6",")(","1","j","|<","1","m",
         "/\/","0","|>","q","r","$","7","u","v","w","x","y","2"]

current_month = datetime.now().strftime('%m') # 02 //This is 0 padded
current_year_full = datetime.now().strftime('%Y')  # 2018
currentdate = current_year_full + current_month

password = str(input("Please Enter Your Username:\n>>"))
passwdFinal = []


for i in range(len(password)):
    if password[i] in  allphabet:
        #print(allphabet.index(password[i]))
        #print(allphabet_map[allphabet.index(password[i])])
        passwdFinal.append(allphabet_map[allphabet.index(password[i])])
passwdFinal = "[" + "".join(passwdFinal) + currentdate + "@123" + "]"
print(passwdFinal)
#print("".join(passwdFinal))

    
    #password = "["+ password + currentdate + "@123" + "]"