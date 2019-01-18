
from  random import randint
import os

from platform import system as system_name # Returns the system/OS name
from os import system as system_call       # Execute a shell command

def  clear_screen():

        """
        Clears the terminal screen.
        """

        # Clear command as function of OS
        command = "cls" if system_name().lower()=="windows" else "clear"

         # Action
        system_call(command)



clear_screen()






#n = input("Enter a number \n>>").isnumeric())
'''
n = int(input("Enter a number \n>>"))

for c in range(n):
    print("")
    for j in range (n):
        #print("_",end="")
        for i in range(n):
            if(i%2 == 0):
                print("|",end='')
                
            else :
                print("_",end='')
                
 '''
answer=int(input("Enetr YOur deminision >>> "))
x=randint(0,answer-1)
y=randint(0,answer-1)


dragon_x=randint(1,answer-1)
dragon_y=randint(1,answer-1)
print(x+1,y+1)
print(dragon_x+1,dragon_y+1)
door_x=randint(0,answer-1)
door_y=randint(0,answer-1)
print(door_x+1,door_y+1)

def showAllowdirectionmessage(x,y):
    if x == 1 and y == 1:
        print("[*]You are currently able to go ['RIGHT','DOWN']")
    elif x == answer and y == 1:
        print("[*]You are currently able to go ['LEFT','DOWN']")
    elif x == 1 and y == answer:
        print("[*]You are currently able to go ['UP','Right']")
    elif x == answer and y == answer:
        print("[*]You are currently able to go ['LEFT','UP']")
    elif x > 1 and y == 1:
        print("[*]You are currently able to go ['LEFT','DOWN','Right']")
    elif x == 1 and y < answer:
        print("[*]You are currently able to go ['Right','UP','Down']")
    elif x > 1 and y == answer:
        print("[*]You are currently able to go ['LEFT','UP','Right']")
    else:
        print("You are currently able to go ['LEFT','RIGHT','UP','DOWN']")

while True:
#     print("You are currently in room{}\
# #You are currently able to go ['LEFT', 'RIGHT', 'UP', 'DOWN']\
# #Type QUIT to stop playing DUNGEON"\
# )

    print("[*]You are currently in room ({},{})".format(x+1,y+1))
    #print("You are currently able to go ['LEFT', 'RIGHT', 'UP', 'DOWN']")
    showAllowdirectionmessage(x+1,y+1)
    print("[*]Please Press u=UP or d=Down or r=Right or l=left")
    print("[*]Type q=QUIT to stop playing DUNGEON")

    for i in range(answer):
        print(' _',end='')
    print('')
    for i in range(answer):
        for j in range(answer+1):
            print('|',end='')
            if i == y and j == x:
                print('X',end='')
            elif not j == answer:
                print('_',end='')    
        print('')
    if x == dragon_x and y == dragon_y:
        print("\n\nYou Lose!!!")
        break

    if x == door_x and y == door_y:
        print("\n\nYou Win!!!")
        break    
    direct=input("Enter Direct >>>").lower()
    clear_screen()
    if direct == 'u':
        if y > 0:
            y -= 1
    elif direct == "d":
        if y < answer-1:
            y += 1
    elif direct == "r":
        if x < answer-1:
            x += 1
    elif direct == "l":
        if x > 0:
            x -= 1
    elif direct == "q":
        break
    else:
        print("\n\nPlease Press u=UP or d=Down or r=Right or l=left!!!\n")






'''
print('\n\n ---'+'---'* 18 + '-- ')
for _ in range (10):
    print('|     ' * 10 + '|')
    print('|  {}  '.format('X') * 10 + '|')
    print()
'''



