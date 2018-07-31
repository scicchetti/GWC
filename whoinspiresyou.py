number = 15
tries = 0

guess = int(input("what number is it?"))
while tries < 3 and number !=guess:
    tries+= 1
    if number > guess:
        guess = int(input("guess higher"))
    else:
        guess = int(input("guess lower"))
print("The number is {}".format(number))
