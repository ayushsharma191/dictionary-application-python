#importing the required libraries and modules

import json
from difflib import get_close_matches

#opening the data.json file and loading it to a variable by the name data

data = json.load(open("data.json"))

#definition of the function which determines the response of the computer upon user input

def translate(w):

    #convert the word in all lower case

    w = w.lower()

    #condition 1 : if the word is found as it is as one of the key in data dictionary then return the value of that pair

    if w in data:
        return data[w]

    #Condition 2 : if the value entered is close enough to one of the existing keys in data dictionary then ask the user if they meant that key instead

    elif len(get_close_matches(w, data.keys())) > 0:
        yesno = input("Did you mean %s instead? Type 'y' for Yes or 'n' for No : " % get_close_matches(w, data.keys())[0])
        if yesno == "y" or yesno == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yesno == "n" or yesno == "No":
            return "Meaning of this word dosent exist in this dictionary !!"
        else:
            return "Wrong Input"

    #Condition 3 : if there is no match then tell the user that the word is not in this dictionary

    else:
        return "Meaning of this word dosent exist in this dictionary !!"

#take user input from user and store it in the variable word

word = input("Enter a word to know its meaning : ")

#pass the word argument in translate function and store its return value in variable

output = translate(word)

#print the variable in a good readable format for user 

if type(output) == list:
    count = 1
    for item in output:
        print("Meaning[%s] : %s" % (count, item))
        count = count + 1
else:
    print(output)

