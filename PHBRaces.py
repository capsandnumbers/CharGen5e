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
    character.HP += 1
    character.toughnessTracker += 1
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


FeyAncestryDesc. You have advantage on saving throws against being charmed, and magic can't put you to sleep.
FeyAncestry = feature("Fey Ancestry","Race",FeyAncestryDesc)

TranceDesc = "Elves do not sleep. Instead they meditate deeply, remaining semi-conscious, for 4 hours a day. The Common word for this meditation is ""trance."" While meditating, you dream after a fashion; such dreams are actually mental exercises that have become reflexive after years of practice. After resting in this way, you gain the same benefit a human would from 8 hours of sleep."
TranceShowText = "You meditate for 4 hours a day instead of sleeping."
Trance = feature("Trance","Race",TranceDesc,showText = TranceShowText)


KeenSensesDesc = "You have proficiency in the Perception skill."
def KeenSensesFunc(character):
    character.addToList(character.skillProfs,"Perception")
KeenSenses = feature("KeenSenses","Race",KeenSensesDesc,function = KeenSensesFunc,hideFeature = True)

# Shared by both subraces, so placing here
ElfWeaponTrainingDesc = "You have proficiency with the longsword, shortsword, shortbow, and longbow."
def ElfWeaponTrainingFunc(character):
    character.addProficiency({"weapon": ["Longsword", "Shortsword","Shortbow","Longbow"]}
ElfWeaponTraining = feature("Elf Weapon Training","Subrace",ElfWeaponTraniningDesc,function = ElfWeaponTraniningFunc,hideFeature = True)

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
    character.spellDict.proficiencies[category].extend(items) # Test this!
Cantrip = feature("Cantrip","Subrace",CantripDesc,function = CantripFunc,hideFeature = True )


HighElfBonuses = {"Intelligence": 1}
HighElfFeatureList = [ElfWeaponTraining,Cantrip,ExtraLanguage]
HighElf = subrace("High Elf", Elf, HighElfBonuses,HighElfFeatureList)


