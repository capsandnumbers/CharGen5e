from character import *
from Races.PHBRaces import *
from Races.SRDRaces import *
from fighterClass import *
from fighterSubclasses import *
from backgrounds import *
from PHBBackgrounds import *
import os

name = "Owain"
outString = name +".pdf"


if os.path.exists(outString):
    os.remove(outString)


Owain = character(name,20, Urchin, Fighter,Champion, Dwarf, HillDwarf)
#Owain.exportCharacter()

#print(Owain.skillMods)
#print(Owain.proficiencies["skill"])
#print(Owain.abilities,Owain.profMod)

#Charles = character("Charles",5,Urchin,Fighter,Champion,Dwarf,HillDwarf)
print("Owain")
Owain.listFeatures()