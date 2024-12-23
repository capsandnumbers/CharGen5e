# Class Defs
from header import *


allLevels = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
allSkills = {
    "Acrobatics": "Dexterity",
    "Animal Handling": "Wisdom",
    "Arcana": "Intelligence",
    "Athletics": "Strength",
    "Deception": "Charisma",
    "History": "Intelligence",
    "Insight": "Wisdom",
    "Intimidation": "Charisma",
    "Investigation": "Intelligence",
    "Medicine": "Wisdom",
    "Nature": "Intelligence",
    "Perception": "Wisdom",
    "Performance": "Charisma",
    "Persuasion": "Charisma",
    "Religion": "Dexterity",
    "Sleight of Hand": "Dexterity",
    "Stealth": "Dexterity",
    "Survival":"Wisdom"
}


allLanguages = ["Common","Elvish","Dwarvish","Halfling","Goblin","Orcish"]

allAbilities = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]

allArmor = ["Light Armor","Medium Armor","Heavy Armor","Shields"]
simpleWeapons = ["Quarterstaff","Whip"]
martialWeapons = ["Shortsword", "Longsword"]


allProfs = {
    "Thieves Tools": "Tool",
    "Light Armor": "Armor"
}





# Fill in using a spreadsheet/webscraping. Can extend with school, range, action type, components, ritual/concentration tags
grimoire = { 
    "Light": {
        "level": 0,  # Cantrips are level 0
        "description": "Create light",
        "range": "Touch",
        "components": ["V", "M"],
        "material": "A firefly or phosphorescent moss"
    },
    "Mage Hand": {
        "level": 0,  # Cantrips are level 0
        "description": "Create a spectral hand that can manipulate objects",
        "range": "30 feet",
        "components": ["V", "S"],
        "material": None
    },
    "Prestidigitation": {
        "level": 0,  # Cantrips are level 0
        "description": "Minor arcane tricks",
        "range": "10 feet",
        "components": ["V", "S"],
        "material": None
    },
}

wizardSpellList = ["Light", "Nage Hand", "Prestidigitation"]


# Would some of these be better as dictionaries?
class charClass():
    def __init__(self, name, HD, abilityPreference, saveProfs, classSkills, skillsToChoose, proficiencies, featureList):
        setupInputArgs(self,inspect.currentframe())

class charSubclass():
    def __init__(self, name, parent, featureList, abilityPreference=[]):
        setupInputArgs(self,inspect.currentframe())




class background():
    def __init__(self, name, proficiencies, featureList):
        setupInputArgs(self,inspect.currentframe())


class race():
    def __init__(self, name, size, speed, abilityBonus, proficiencies, featureList, needsSubrace = False):
        setupInputArgs(self,inspect.currentframe())
        if needsSubrace:
            self.subraces = []



class subrace():
    def __init__(self, name, parent, abilityBonus, proficiencies = {}, featureList = []):
        setupInputArgs(self,inspect.currentframe())

        self.parent.subraces.append(self)

#class lineage():
def combineRace(inputRace, inputSubrace):
    # Make a shallow copy of the race to avoid modifying the original
    combinedRace = race(
        name=inputSubrace.name,  # Combine names
        size=inputRace.size,
        speed=inputRace.speed,
        abilityBonus=inputRace.abilityBonus.copy(),
        proficiencies=inputRace.proficiencies,
        featureList=inputRace.featureList[:]              
    )
    
    # Merge ability bonuses from subrace
    for ability, bonus in inputSubrace.abilityBonus.items():
        combinedRace.abilityBonus[ability] = bonus
    


    for category, items in inputSubrace.proficiencies.items():
        if category in combinedRace.proficiencies:
            combinedRace.proficiencies[category].extend(items)
        else:
            combinedRace.proficiencies[category] = items

    #character.addProficiency({"language": ["Light Armor", "Medium Armor"]})

    #combinedRace.proficiencies.extend(inputSubrace.proficiencies)
    combinedRace.featureList.extend(inputSubrace.featureList)  # Extend, not append
    
    return combinedRace



class feature():
    def __init__(self, name, source, description, levelsActive = [1], function = None, hasFunction = False, hideFeature = False, showText = None):
        setupInputArgs(self,inspect.currentframe())
        if self.function is not None:
            self.hasFunction = True
        
        if self.showText is None:
            self.showText = description
        
        
        if isinstance(levelsActive,list):
            self.levelObtained = levelsActive[0]
        else:
            self.levelObtained = levelsActive

    




#class spell():
#    def __init__(self, name, spellLevel, hasVerbal, hasSomatic, hasMaterial, isRitual ):
        
