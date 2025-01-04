# PHBRaces
from classDefs import *




DarkvisionDwarfDesc = "Accustomed to life underground, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray."
DarkvisionDwarfShowText = "You can see in dim light as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness."
DarkvisionDwarf = feature("Darkvision 60 ft.", "Race", DarkvisionDwarfDesc,showText=DarkvisionDwarfShowText)


DwarvenResilienceDesc = 'You have advantage on saving throws against poison, and you have resistance against poison damage.'
def DwarvenResilienceFunc(character):
    addToList(character.damageResistances,"Poison")

DwarvenResilience = feature("Dwarven Resilience", "Race", DwarvenResilienceDesc, function = DwarvenResilienceFunc)







DwarvenCombatTrainingDesc = 'You have proficiency with the battleaxe, handaxe, light hammer, and warhammer.'
def DwarvenCombatTrainingFunc(character):
    character.addProficiency({"weapon": ['Battleaxe', 'Handaxe', 'Light hammer']})
    #addToList(character.proficiencies,['Battleaxe', 'Handaxe', 'Light hammer'])
DwarvenCombatTraining = feature("Dwarven Combat Training","Race",DwarvenCombatTrainingDesc, function = DwarvenCombatTrainingFunc, hideFeature=True) 



ToolProficiencyDwarfDesc = "You gain proficiency with the artisan's tools of your choice: smith's tools, brewer's supplies, or mason's tools."
def ToolProficiencyDwarfFunc(character):
    choice = arrayChoose(["Smith's tools", "Brewer's supplies", "Mason's tools"], 1)

    character.addProficiency({"tool": choice})
    #addToList(character.proficiencies, choice)
ToolProficiencyDwarf = feature('Tool Proficiency', 'Race', ToolProficiencyDwarfDesc, function = ToolProficiencyDwarfFunc, hideFeature=True) 


StonecunningDesc = "Whenever you make an Intelligence (History) check related to the origin of stonework, you are considered proficient in the History skill and add double your proficiency bonus to the check, instead of your normal proficiency bonus."
StonecunningShowText = "You make History checks related to the origin of stonework with Expertise."
Stonecunning = feature("Stonecunning","Race", StonecunningDesc, showText=StonecunningShowText) 







DwarvenToughnessDesc = "Your hit point maximum increases by 1, and it increases by 1 every time you gain a level."
def DwarvenToughnessFunc(character):
    # Assume that the character will never lose this feature
    
    character.HP += 1
DwarvenToughness = feature("Dwarven Toughness","Subrace",DwarvenToughnessDesc,levelsActive = allLevels, function = DwarvenToughnessFunc)


DwarvenArmorTrainingDesc = "You have proficiency with light and medium armor."
def DwarvenArmorTrainingFunc(character):
    character.addProficiency({"armor": ["Light Armor", "Medium Armor"]})
#    print('added')
DwarvenArmorTraining = feature("Dwarven Armor Training", "Subrace", DwarvenArmorTrainingDesc,function = DwarvenArmorTrainingFunc,hideFeature=True)



DwarfFeatureList = [DarkvisionDwarf, DwarvenResilience, DwarvenCombatTraining, ToolProficiencyDwarf, Stonecunning]
DwarfBonuses = {"Constitution": 2}



Dwarf = race("Dwarf","Medium",25,DwarfBonuses,{"language": ["Common","Dwarvish"]}, DwarfFeatureList, needsSubrace=True)




HillDwarfBonuses = {"Wisdom": 1}
HillDwarf = subrace("Hill Dwarf",Dwarf,HillDwarfBonuses,[DwarvenToughness])



MountainDwarfBonuses = {"Strength": 2}
MountainDwarf = subrace("Mountain Dwarf",Dwarf,MountainDwarfBonuses,featureList = [DwarvenArmorTraining])








#Dwarf = race("Dwarf","Medium",25,DwarfBonuses,{"language": ["Common","Dwarvish"]}, DwarfFeatureList, needsSubrace=True)


DarkvisionElfDesc = "Accustomed to twilit forests and the night sky, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray."
DarkvisionElfShowText = "You can see in dim light as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness."
DarkvisionElf = feature("Darkvision 60 ft.", "Race", DarkvisionElfDesc,showText=DarkvisionElfShowText)


FeyAncestryDesc = "You have advantage on saving throws against being charmed, and magic can't put you to sleep."
FeyAncestry = feature("Fey Ancestry","Race",FeyAncestryDesc)

TranceDesc = "Elves do not sleep. Instead they meditate deeply, remaining semi-conscious, for 4 hours a day. The Common word for this meditation is ""trance."" While meditating, you dream after a fashion; such dreams are actually mental exercises that have become reflexive after years of practice. After resting in this way, you gain the same benefit a human would from 8 hours of sleep."
TranceShowText = "You meditate for 4 hours a day instead of sleeping."
Trance = feature("Trance","Race",TranceDesc,showText = TranceShowText)


