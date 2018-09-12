from random import randint
import sys
words = ["placeholder", "death", "destruction", "cube"]
displayString = ""

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
        sys.stdout.write(letter+" ")
        sys.stdout.flush()
    print("")
    x = input("input a letter: ").lower()
    i = 0
    i = key.find(x)
    if (i==-1):
        return failCount()
    ansCopy = key
    while(i!=-1):
        displayString = strReplace(displayString, i, key[i])
        i = ansCopy.find(x)
        ansCopy = ansCopy[:i]
    return checker(key)

def failCount():
    fail = 0
    fail+=1
    if(fail==7):
        return "YOU FAILED"
    checker(key)

key = stringChooser()
displayString = str("_"*len(key))
checker(key)
