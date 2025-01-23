#MonkClass

from dndCharGenerator.classDefs import *
from dndCharGenerator.character import *



from dndCharGenerator.character import *
from Races.PHBRaces import *
from Races.SRDRaces import *
from dndCharGenerator.fighterClass import *
from fighterSubclasses import *
from dndCharGenerator.backgrounds import *
from dndCharGenerator.PHBBackgrounds import *
import os

Monk = charClass("Monk",8,["Strength","Constitution","Charisma"],["Strength","Dexterity"],['Acrobatics', 'Athletics', 'History', 'Insight', 'Religion', 'Stealth'],2,{"weapon": [simpleWeapons, "Shortsword"]},[],ASISchedules["Monk"],optionalProfs = ["tool",[artisansTools+musicalInstruments],1])


Carl = character("Carl",20, Urchin, Fighter,Champion, Elf, HighElf)

print(Carl.proficiencies)