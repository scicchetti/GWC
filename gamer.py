########### Starter code for Rock Paper Scissors ############

# TODO: Import the module (aka library) random
import random
# TODO: Create a list of possible moves in rock paper scissors
gestures = ["rock", "paper", "scissors"]

# Allow the computer to make a random selection on the move
computer = random.choice(gestures)

# TODO: Take in user input for rock, paper, or scissors
# BE SURE TO PROCESS INPUT (valid inputs allowed ONLY)
human = input("Choose rock, paper or scissors.")


# Show the human player what the computer decided on
print("I choose {}".format(computer.upper()))

# Determine who wins
# TODO: when would there be a tie?
if computer == "rock" and human == "rock":
    print ("It's a tie!")
elif computer == "paper" and human == "paper":
    print ("It's a tie!")
elif computer == "scissors" and human == "scissors":
    print ("It's a tie!")

# TODO: when does the computer win?
if computer == "rock" and human == "scissors":
    print ("I win!!")
elif computer == "paper" and human == "rock":
    print ("I win!!")
elif computer == "scissors" and human == "paper":
    print ("I win!!")

# TODO: when does the human win?
if computer == "rock" and human == "paper":
    print ("You win!!")
elif computer == "paper" and human == "scissors":
    print ("You win!!")
elif computer == "scissors" and human == "rock":
    print ("You win!!")


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
