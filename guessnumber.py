import random
Gole = random.randint(1,99)
tries = 7
i=0
print(Gole)

while   i < tries:
    Guess = input("Enter an integer from 1 to 99:\n> ")
    if Guess.isnumeric():
        Guess=int(Guess)
    else:
        print("Please enter Valid NUMBER !!")
        continue
    i += 1
    
    if ( Guess < Gole ):
        print("Guess {} is low than < mynumber , number of guess left is ".format(Guess) + str( tries - i ))    
    elif ( Guess > Gole ):
        print("Guess {} is higher than > mynumber , number of guess left is ".format(Guess) + str( tries - i ))
       
    else:
        break

if Gole == Guess :
    print("You Guessed it!!!")
        
else:
    print("You Lose!!!")




