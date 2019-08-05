import random

def randWords(fileName):
    f = open(fileName, "r")
    fl = []

    for x in f:
        fl.append(x)

    return fl[random.randint(0,999)]
