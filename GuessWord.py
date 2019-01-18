
import random

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

answerlist = ["world","look","hello","goodbye"]

random.shuffle(answerlist)
#print(answerlist[0])

answer = list(answerlist[0])
#print(answer)

WordshowToUser = []

used = []

WordshowToUser.extend(answer)
used.extend(WordshowToUser)
#print(WordshowToUser)


for i in range(len(WordshowToUser)):
    WordshowToUser[i] = "*"

#print(WordshowToUser)
print(' '.join(WordshowToUser))

count = 0
incorrect = 5

while count < len(answer) and incorrect > 0:
    guess = input("Please guess a letter:")
    guess = guess.lower()
    print(count)

    for i in range(len(answer)):
        if answer[i] == guess  and guess in used:
            WordshowToUser[i] = guess 
            count = count + 1
            used.remove(guess)

    if guess not in WordshowToUser:
        incorrect = incorrect - 1
        print ("sorry,wrong guess.You have ",incorrect, "chance left")


    print("You have guessed ", count ,"correct letters.")
    print("You have",incorrect,"chances left")

    print(' '.join(WordshowToUser))
    print()

if (count == len(answer)):
    print("Well done, you guess the word!")
else:
    print("unfortunatly you ran out of goes")












