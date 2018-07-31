import json
import os
# datas = [{'Whats your name?': 'Sam', 'How old are you?': 16, 'Whens your birthday?': 'October 1st 2001', 'Any Hobbies?': 'Netflix'}]

# f = open("data.json", "w")
#
# json_obj = json.dumps(datas)
#
# f.write(json_obj)
#
# f.close()

cont = True
question = ['Whats your name?', 'How old are you?', 'Whens your birthday?', 'Any Hobbies?', 'Favorite food?', 'Favorite movie?']
data = []
while cont:
    response = {}
    for q in question:
        response[q] = input(q)
    print(response)
    data.append(response)
    cont = input('Would you like to continue? Y/N')
    if cont == "Y":
        cont = True
    else:
        cont = False
print(data)

if os.path.isfile("data.json"):
    file = open("data.json", "r+")
    old_data = json.load(file)
    old_data.extend(data)
    file.write(json.dumps(old_data))
    file.close()

else:
    file = open("data.json", "w")
    file.write(json.dumps(data))
    file.close()

file = open("list_of_responses.json", "r")
a = "".join(file.readlines())
new_data = ",".join(a.split(']['))
file.close()

file = open("list_of_responses.json", "w")
file.write(json.dumps(new_data))
file.close()