KeenSensesDesc = "You have proficiency in the Perception skill."
def KeenSensesFunc(character):
    #character.addToList(character.skillProfs,"Perception")
    character.addProficiency({"weapon": "Perception"}) 
KeenSenses = feature("KeenSenses","Race",KeenSensesDesc,function = KeenSensesFunc,hideFeature = True)

# Shared by both subraces, so placing here
ElfWeaponTrainingDesc = "You have proficiency with the longsword, shortsword, shortbow, and longbow."
def ElfWeaponTrainingFunc(character):
    character.addProficiency({"weapon": ["Longsword", "Shortsword","Shortbow","Longbow"]})
ElfWeaponTraining = feature("Elf Weapon Training","Subrace",ElfWeaponTrainingDesc,function = ElfWeaponTrainingFunc,hideFeature = True)

ElfBonuses = {"Dexterity": 2}
ElfFeatureList = [DarkvisionElf, FeyAncestry, Trance, KeenSenses]
Elf = race("Elf","Medium",30,ElfBonuses,{"language":["Common","Elvish"]}, ElfFeatureList, needsSubrace=True)






FleetOfFootDesc = "Fleet of Foot. Your base walking speed increases to 35 feet."
def FleetOfFootFunc(character):
    character.speed = 35
FleetOfFoot = feature("Fleet of Foot","Subrace",FleetOfFootDesc,function = FleetOfFootFunc,hideFeature = True)

MaskOfTheWildDesc = "You can attempt to hide even when you are only lightly obscured by foliage, heavy rain, falling snow, mist, and other natural phenomena."
MaskOfTheWild = feature("Mask of the Wild","Subrace",MaskOfTheWildDesc)


WoodElfBonuses = {"Wisdom": 1}
WoodElfFeatureList = [ElfWeaponTraining,FleetOfFoot,MaskOfTheWild]
WoodElf = subrace("Wood Elf", Elf, WoodElfBonuses,WoodElfFeatureList)








ExtraLanguageDesc = "You can read, speak, and write one additional language of your choice."
def ExtraLanguageFunc(character):
    eligibleLanguages = [lang for lang in allLanguages if lang not in character.proficiencies["language"]]
    chosenLang = r.choice(eligibleLanguages)
    character.addProficiency({"language":[chosenLang]})
ExtraLanguage = feature("Extra Language", "Subrace", ExtraLanguageDesc, function = ExtraLanguageFunc, hideFeature = True)


CantripDesc = "You know one cantrip of your choice from the Wizard spell list. Intelligence is your spellcasting ability for it."
def CantripFunc(character):
    eligibleSpells = [
        spell for spell, details in grimoire.items()
        if details["level"] == 0                     # Spell level is 0
        and spell in wizardSpellList                 # Spell is in wizard spell list
        and spell not in character.spellDict      # Spell is not in character's spellDict
    ]
    
    chosenSpell = r.choice(eligibleSpells)
    character.spellDict.extend({chosenSpell, "Intelligence"}) # Test this!
Cantrip = feature("Cantrip","Subrace",CantripDesc,function = CantripFunc,hideFeature = True )


HighElfBonuses = {"Intelligence": 1}
HighElfFeatureList = [ElfWeaponTraining,Cantrip,ExtraLanguage]
HighElf = subrace("High Elf", Elf, HighElfBonuses,HighElfFeatureList)


Lucky = feature("Lucky","Race", "When you roll a 1 on an attack roll, ability check, or saving throw, you can reroll the die. You must use the new result, even if it is a 1.")
Brave = feature("Brave","Race", "You have advantage on saving throws against being frightened.")
Nimble = feature("Nimble","Race","You can move through the space of any creature that is of a size larger than yours.")

Halfling = race("Halfling","Small",25,{"Dexterity": 2},{"language": ["Common","Halfling"]}, [Lucky, Brave, Nimble], needsSubrace=True)


NaturallyStealthy = feature("Naturally Stealthy","Subrace","You can attempt to hide even when you are only obscured by a creature that is at least one size larger than you.")
LightfootHalfling = subrace("Lightfoot Halfling",Halfling,{"Charisma": 1},[NaturallyStealthy])



def StoutResilianceFunc(character): 
    addToList(character.damageResistances,"Poison")
StoutResiliance = feature("Stout Resiliance","Subrace","You have advantage on saving throws against poison, and you have resistance to poison damage.",function = StoutResilianceFunc)
StoutHalfling = subrace("Stout Halfling",Halfling,{"Constitution": 1},[StoutResiliance])









Dragonborn = race("Dragonborn", "Medium",30,{"Strength":2,"Charisma":1},{"language": ["Common","Draconic"]},[], needsSubrace = True)

                             

LineArea = "a 5 by 30 ft. line"
ConeArea = "15 ft. cone"





DraconicAncestryGeneric = "You are distantly related to a particular kind of dragon. Choose a type of dragon from the below list; this determines the damage and area of your breath weapon, and the type of resistance you gain."

