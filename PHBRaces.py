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
