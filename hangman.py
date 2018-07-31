# Have a word/ phrase
phrase = "girls who code"

# keep track of users guesses
guessed_letters = []
game_over = False
# Keep track of bad letters
bad = []
# keep track of good letters
good = []

# allow user to give input to computer
display = ""
for letter in phrase:
        if letter in guessed_letters:
                display += letter
        elif letter == " ":
            display += " "
# Tell the user if the get the right letter
        else:
            display += "_ "
print(display)


guess = input("Enter a letter!: ")
total_underscores = 0
while game_over != True:

    if guess in phrase:
        print("You got a letter: {}".format(guess))

    else:
        print("{} is not in the phrase".format(guess))

    guessed_letters.append(guess)

    display = ""
    for letter in phrase:
            if letter in guessed_letters:
                    display += letter
            elif letter == " ":
                display += " "
    # Tell the user if the get the right letter
            else:
                display += "_ "
    print(display)

    total_underscores += 1
    if total_underscores == 0:
        game_over = True
    else:
        game_over = False


print("END OF GAME")
    # Tell the user if they get the wrong letter
     # Add the bad letter to the bad letter list

# end the game if the user gets all the right letters in our word/ phrase
