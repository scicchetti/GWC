#imports the ability to get a random number (we will learn more about this later!)
from random import *

aList = ["Lisette", "Marty", "Zoe", "Hailey", "Han", "Grace", "Khatu", "Sydney", "Emilye", "Annamarie", "Adriana", "Esther", "Aspen", "Isabel", "Kayla", "Ashely", "Arielle", "Marla"]


#Generates a random integer.
response = input("Would you like a fun name?(Y/N)")
while response !="N":
    if response == "Y":
        aRandomIndex = randint(0, len(aList)-1)
        print(aList[aRandomIndex])
    else:
        print("{} Is an invalid input".format(response))
    response = input("Would you like a fun name?(Y/N)")
