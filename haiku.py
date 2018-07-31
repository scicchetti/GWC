import random

alist = ["Look alive.", "They're alive.", "Use them all", "I'm alone.","Come along."]
bList = ["I'm an addict.", "I'm adopted.", "You're an adult.", "Take my advice.", "Please look again."]
clist = ["We've arrived.", "Is this art?","I won't ask.", "Step aside.", "They'll attack.", "I'm awake.", "It's awful.", "You came back."]

alist_index = random.randint(0, len(alist)-1)
blist_index = random.randint(0, len(blist)-1)
clist_index = random.randint(0, len(clist)-1)

print("{}\n {}\n {}")
