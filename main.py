# so pretty much what this does is it makes a copy of resume.json
# and then fills it out with random information.
# 
# Name (str), Age (int), Skills [list], Experiences [list], Education [list], Additonal Notes (str)

import random
import shutil
import json

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