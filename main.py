# Dice Roll Simulator By Samuel Wolde


#Main Program Loop
loop = True
while loop:
    #Print Main Menu 
    print("\nDICE ROLL SIMULATOR MENU")
    print("1: Roll Dice Once")
    print("2: Roll Dice 5 Times")
    print("3: Roll Dice ‘n’ Times")
    print("4: Roll Dice until Snake Eyes")
    print("5: Exit")

    #Choose a random number 1-6
    import random
    rand_num1 = random.randrange(1, 7)
    rand_num2 = random.randrange(1, 7)
    sum = rand_num1 + rand_num2

    # Get Menu Selection from User
    selection = input("Select an option (1-5): ")

    # Take Action Based on Menu Selection 
    if selection == "1":
        print(str(rand_num1) + "," + str(rand_num2) + " (sum: " + str(sum) + ")")
    elif selection == "2":
        loop = True
        rolls = 0
        while loop:
            rolls+=1
            print(str(rand_num1) + "," + str(rand_num2) + " (sum: " + str(sum) + ")")
            if rolls == 5:
                loop = False

    elif selection == "3":
        print("\nOption 3")
    elif selection == "4":
        print("\noption 4")
    elif selection == "5":
        print("\nEXIT")
        loop = False