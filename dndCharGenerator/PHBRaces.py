# PHBRaces
from dndCharGenerator.classDefs import *
from Races.SRDRaces import *


DwarvenArmorTrainingDesc = "You have proficiency with light and medium armor."
def DwarvenArmorTrainingFunc(character):
    character.addProficiency({"armor": ["Light Armor", "Medium Armor"]})
#    print('added')
DwarvenArmorTraining = feature("Dwarven Armor Training", "Subrace", DwarvenArmorTrainingDesc,function = DwarvenArmorTrainingFunc,hideFeature=True)




MountainDwarfBonuses = {"Strength": 2}
MountainDwarf = subrace("Mountain Dwarf",Dwarf,MountainDwarfBonuses,featureList = [DwarvenArmorTraining])












FleetOfFootDesc = "Fleet of Foot. Your base walking speed increases to 35 feet."
def FleetOfFootFunc(character):
    character.speed = 35
FleetOfFoot = feature("Fleet of Foot","Subrace",FleetOfFootDesc,function = FleetOfFootFunc,hideFeature = True)

MaskOfTheWildDesc = "You can attempt to hide even when you are only lightly obscured by foliage, heavy rain, falling snow, mist, and other natural phenomena."
MaskOfTheWild = feature("Mask of the Wild","Subrace",MaskOfTheWildDesc)


WoodElfBonuses = {"Wisdom": 1}
WoodElfFeatureList = [ElfWeaponTraining,FleetOfFoot,MaskOfTheWild]
WoodElf = subrace("Wood Elf", Elf, WoodElfBonuses,WoodElfFeatureList)



def StoutResilianceFunc(character): 
    addToList(character.damageResistances,"Poison")
StoutResiliance = feature("Stout Resiliance","Subrace","You have advantage on saving throws against poison, and you have resistance to poison damage.",function = StoutResilianceFunc)
StoutHalfling = subrace("Stout Halfling",Halfling,{"Constitution": 1},[StoutResiliance])






