# --- Define your functions below! ---
def intro():
    print("Welcome to the chatbot!")
def greeting():
    print("let's have a deep conversation....")
def dating():
    print("I am 105 years old. I am a fashion nova instagram model in my free time")
    print("During the day, I am a cereal killer. At night I am Batman")
    rep = input("""
Soooooo, come here often?
    (~~~~~~~~~~~~~~~)           (~~~~~~~~~~~~~~~) \n
     \   \~~~~~~~/ /             \   \~~~~~~~/ / \n
       \  \    / /                 \  \    / / \n
         \  \/ /__===_____________==_\  \/ / \n
        __ --  __----__          __-----__  --__ \n
     _-~     /'         ~\      /'         ~\    ~-_ \n
   /~       |____________|    |_____________|       ~\ \n
  |         |  O         |  /\| O           |         | \n
  |          \ _       ./ /    \.          /          | \n
  |             ~~~~~~ /        \~~~~~~~'           | \n
   \                  /____________\                 / \n
    ~--__         ___(              )___       ___--~ \n
         ~~~~--~~~    \            /    ~~~--~~____------ \n
 ------____/__   ~~     \        /    __---~~ ~\ \n
          |   ~~~~~       \    /        __----~|~~~~~~ \n
      -----\------------    \/      _________  /\n
            \                |                /\n
              \   _______   / \     ~~----__/____\n
____-----~~~~~~~\~        /     \         /      ~~~~~---\n
                 ~-____-~        ~-____-~\n
                     \              /\n
                       \          /\n
                        ~-______-~\n
    """)
def is_valid_input(response, all_valid_inputs):
    if response in all_valid_inputs:
        return True
    else:
        return False
print("I was talking with your cousin last night..")
# --- Put your main program below! ---
def main():
  valid_input = ["Hi!", 'Hello ;)', 'love me', 'come here often?','I need a partner in crime', 'draw me', 'art', 'draw please']

  intro()
  while True:
    answer = input("(What will you say?) ")
    if is_valid_input(answer, valid_input):
        if answer == "Hi!":
            greeting()
        elif answer in ['Hello ;)', 'love me', 'come here often?','I need a partner in crime']:
            dating()
        elif answer in ['draw me', 'art', 'draw please']:
            dating()
    else:
        print("Say 'Hi!' I dont understand anything else")
        print("These are the inputs I understand: ")
        for vi in valid_input:
            print(vi)


# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
