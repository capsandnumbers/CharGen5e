# PHBRaces
from CharGen5e.classDefs import *

Guy = race("Guy","Medium",30,{},{},[])


DarkvisionDwarfDesc = "Accustomed to life underground, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray."
DarkvisionDwarfText = "You can see in dim light as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness."
DarkvisionDwarf = feature("Darkvision 60 ft.", "Race", DarkvisionDwarfDesc,DarkvisionDwarfText)


DwarvenResilienceDesc = 'You have advantage on saving throws against poison, and you have resistance against poison damage.'
def DwarvenResilienceFunc(character):
    addToList(character.damageResistances,"Poison")

DwarvenResilience = feature("Dwarven Resilience", "Race", DwarvenResilienceDesc,None, function = DwarvenResilienceFunc)







DwarvenCombatTrainingDesc = 'You have proficiency with the battleaxe, handaxe, light hammer, and warhammer.'
def DwarvenCombatTrainingFunc(character):
    character.addProficiency({"weapon": ['Battleaxe', 'Handaxe', 'Light hammer']})
    #addToList(character.proficiencies,['Battleaxe', 'Handaxe', 'Light hammer'])
DwarvenCombatTraining = feature("Dwarven Combat Training","Race",DwarvenCombatTrainingDesc,None, function = DwarvenCombatTrainingFunc, hideFeature=True) 



ToolProficiencyDwarfDesc = "You gain proficiency with the artisan's tools of your choice: smith's tools, brewer's supplies, or mason's tools."
def ToolProficiencyDwarfFunc(character):
    choice = arrayChoose(["Smith's tools", "Brewer's supplies", "Mason's tools"], 1)

    character.addProficiency({"tool": choice})
    #addToList(character.proficiencies, choice)
ToolProficiencyDwarf = feature('Tool Proficiency', 'Race', ToolProficiencyDwarfDesc, None,function = ToolProficiencyDwarfFunc, hideFeature=True) 


StonecunningDesc = "Whenever you make an Intelligence (History) check related to the origin of stonework, you are considered proficient in the History skill and add double your proficiency bonus to the check, instead of your normal proficiency bonus."
StonecunningText = "You make History checks related to the origin of stonework with Expertise."
Stonecunning = feature("Stonecunning","Race", StonecunningDesc,StonecunningText) 




DwarfFeatureList = [DarkvisionDwarf, DwarvenResilience, DwarvenCombatTraining, ToolProficiencyDwarf, Stonecunning]
DwarfBonuses = {"Constitution": 2}



Dwarf = race("Dwarf","Medium",25,DwarfBonuses,{"language": ["Common","Dwarvish"]}, DwarfFeatureList, needsSubrace=True)















DarkvisionElfDesc = "Accustomed to twilit forests and the night sky, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray."
DarkvisionElfText = "You can see in dim light as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness."
DarkvisionElf = feature("Darkvision 60 ft.", "Race", DarkvisionElfDesc,DarkvisionElfText)


FeyAncestryDesc = "You have advantage on saving throws against being charmed, and magic can't put you to sleep."
FeyAncestry = feature("Fey Ancestry","Race",FeyAncestryDesc,None)

TranceDesc = "Elves do not sleep. Instead they meditate deeply, remaining semi-conscious, for 4 hours a day. The Common word for this meditation is ""trance."" While meditating, you dream after a fashion; such dreams are actually mental exercises that have become reflexive after years of practice. After resting in this way, you gain the same benefit a human would from 8 hours of sleep."
TranceText = "You meditate for 4 hours a day instead of sleeping."
Trance = feature("Trance","Race",TranceDesc, TranceText)


KeenSensesDesc = "You have proficiency in the Perception skill."
def KeenSensesFunc(character):
    #character.addToList(character.skillProfs,"Perception")
    character.addProficiency({"skill": ["Perception"]}) 
KeenSenses = feature("KeenSenses","Race",KeenSensesDesc,None,function = KeenSensesFunc,hideFeature = True)

# Shared by both subraces, so placing here
ElfWeaponTrainingDesc = "You have proficiency with the longsword, shortsword, shortbow, and longbow."
def ElfWeaponTrainingFunc(character):
    character.addProficiency({"weapon": ["Longsword", "Shortsword","Shortbow","Longbow"]})
ElfWeaponTraining = feature("Elf Weapon Training","Subrace",ElfWeaponTrainingDesc,None,function = ElfWeaponTrainingFunc,hideFeature = True)

ElfBonuses = {"Dexterity": 2}
ElfFeatureList = [DarkvisionElf, FeyAncestry, Trance, KeenSenses]
Elf = race("Elf","Medium",30,ElfBonuses,{"language":["Common","Elvish"]}, ElfFeatureList, needsSubrace=True)




















