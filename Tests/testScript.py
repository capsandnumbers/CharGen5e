from CharGen5e.character import *
from CharGen5e.Sources.Test.TestSources import *

from CharGen5e.Sources.PHB.Backgrounds import *

from CharGen5e.Sources.SRD.Races import *
from CharGen5e.Sources.SRD.Subraces import *

from CharGen5e.Sources.SRD.Classes.fighterClass import *
from CharGen5e.Sources.SRD.Classes.monkClass import *



from CharGen5e.Sources.SRD.Subclasses.MonkSubclasses import *
from CharGen5e.Sources.PHB.Subclasses.MonkSubclasses import *
from CharGen5e.Sources.XGE.Subclasses.MonkSubclasses import *

from CharGen5e.Sources.SRD.Subclasses.FighterSubclasses import *
from CharGen5e.Sources.PHB.Subclasses.FighterSubclasses import *
from CharGen5e.Sources.XGE.Subclasses.FighterSubclasses import *
from CharGen5e.Sources.TCE.Subclasses.FighterSubclasses import *


from CharGen5e.Sources.SRD.Backgrounds import *
from CharGen5e.outToPDF import *
import os
from CharGen5e.classDefs import *

name = "Owain"
outString = name +".pdf"


if os.path.exists(outString):
    os.remove(outString)



Owain = character(name,1, TestBackground, Fighter,RuneKnight,TestRace)

Owain.listFeatures()

print(Owain.abilities)


#print(Owain.proficiencies)
#print(Owain.abilityMods,Owain.profBonus)

print(Owain.height)