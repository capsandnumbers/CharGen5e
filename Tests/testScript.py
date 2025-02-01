from CharGen5e.character import *
from CharGen5e.Sources.SRD.Races.SRDRaces import *
from CharGen5e.Sources.SRD.Races.SRDSubraces import *
from CharGen5e.Sources.SRD.Classes.fighterClass import *
from CharGen5e.Sources.SRD.Classes.monkClass import *
from CharGen5e.Sources.SRD.Subclasses.SRDMonkSubclasses import *
from CharGen5e.Sources.PHB.Subclasses.PHBMonkSubclasses import *

from CharGen5e.Sources.XGE.Subclasses.XGEMonkSubclasses import *
from CharGen5e.Sources.SRD.Backgrounds.SRDBackgrounds import *
from CharGen5e.outToPDF import *
import os
from CharGen5e.classDefs import *

name = "Owain"
outString = name +".pdf"


if os.path.exists(outString):
    os.remove(outString)



Owain = character(name,20, Acolyte, Monk,Kensei,Dwarf,HillDwarf)

#Owain.listFeatures()
print(Owain.proficiencies)