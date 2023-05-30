# Dice Roll Simulator By Samuel Wolde

import random

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

    # Get Menu Selection from User
    selection = input("Select an option (1-5): ")

    # Take Action Based on Menu Selection 
    if selection == "1":
        rand_num1 = random.randrange(1, 7)
        rand_num2 = random.randrange(1, 7)
        sum = rand_num1 + rand_num2
        print(str(rand_num1) + "," + str(rand_num2) + " (sum: " + str(sum) + ")")
    elif selection == "2":
        loop2 = True
        rolls = 0
        while loop2:
            rolls += 1
            rand_num1 = random.randrange(1, 7)
            rand_num2 = random.randrange(1, 7)
            sum = rand_num1 + rand_num2
            print(str(rand_num1) + "," + str(rand_num2) + " (sum: " + str(sum) + ")")
            if rolls == 5:
                loop2 = False

    elif selection == "3":
        rolls = 0
        loop3 = True
        rolls_requested = input("\nHow many rolls would you like? ")
        while loop3:
            rand_num1 = random.randrange(1, 7)
            rand_num2 = random.randrange(1, 7)
            sum = rand_num1 + rand_num2
            rolls+= 1
            print(str(rand_num1) + "," + str(rand_num2) + " (sum: " + str(sum) + ")")
            if rolls == int(rolls_requested):
                loop3 = False
    elif selection == "4":
        rolls = 0
        loop4 = True
        while loop4:
            rand_num1 = random.randrange(1, 7)
            rand_num2 = random.randrange(1, 7)
            sum = rand_num1 + rand_num2
            rolls += 1
            print(str(rand_num1) + "," + str(rand_num2) + " (sum: " + str(sum) + ")")
            if rand_num1 == rand_num2:
                print("\nSNAKE EYES! It took " + str(rolls) + " rolls to get snake eyes.")
                loop4 = False
    elif selection == "5":
        print("\nEXIT")
        loop = False