Lucky = feature("Lucky","Race", "When you roll a 1 on an attack roll, ability check, or saving throw, you can reroll the die. You must use the new result, even if it is a 1.",None)
Brave = feature("Brave","Race", "You have advantage on saving throws against being frightened.",None)
Nimble = feature("Nimble","Race","You can move through the space of any creature that is of a size larger than yours.",None)

Halfling = race("Halfling","Small",25,{"Dexterity": 2},{"language": ["Common","Halfling"]}, [Lucky, Brave, Nimble], needsSubrace=True)








Dragonborn = race("Dragonborn", "Medium",30,{"Strength":2,"Charisma":1},{"language": ["Common","Draconic"]},[], needsSubrace = True)

                             

LineArea = "a 5 by 30 ft. line"
ConeArea = "15 ft. cone"





DraconicAncestryGeneric = "You are distantly related to a particular kind of dragon. Choose a type of dragon from the below list; this determines the damage and area of your breath weapon, and the type of resistance you gain."

BreathWeaponGenericDesc = "You can use your action to exhale destructive energy. It deals damage in an area according to your ancestry. When you use your breath weapon, all creatures in the area must make a saving throw, the type of which is determined by your ancestry. The DC of this saving throw is 8 + your Constitution modifier + your proficiency bonus. A creature takes 2d6 damage on a failed save, and half as much damage on a successful one. The damage increase to 3d6 at 6th level, 4d6 at 11th, and 5d6 at 16th level. After using your breath weapon, you cannot use it again until you complete a short or long rest."
BreathWeaponGenericText = "As an action you exhale destructive energy, causing all creatures in AREA to make a SAVETYPE saving throw with DC DCVALUE. A creature takes DAMAGE DTYPE damage on a failed save, and half as much on a successful one."



DragonbornStats = {
    "Black": { 
        "damageType": "Acid",
        "Area": LineArea,
        "Save": "Dexterity"
    },
    "Blue": { 
        "damageType": "Lightning",
        "Area": LineArea,
        "Save": "Dexterity"
    },
    "Brass": { 
        "damageType": "Fire",
        "Area": LineArea,
        "Save": "Dexterity"
    },
    "Bronze": { 
        "damageType": "Lightning",
        "Area": LineArea,
        "Save": "Dexterity"
    },
    "Copper": { 
        "damageType": "Acid",
        "Area": LineArea,
        "Save": "Dexterity"
    },
    "Gold": { 
        "damageType": "Fire",
        "Area": ConeArea,
        "Save": "Dexterity"
    },
    "Green": { 
        "damageType": "Poison",
        "Area": ConeArea,
        "Save": "Constitution"
    },
    "Red": { 
        "damageType": "Fire",
        "Area": ConeArea,
        "Save": "Dexterity"
    },
    "Silver": { 
        "damageType": "Cold",
        "Area": ConeArea,
        "Save": "Constitution"
    },
    "White": { 
        "damageType": "Cold",
        "Area": ConeArea,
        "Save": "Constitution"
    },
}


BreathWeaponDamageSchedule = {
    16:5,
    11:4,
    6:3,
    1:2
}



def getDragonbornColor(character):
    raceName = character.race.name
    color = raceName.replace(" Dragonborn","")
    return color


def BreathWeaponTextFunc(character):
    color = getDragonbornColor(character)
    area = DragonbornStats[color]["Area"]
    saveType = DragonbornStats[color]["Save"]
    saveDC = str(8 + character.abilityMods["Constitution"]   + character.profMod)
    damageValue = str(matchToSchedule(BreathWeaponDamageSchedule,character))+ "d6"
    damageType = DragonbornStats[color]["damageType"]

    return "As an action you exhale destructive energy, causing all creatures in "+area+ "to make a "+saveType+" saving throw with DC "+ saveDC+". A creature takes " + damageValue + " " + damageType + " damage on a failed save, and half as much on a successful one."


DamageResistanceDesc = "You have resistance to the damage type associated with your ancestry."


def DamageResistanceFunc(character):
    
    color = getDragonbornColor(character)
    damageType = DragonbornStats[color]["damageType"]
    addToList(character.damageResistances,damageType)

DamageResistance = feature("Damage Resistance", "Subrace", DamageResistanceDesc,None, function = DamageResistanceFunc, hideFeature = True)

                                                          
for color, details in DragonbornStats.items():
    varName = color + "Dragonborn"
    showName = color + " Dragonborn"
    breathWeaponVarName = "BreathWeapon" + color



    damageResistanceVarName = "DamageResistance" + color


    globals()[breathWeaponVarName] = feature("Breath Weapon", "Subrace", BreathWeaponGenericDesc,BreathWeaponGenericText, levelsActive = allLevels, textFunc = BreathWeaponTextFunc)
    globals()[damageResistanceVarName] = feature("Damage Resistance", "Subrace", DamageResistanceDesc,None, function = DamageResistanceFunc, hideFeature = True)
    
    globals()[varName] = subrace(showName,Dragonborn,{},featureList = [eval(breathWeaponVarName),eval(damageResistanceVarName)])

