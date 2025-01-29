from CharGen5e.classDefs import *
from CharGen5e.Sources.SRD.Races.SRDRaces import *







DwarvenToughnessDesc = "Your hit point maximum increases by 1, and it increases by 1 every time you gain a level."
def DwarvenToughnessFunc(character):
    # Assume that the character will never lose this feature
    
    character.HP += 1
DwarvenToughness = feature("Dwarven Toughness","Subrace",DwarvenToughnessDesc,levelsActive = allLevels, function = DwarvenToughnessFunc)




HillDwarfBonuses = {"Wisdom": 1}
HillDwarf = subrace("Hill Dwarf",Dwarf,HillDwarfBonuses,[DwarvenToughness])






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
        and spell not in character.spellDict[0]      # Spell is not in character's spellDict
    ]
    
    chosenSpell = r.choice(eligibleSpells)
    character.spellDict[0].append(chosenSpell) # Test this!
Cantrip = feature("Cantrip","Subrace",CantripDesc,function = CantripFunc,hideFeature = True )


HighElfBonuses = {"Intelligence": 1}
HighElfFeatureList = [ElfWeaponTraining,Cantrip,ExtraLanguage]
HighElf = subrace("High Elf", Elf, HighElfBonuses,HighElfFeatureList)



NaturallyStealthy = feature("Naturally Stealthy","Subrace","You can attempt to hide even when you are only obscured by a creature that is at least one size larger than you.")
LightfootHalfling = subrace("Lightfoot Halfling",Halfling,{"Charisma": 1},[NaturallyStealthy])


