# Class Defs
from dndCharGenerator.header import *

# Here I dump many useful lists and dictionaries to be referenced by functions/methods, some need completing

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


allLanguages = ["Common","Elvish","Dwarvish","Halfling","Goblin","Orcish"] # Idea: Split into common and rare/secret languages

standardLanguages = ["Common","Elvish","Dwarvish","Giant","Gnomish","Goblin","Halfling","Orc"]
exoticLanguages = ["Abyssal", "Celestial", "Draconic", "Deep Speech", "Infernal", "Primordial", "Sylvan", "Undercommon"]

allAbilities = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]

allArmor = ["Light Armor","Medium Armor","Heavy Armor","Shields"]

simpleWeapons = ["Quarterstaff","Whip"] # Increasingly I think weapons could be a dictionary
martialWeapons = ["Shortsword", "Longsword"]





artisansTools = ["Alchemist’s Supplies", "Brewer’s Supplies", "Calligrapher's Supplies", "Carpenter’s Tools", "Cartographer’s Tools", "Cobbler’s Tools", "Cook’s Utensils", "Glassblower’s Tools", "Jeweler’s Tools", "Leatherworker’s Tools", "Mason’s Tools", "Painter’s Supplies", "Potter’s Tools", "Smith’s Tools", "Tinker’s Tools", "Weaver’s Tools", "Woodcarver’s Tools"]
musicalInstruments = ["Lute","Drum"]

allProfs = {
    "Thieves Tools": "Tool",
    "Light Armor": "Armor"
}





# grimoire will contain all the spells in the game. Fill in using a spreadsheet, or maybe webscraping. Can extend with school, range, action type, ritual/concentration tags
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

# Make spell list an attribute of charClass?
wizardSpellList = ["Light", "Nage Hand", "Prestidigitation"]





ASISchedules = {"Fighter":[4,6,8,12,14,16,19],"Monk":[4,8,12,16,19]}



# Would some of these be better as dictionaries?
class charClass():
    def __init__(self, name, HD, abilityPreference, saveProfs, classSkills, skillsToChoose, proficiencies, featureList, ASISchedule,optionalProfs = None):


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
    def __init__(self, name, parent, abilityBonus, featureList = [], proficiencies = {}):
        setupInputArgs(self,inspect.currentframe())

        self.parent.subraces.append(self)



# Some races have subraces and some don't, so where there is a subrace I combine them
def combineRace(inputRace, inputSubrace):

    combinedRace = race(
        name=inputSubrace.name, # Take name of subrace. "Hill Dwarf" instead of "Dwarf"
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

    combinedRace.featureList.extend(inputSubrace.featureList)  # Add subrace's feature list to race's
    
    return combinedRace


# Features can come from a character's class, subclass, race, subrace,  or background
# The simplest ones don't change a character's stats - They just add text to a list of features
# Some add proficiencies to other lists, or might change character's HP
# Some need to be updated with a character's stats info. Example:
# Some are updated as a character levels. Example: The Fighter feature Action Surge

def stagedUpdate(schedule):

    def featureTextFunc(character):

        level = character.level
        text = ""

        # Iterate over the schedule in reverse order to find the applicable feature text
        for key in sorted(schedule.keys()):
            if level >= key:
                text = schedule[key]

        
        return text

    return featureTextFunc



def replacePlaceholders(text, character):

    # Dictionary of character stats that can be referenced in text
    stats = {
        "level": character.level,
        "CON": character.abilityMods["Constitution"],
        "WIS": character.abilityMods["Wisdom"]
        # Add other stats as needed
    }

    # Replace each placeholder in the text with the corresponding stat
    for placeholder, value in stats.items():
        text = text.replace(f"{{{placeholder}}}", str(value))


    return text



class feature():
    def __init__(self, name, source, description, levelsActive = [1],type = "Simple", function = None, hasFunction = False, hideFeature = False, text = None, textFunc = None):
        setupInputArgs(self,inspect.currentframe())
        if self.function is not None:
            self.hasFunction = True
        
        if self.text is None:
            self.text = description
        
        
        if isinstance(levelsActive,list):
            self.levelObtained = levelsActive[0]
        else:
            self.levelObtained = levelsActive


    def getText(self,character):
        if self.textFunc is None:
            return replacePlaceholders(self.text,character)
        else:
            return self.textFunc(character)
