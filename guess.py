number=45

guess = int(input("what number is it?"))
for tries in range(3):
    if guess in range(46, 100):
        guess = int(input("lower"))
    if guess in range (0, 44):
        guess = int(input("higher"))
    if guess == number:
        print("great job you got it!")
        break
