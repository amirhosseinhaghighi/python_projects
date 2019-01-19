
import random
#from  random import randint

response = input("\n\nHow many characters?\n>>")
length = int(response)
# while True:
if int(response) <= 8:
    print("Please Enter higher than 8 character!!")

else:

    for i in range(10):
        i += 1
        password=''
        for i in range(length):
            char = chr(random.randrange(33,127))
            password += char
        print(password)