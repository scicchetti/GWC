import random
def evenorodd():
    computer_value = random.randint(1,10)
    print("{}".format(computer_value))
    user_input = input("Is this number even or odd? \n")
    if (computer_value % 2 == 0) and (user_input == "even"):
        print("You did it!")
    elif (computer_value % 2 == 0) and (user_input == "odd"):
        print("You're wrong!")
    elif (computer_value % 2 != 0) and (user_input == "odd"):
        print("You did it!")
    elif (computer_value % 2 != 0) and (user_input == "even"):
        print("You're wrong!")

evenorodd()
