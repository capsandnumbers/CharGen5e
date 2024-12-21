from os import remove
import numpy as np
import random as r
import inspect
from header import *
from classDefs import *
from character import *
from fighterClass import *
from PHBRaces import *










citySecretsDesc = 'You know the secret patterns and flow to cities and can find passages through the urban sprawl that others would miss. When you are not in combat, you (and companions you lead) can travel between any two locations in the city twice as fast as your speed would normally allow.'
CitySecretsShowText = "When not in combat, you and your party can travel in the city twice as fast as your usual speed."
CitySecrets = feature("City Secrets","Background",citySecretsDesc, showText=CitySecretsShowText)


Urchin = background("Urchin",["Sleight of Hand","Athletics"],{"tool": ["Disguise kit, Thieves' tools"]},[CitySecrets])









#Wizard = charClass("Wizard",6,(3,2),(3,2),[],0,[])
Rogue = charClass("Rogue",8,["Dexterity","Wisdom"],["Dexterity", "Intelligence"],["Acrobatics", "Athletics", "Deception", "Insight", "Intimidation", "Investigation", "Perception", "Performance", "Persuasion"],4,{},[])


try:
   remove("Owain.pdf")
except:
   1
   
#Owain = character("Owain",5,Urchin,Fighter,"Champion",Dwarf,subrace=MountainDwarf)

Owain = character("Owain",10,Urchin,Fighter,Samurai,Dwarf,MountainDwarf)





print(Owain.name)


#print(Owain.level)
#print(Owain.race.name)
#print(Owain.subrace.name)
#print(Owain.abilities)
#print(Owain.HP)
print(Owain.proficiencies)
#print(Owain.weaponProfs)


#for feature in Owain.features:
#  if feature.hideFeature is not True:
#    print(feature.name)
#    print(feature.showText)


#Owain.exportCharacter()