BreathWeaponGenericDesc = "You can use your action to exhale destructive energy. It deals damage in an area according to your ancestry. When you use your breath weapon, all creatures in the area must make a saving throw, the type of which is determined by your ancestry. The DC of this saving throw is 8 + your Constitution modifier + your proficiency bonus. A creature takes 2d6 damage on a failed save, and half as much damage on a successful one. The damage increase to 3d6 at 6th level, 4d6 at 11th, and 5d6 at 16th level. After using your breath weapon, you cannot use it again until you complete a short or long rest."
BreathWeaponGenericShowText = "As an action you exhale destructive energy, causing all creatures in AREA to make a SAVETYPE saving throw with DC DCVALUE. A creature takes DAMAGE DTYPE damage on a failed save, and half as much on a successful one."

DragonbornStats = {
    "Black": { 
        "damageType": "Acid",
        "Area": LineArea,
        "Save": "Dexterity",
        "breathWeaponShowText": BreathWeaponGenericShowText 
    },
    "Blue": { 
        "damageType": "Lightning",
        "Area": LineArea,
        "Save": "Dexterity",
        "breathWeaponShowText": BreathWeaponGenericShowText
    },
    "Brass": { 
        "damageType": "Fire",
        "Area": LineArea,
        "Save": "Dexterity",
        "breathWeaponShowText": BreathWeaponGenericShowText
    },
    "Bronze": { 
        "damageType": "Lightning",
        "Area": LineArea,
        "Save": "Dexterity",
        "breathWeaponShowText": BreathWeaponGenericShowText
    },
    "Copper": { 
        "damageType": "Acid",
        "Area": LineArea,
        "Save": "Dexterity",
        "breathWeaponShowText": BreathWeaponGenericShowText
    },
    "Gold": { 
        "damageType": "Fire",
        "Area": ConeArea,
        "Save": "Dexterity",
        "breathWeaponShowText": BreathWeaponGenericShowText
    },
    "Green": { 
        "damageType": "Poison",
        "Area": ConeArea,
        "Save": "Constitution",
        "breathWeaponShowText": BreathWeaponGenericShowText
    },
    "Red": { 
        "damageType": "Fire",
        "Area": ConeArea,
        "Save": "Dexterity",
        "breathWeaponShowText": BreathWeaponGenericShowText
    },
    "Silver": { 
        "damageType": "Cold",
        "Area": ConeArea,
        "Save": "Constitution",
        "breathWeaponShowText": BreathWeaponGenericShowText
    },
    "White": { 
        "damageType": "Cold",
        "Area": ConeArea,
        "Save": "Constitution",
        "breathWeaponShowText": BreathWeaponGenericShowText
    },
}

for key, details in DragonbornStats.items():
    details["breathWeaponShowText"] = details["breathWeaponShowText"].replace("AREA", details["Area"])
    details["breathWeaponShowText"] = details["breathWeaponShowText"].replace("SAVETYPE", details["Save"])
    details["breathWeaponShowText"] = details["breathWeaponShowText"].replace("DTYPE", details["damageType"])




DamageResistanceDesc = "You have resistance to the damage type associated with your ancestry."


def BreathWeaponFunc(character):
    raceName = character.race.name
        
    color = raceName.replace(" Dragonborn","")
    #print("Color:", color)
    details = DragonbornStats[color]
    initialShowText = details["breathWeaponShowText"]
    #print("Details:",details)

    for feature in character.features:
        if feature.name == "Breath Weapon":

            if character.level >= 16:
                damageValue = "5d6"
            elif character.level >= 11:
                damageValue = "4d6"
            elif character.level >= 6:
                damageValue = "3d6"
            else:
                damageValue = "2d6"
            
            feature.showText = details["breathWeaponShowText"]
            feature.showText = feature.showText.replace("DAMAGE", damageValue)
            feature.showText = feature.showText.replace("DCVALUE", str(int(8 + abMod(character.abilities["Constitution"])   + character.profMod)))


def DamageResistanceFunc(character):
    raceName = character.race.name
    color = raceName.replace(" Dragonborn","")
    damageType = DragonbornStats[color]["damageType"]
    addToList(character.damageResistances,damageType)

DamageResistance = feature("Damage Resistance", "Subrace", DamageResistanceDesc, function = DamageResistanceFunc, hideFeature = True)

                                                          
for color, details in DragonbornStats.items():
    varName = color + "Dragonborn"
    showName = color + " Dragonborn"
    breathWeaponVarName = "BreathWeapon" + color



    damageResistanceVarName = "DamageResistance" + color


    globals()[breathWeaponVarName] = feature("Breath Weapon", "Subrace", BreathWeaponGenericDesc, showText = BreathWeaponGenericShowText, levelsActive = allLevels, function = BreathWeaponFunc)
    globals()[damageResistanceVarName] = feature("Damage Resistance", "Subrace", DamageResistanceDesc, function = DamageResistanceFunc, hideFeature = True)
    
    globals()[varName] = subrace(showName,Dragonborn,{},featureList = [eval(breathWeaponVarName),eval(damageResistanceVarName)])

