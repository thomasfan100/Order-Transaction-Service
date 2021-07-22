import sys

def mainMenu():
    exit = True
    while exit: #will exit when exit is False
        
        menu = {
            '1':'Administrator Login',
            '2':'Place Order',
            '3':'Logout',
            }
        print("Choose Option from the Main Menu below")
        print("---------------------------------------")
        for x in menu:
            print(f"{x}.{menu[x]}")
        
        input_option = input("Choose option:")
        if input_option == '1': #Administrator login
            adminLogin()
        elif input_option == '2': #Place order
            placeOrder()
        elif input_option == '3': #Logout
            print("Have a nice day !")
            exit = False 
            
        else:
            print("ERROR: You must enter a 1, 2, or 3")
        
def adminLogin():
    print("Admin Login")
    print("---------------------------------------")

    found = False #if the user and pass word are found, set to true
    #opens credentials to see valid admin login and passwords
    again = True
    while again:
        username = input("Enter Username:")
        password = input("Enter Password:")
        f = open("credentials.txt","r")
        for line in f:
            #split the list by comma
            the_line = line.rstrip() #removes the \n at end of some lines
            comma_list = the_line.split(", ") #comma_list is a list var
            if comma_list[0] == username and comma_list[1] == password:
                found = True
        if found == False:
            print("Invalid username/password combination")
            print("Try again...")
        else: #valid combination
            again = False #breaks out of the loop
        f.close()
    #admin has logged in now
    f = open("order_log.txt","r")
    total = 0.0 
    for line in f:
        the_line = line.rstrip()
        comma_list = the_line.split(", ")
        total += float(comma_list[2]) * float(comma_list[3])
        print(line)
    f.close()
    print(f"${total}")
    print("You are logged out now!")


def placeOrder():
    print("Choose an Item from the menu below")
    print("---------------------------------------")
    menu_items = [] #this is a list of all menu items
    purchased_items = [] #this is a list of items customer purchased
    
    f = open("order_log.txt","r")
    total = 0.0
    #printing out all menu items and price
    for line in f:
        the_line = line.rstrip()
        comma_list = the_line.split(", ")
        menu_items.append(comma_list)
        print(f"{comma_list[0]}. {comma_list[1]}..... ${comma_list[2]}")
    f.close()

    end = True
    while end:
        #get user input on what option
        valid = True
        choice = -1
        while valid: #break out of loop when a valid number is found
            choice = input("Choose option:")
            if choice.isdigit():
                if int(choice) > 0 and int(choice) < len(menu_items)+1:
                    valid = False
                else:
                    print("ERROR You must enter a number between 1 and {len(menu_items)}")
            else:
                print("ERROR You must enter a number between 1 and {len(menu_items)}")

        #update the price in the text file
        how_many = int(input("How many would you like?"))
        choice = int(choice) - 1 #so this is where choice is in the menu_items list
        new_quantity = int(menu_items[choice][3]) + how_many
        menu_items[choice] = [menu_items[choice][0],
                              menu_items[choice][1],
                              menu_items[choice][2],
                              str(new_quantity)] #this is just a list
        total = float(menu_items[choice][2]) * how_many
        purchased = [menu_items[choice][1],how_many,menu_items[choice][2],str(total)]
        purchased_items.append(purchased) #add item you just bought to the list
        continue_yn = input("Press y to continue shopping. Press any other key to go back to main menu?")
        if continue_yn != "y":
            end = False #abort this loop


        f = open("order_log.txt","w")
        for x in menu_items:
            f.write(f"{x[0]}, {x[1]}, {x[2]}, {x[3]}\n")
        f.close()
        
    print("* Order Totals *")
    for x in purchased_items: #print all items purchased in nice format
        print(f"{x[0]}: {x[1]} @ ${x[2]} = {x[3]}")

    #calculate total price
    total = 0.0
    for x in purchased_items:
        total += float(x[3])
    print(f"Total: ${total}")
    print("Your order has been placed successfully! Have a nice day!")
        

mainMenu()
