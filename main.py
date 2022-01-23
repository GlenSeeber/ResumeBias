# so pretty much what this does is it makes a copy of resume.json
# and then fills it out with random information.
# 
# Name (str), Age (int), Skills [list], Experiences [list], Education [list], Additonal Notes (str)

import random
import shutil
import json

def randomizer():
    # 2 genders * 3 races = 6 options
    # pick a random number 1-6
    # numbers correlate in this order:
    # White man, Black man, Latino man, White woman, Black woman, Latino Woman
    
    r = random.randint(0, 5)
    if (r <= 2):
        gender = "Masculine"

    elif (r >= 3):
        gender = "Feminine"
        r -= 3

    raceIndex = {0: "White", 1:"Black", 2:"Latino"}
    race = raceIndex[r]



#open template file
f = open("resume.json", "r")
myJson = json.load(f)
f.close()

#change whatever values you want
myJson["name"] = "james"

#open/create an output file, which will have actual values inputted
f = open("output.json", "w")
json.dump(myJson, f)
f.close()