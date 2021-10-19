#Grocery list
#user will be able to add items to a grocery list and when they are done
#that list will be printed

#create list
grocery_list = []
choices = ["yes" , "no"]

#ask user to enter intial item to list
item = input("What would you like to add to your grocery list? ")

#add item to list
grocery_list.append(item)

while True:
    add_to_list = input("\nWould you like to add another item? Yes or No: ").lower()
    
    #check if they entered yes or no
    if add_to_list not in choices:
        print("Please enter a valid answer")
        continue
    else:
        if add_to_list == "no":
            print("\nHere is your current list: ")
            print(*grocery_list, sep="\n")
            exit()
        else:
            item = input("What else would you like to add to your grocery list? ")
            grocery_list.append(item)
            #after user enters item, loop will restart
            continue
