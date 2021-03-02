import json
from difflib import get_close_matches

# read data from json file/ save into dictionary
data = json.load(open("data.json"))


# get input from user
def get_Input():
    return input('<<<<<< Enter a Word >>>>>>\n').lower()


# search the dictionary to find the translation for the given word
def translate():
    # get word as input
    word = get_Input()
    # check if word is in the dictionary
    if word in data:
        return data[word]
    # check if user enter an incorrect word/get_close_matches method gives a list of similar words
    elif len(get_close_matches(word, data.keys())) > 0:
        # most match word is in index 0
        correct_word = get_close_matches(word, data.keys())[0]
        print("Did you mean " + correct_word + "???" + "\nyes/no")
        user_response = input().lower()
        # check the dictionary again (check corrected word)
        if user_response == 'yes':
            return data[correct_word]
        else:
            return "I did not understand what you mean..."
    else:
        return "Ooops! this word is not defined..."


print("WELCOME TO MY ONLINE TRANSLATOR")
while True:
    print(translate())
    choice = input('\nDo you want to try again?\nIf yes, press "Y"\nIf no, press "N"\n').lower()
    if choice == 'y':
        continue
    print("HAVE A GOOD DAY!")
    break

