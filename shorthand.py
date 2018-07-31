def translate_shorthand(dictionary):
    for key, value in sorted(dictionary.items()):

phrases = {
"ttyl" : "talk to you later"
"gr8" : "great"
"gr9" : "even better then gr8 cuz its gr9"
"fr" : "for real"
"gtg" : "got to go"
}

translate_shorthand(phrases)

story = """
Stacy was texting . She said fr del taco is gr8 but like taco bell is gr9 . Anyways I gtg ttyl .
"""

story_list = story.split()

new_story_list = []

for word in story_list:
    if word in phrases.keys():
        new_story_list.append(phrases[word])

    else:
        new_story_list.append(word)
print(new_story_list)
print(" ".join(new_story_list))
