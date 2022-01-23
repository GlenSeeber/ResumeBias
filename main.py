# so pretty much what this does is it makes a copy of resume.json
# and then fills it out with random information.
# 
# Name (str), Age (int), Skills [list], Experiences [list], Education [list], Additonal Notes (str)

import random
import json

def liMaker(string):
    li = list(string.split(', '))
    return li

def jsonRead(myPath):
    f = open(myPath, 'r')
    myJson = json.load(f)
    f.close()
    return myJson

def jsonWrite(myPath, dumpContent):
    f = open(myPath, "w")
    json.dump(dumpContent, f)
    f.close()

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

    return name

def fillName(name, gender, race):
    # makes a copy of resume.json (the template), pastes values into it on
    # output.json

    # open template file
    f = open("input.json", "r")
    myJson = json.load(f)
    f.close()

    # change whatever values you want
    myJson["Name"] = name
    myJson["Gender"] = gender
    myJson["Race"] = race

    # open/create an output file, which will have actual values inputted
    f = open("output.json", "w")
    json.dump(myJson, f)
    f.close()

def stamp():
    # covers up the top of a resume with a fake name and identity
    id = randomId()

    id = liMaker(id)

    name = randomName(id[0], id[1])

    fillName(name, id[0], id[1])

def sendResume():
    global resumeCount
    #open 
    myJson = jsonRead('resume'+str(resumeCount)+'.json')

    jsonWrite('input.json', myJson)

    stamp()

    #send the file to frontend
    #confirm it has been recieved (somehow)

    resumeCount += 1

#program

resumeCount = 0

run = True

while run:
    # change condition to:
    # "if a request has been recieved from frontend"
    if True:
        sendResume()
    # change to an if statement, if "client is unresponsive", then quit, or something
    run = False