# so pretty much what this does is it makes a copy of resume.json
# and then fills it out with random information.
# 
# Name (str), Age (int), Skills [list], Experiences [list], Education [list], Additonal Notes (str)

from inspect import GEN_CLOSED
import random
import shutil
import json

def liMaker(string):
    li = list(string.split(', '))
    return li

def randomId():
    # 2 genders * 3 races = 6 options
    # pick a random number 1-6
    # numbers correlate in this order:
    # White man, Black man, Latino man, White woman, Black woman, Latino Woman
    
    myRand = random.randint(0, 5)
    if (myRand <= 2):
        gender = "Masculine"

    elif (myRand >= 3):
        gender = "Feminine"
        myRand -= 3

    raceIndex = {0: "White", 1:"Black", 2:"Latino"}
    race = raceIndex[myRand]

    return gender+', '+race

def randomName(gender, race):
    # picks a random name based on the race and gender given by
    # randomId()

    myRand = random.randint(0, 4)

    f = open("names.json", "r")
    myJson = json.load(f)
    f.close()

    name = myJson.get(str(gender), {}).get(str(race), {})[myRand]

    print(name)
    return name

def fillName(name):
    # makes a copy of resume.json (the template), pastes values into it on
    # output.json

    # open template file
    f = open("resume.json", "r")
    myJson = json.load(f)
    f.close()

    # change whatever values you want
    myJson["name"] = name

    # open/create an output file, which will have actual values inputted
    f = open("output.json", "w")
    json.dump(myJson, f)
    f.close()

#program
id = randomId()

id = liMaker(id)


fillName(randomName(id[0], id[1]))