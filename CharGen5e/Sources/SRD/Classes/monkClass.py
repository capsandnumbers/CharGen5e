#MonkClass

from CharGen5e.classDefs import *
from CharGen5e.character import *



Monk = charClass("Monk",8,["Strength","Constitution","Charisma"],["Strength","Dexterity"],['Acrobatics', 'Athletics', 'History', 'Insight', 'Religion', 'Stealth'],2,{"weapon": [simpleWeapons, "Shortsword"]},[],ASISchedules["Monk"],optionalProfs = ["tool",[artisansTools+musicalInstruments],1])

