import json
from difflib import get_close_matches #module which helps to check for missmatches in words 
data = json.load(open("data.json"))#loading data 


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        Yn = input("did you mean %s insted? eneter Y if yes and N for NO " %
                   get_close_matches(word, data.keys())[0])
        if Yn == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif Yn == "N":
            return "word does not avail please check "
        else:
            return "sorry what?"

    else:
        return "word does not exist please check and input correct words"

#printing output and user inputs 
word = input("enter word:")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)

else:
    print(output)
