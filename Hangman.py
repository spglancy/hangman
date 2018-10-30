from random import randint
import requests
import sys
words = ["placeholder"]
tried = []
displayString = ""

def getWord():
    word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"

    response = requests.get(word_site)
    WORDS = response.content.splitlines()

    word = (WORDS[randint(0,len(WORDS)-1)])
    word = str(word)
    return(word[2:-1].lower())
# credit to Ki for this ^^^

def stringChooser():
    answerInternal =  words[randint(0,len(words)-1)]
    mainString = str("_"*len(answerInternal))
    return (answerInternal)

def strReplace(str,index,char):
    str = list(str)
    str[index] = char
    return "".join(str)

def checker(key):
    global displayString
    for letter in displayString:
        sys.stdout.write(letter + " ")
        sys.stdout.flush()
    print("")
    x = input("input a letter: ").lower()
    if (x == key):
        print(key)
        print("You Win")
        sys.exit()
    elif (len(x) > 1):
        print("Invalid input, please try again")
        return checker(key)
    if (key.find(x) == -1):
        if (x not in tried):
            tried.append(x)
            print(tried)
        else:
            print("You already tried that letter!")
        if(len(tried) == 7):
            print("You Lose")
            print("The string was: " + key)
            sys.exit()
    for i in range(len(displayString)):
        if (key[i] == x):
            displayString = strReplace(displayString, i, key[i])
    if("_" not in displayString):
        print(key)
        print("You Win")
        sys.exit()
    return checker(key)

key = getWord()
displayString = str("_"*len(key))
checker(key)
