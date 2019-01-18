
shopping_list =  []


print("what should we use at the store?\n"
    "Enter 'DONE' to stop adding items\n"
    "Enter 'HELP' to show all instructions in our app\n"
    "Enter 'SHOW' to show all items in our shopping list\n"
    "Enter 'REMOVE' to remove item in our shopping list\n")

while True:
    ans = input("> ").upper()

    if ans == "DONE":
        break

    elif ans == "HELP":
        print("what should we use at the store?\n"
        "Enter 'DONE' to stop adding items\n"
        "Enter 'HELP' to show all instructions in our app\n"
        "Enter 'SHOW' to show all items in our shopping list\n"
        "Enter 'REMOVE' to remove item in our shopping list\n")
    elif ans == '':
        continue
    elif ans == "SHOW":
       print(shopping_list)
    elif ans == 'REMOVE':
        ans=input("Enter Your remove Item --> ").upper()
        if ans in shopping_list:
            shopping_list.remove(ans)
            print("\033[1;31;40m{}\033[m removed from  list".format(ans))
        else:
            print("{} not exist in list".format(ans))
    else:
        if not ans in shopping_list:
            shopping_list.append(ans)
            print("Added {0} to list now. the list now has {1}  items".format(ans,len(shopping_list)))
        else:
            print("{} pre exist in shopping list".format(ans))
