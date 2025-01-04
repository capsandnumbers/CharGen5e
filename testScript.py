from character import *
from PHBRaces import *
from fighterClass import *
from backgrounds import *
import os

name = "Owain"
outString = name +".pdf"


if os.path.exists(outString):
    os.remove(outString)


Owain = character(name,1, Urchin, Fighter,Champion, Dwarf, HillDwarf)
Owain.exportCharacter()

print(Owain.skillMods)
print(Owain.proficiencies["skill"])
print(Owain.abilities,Owain.profMod)