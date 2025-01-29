from CharGen5e.character import *
from CharGen5e.Sources.SRD.Races.SRDRaces import *
from CharGen5e.Sources.SRD.Races.SRDSubraces import *
from CharGen5e.Sources.SRD.Classes.fighterClass import *
from CharGen5e.Sources.SRD.Classes.monkClass import *
from CharGen5e.Sources.SRD.Subclasses.SRDMonkSubclasses import *
from CharGen5e.Sources.SRD.Backgrounds.SRDBackgrounds import *
from CharGen5e.outToPDF import *
import os

name = "Owain"
outString = name +".pdf"


if os.path.exists(outString):
    os.remove(outString)


Owain = character(name,20, Acolyte, Monk,OpenHand,Elf,HighElf)
#Owain.exportCharacter()

#print(Owain.skillMods)
#print(Owain.proficiencies["skill"])
#print(Owain.abilities,Owain.profMod)

#Charles = character("Charles",5,Urchin,Fighter,Champion,Dwarf,HillDwarf)

#Owain.listFeatures()
print(Owain.spellDict)