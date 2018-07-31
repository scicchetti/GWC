data2 = [{'Whats your name?': 'Sam', 'How old are you?': '16', 'Whens your birthday?': 'October 1st 2001', 'Any Hobbies?': 'Netflix'}]
f = open("data.json", "r+")
old_data = json.load(f)
old_data.extend(data2)
f.write(json.dumps(old_data))
f.close()
