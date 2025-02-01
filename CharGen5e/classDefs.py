# Class Defs
from CharGen5e.header import *

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





artisansTools = ["Alchemist’s Supplies", "Brewer’s Supplies", "Calligrapher's Supplies", "Carpenter’s Tools", "Cartographer’s Tools", "Cobbler’s Tools", "Cook’s Utensils", "Glassblower’s Tools", "Jeweler’s Tools", "Leatherworker’s Tools", "Mason’s Tools", "Painter’s Supplies", "Potter’s Tools", "Smith’s Tools", "Tinker’s Tools", "Weaver’s Tools", "Woodcarver’s Tools"]
musicalInstruments = ["Lute","Drum"]

allProfs = {
    "Thieves Tools": "Tool",
    "Light Armor": "Armor"
}

weaponsDict = {'Club': {'Expertise': 'Simple', 'CombatType': 'Melee', 'Cost': 0.1, 'Damage': '1d4', 'DamageType': 'bludgeoning', 'Weight': 2.0, 'Properties': "['Light']"}, 'Dagger': {'Expertise': 'Simple', 'CombatType': 'Melee', 'Cost': 2.0, 'Damage': '1d4', 'DamageType': 'piercing', 'Weight': 1.0, 'Properties': "['Finesse','Light']"}, 'Greatclub': {'Expertise': 'Simple', 'CombatType': 'Melee', 'Cost': 0.2, 'Damage': '1d8', 'DamageType': 'bludgeoning', 'Weight': 10.0, 'Properties': "['Two-Handed']"}, 'Handaxe': {'Expertise': 'Simple', 'CombatType': 'Melee', 'Cost': 5.0, 'Damage': '1d6', 'DamageType': 'slashing', 'Weight': 2.0, 'Properties': "['Light','Thrown (20/60)']"}, 'Javelin': {'Expertise': 'Simple', 'CombatType': 'Melee', 'Cost': 0.5, 'Damage': '1d6', 'DamageType': 'piercing', 'Weight': 2.0, 'Properties': "['Thrown (30/120)']"}, 'Light hammer': {'Expertise': 'Simple', 'CombatType': 'Melee', 'Cost': 2.0, 'Damage': '1d4', 'DamageType': 'bludgeoning', 'Weight': 2.0, 'Properties': "['Light','Thrown (20/60)']"}, 'Mace': {'Expertise': 'Simple', 'CombatType': 'Melee', 'Cost': 5.0, 'Damage': '1d6', 'DamageType': 'bludgeoning', 'Weight': 4.0, 'Properties': '[]'}, 'Quarterstaff': {'Expertise': 'Simple', 'CombatType': 'Melee', 'Cost': 0.2, 'Damage': '1d6', 'DamageType': 'bludgeoning', 'Weight': 4.0, 'Properties': "['Versatile (1d8)']"}, 'Sickle': {'Expertise': 'Simple', 'CombatType': 'Melee', 'Cost': 1.0, 'Damage': '1d4', 'DamageType': 'slashing', 'Weight': 2.0, 'Properties': "['Light']"}, 'Spear': {'Expertise': 'Simple', 'CombatType': 'Melee', 'Cost': 1.0, 'Damage': '1d6', 'DamageType': 'piercing', 'Weight': 3.0, 'Properties': "['Thrown (20/60)','Versatile (1d8)']"}, 'Light Crossbow': {'Expertise': 'Simple', 'CombatType': 'Ranged', 'Cost': 25.0, 'Damage': '1d8', 'DamageType': 'piercing', 'Weight': 5.0, 'Properties': "['Ammunition','Range (80/320)']"}, 'Dart': {'Expertise': 'Simple', 'CombatType': 'Ranged', 'Cost': 0.05, 'Damage': '1d4', 'DamageType': 'piercing', 'Weight': 0.25, 'Properties': "['Finesse','Thrown (20/60)']"}, 'Shortbow': {'Expertise': 'Simple', 'CombatType': 'Ranged', 'Cost': 25.0, 'Damage': '1d6', 'DamageType': 'piercing', 'Weight': 2.0, 'Properties': "['Ammunition','Range (80/320)']"}, 'Sling': {'Expertise': 'Simple', 'CombatType': 'Ranged', 'Cost': 0.1, 'Damage': '1d4', 'DamageType': 'bludgeoning', 'Weight': 0.0, 'Properties': "['Ammunition','Range (30/120)']"}, 'Battleaxe': {'Expertise': 'Martial', 'CombatType': 'Melee', 'Cost': 10.0, 'Damage': '1d8', 'DamageType': 'slashing', 'Weight': 4.0, 'Properties': "['Versatile (1d10)']"}, 'Flail': {'Expertise': 'Martial', 'CombatType': 'Melee', 'Cost': 10.0, 'Damage': '1d8', 'DamageType': 'bludgeoning', 'Weight': 2.0, 'Properties': '[]'}, 'Glaive': {'Expertise': 'Martial', 'CombatType': 'Melee', 'Cost': 20.0, 'Damage': '1d10', 'DamageType': 'slashing', 'Weight': 6.0, 'Properties': "['Heavy','Reach']"}, 'Greataxe': {'Expertise': 'Martial', 'CombatType': 'Melee', 'Cost': 30.0, 'Damage': '1d12', 'DamageType': 'slashing', 'Weight': 7.0, 'Properties': "['Heavy','Two-Handed']"}, 'Greatsword': {'Expertise': 'Martial', 'CombatType': 'Melee', 'Cost': 50.0, 'Damage': '2d6', 'DamageType': 'slashing', 'Weight': 6.0, 'Properties': "['Heavy','Two-Handed']"}, 'Halberd': {'Expertise': 'Martial', 'CombatType': 'Melee', 'Cost': 20.0, 'Damage': '1d10', 'DamageType': 'slashing', 'Weight': 6.0, 'Properties': "['Heavy','Reach']"}, 'Special': {'Expertise': 'Martial', 'CombatType': 'Melee', 'Cost': 10.0, 'Damage': '1d12', 'DamageType': 'piercing', 'Weight': 6.0, 'Properties': "['Reach','Lance']"}, 'Longsword': {'Expertise': 'Martial', 'CombatType': 'Melee', 'Cost': 15.0, 'Damage': '1d8', 'DamageType': 'slashing', 'Weight': 3.0, 'Properties': "['Versatile (1d10)']"}, 'Maul': {'Expertise': 'Martial', 'CombatType': 'Melee', 'Cost': 10.0, 'Damage': '2d6', 'DamageType': 'bludgeoning', 'Weight': 10.0, 'Properties': "['Heavy','Two-Handed']"}, 'Morningstar': {'Expertise': 'Martial', 'CombatType': 'Melee', 'Cost': 15.0, 'Damage': '1d8', 'DamageType': 'piercing', 'Weight': 4.0, 'Properties': '[]'}, 'Pike': {'Expertise': 'Martial', 'CombatType': 'Melee', 'Cost': 5.0, 'Damage': '1d10', 'DamageType': 'piercing', 'Weight': 18.0, 'Properties': "['Heavy','Reach']"}, 'Rapier': {'Expertise': 'Martial', 'CombatType': 'Melee', 'Cost': 25.0, 'Damage': '1d8', 'DamageType': 'piercing', 'Weight': 2.0, 'Properties': "['Finesse']"}, 'Scimitar': {'Expertise': 'Martial', 'CombatType': 'Melee', 'Cost': 25.0, 'Damage': '1d6', 'DamageType': 'slashing', 'Weight': 3.0, 'Properties': "['Finesse','Light']"}, 'Shortsword': {'Expertise': 'Martial', 'CombatType': 'Melee', 'Cost': 10.0, 'Damage': '1d6', 'DamageType': 'piercing', 'Weight': 2.0, 'Properties': "['Finesse','Light']"}, 'Trident': {'Expertise': 'Martial', 'CombatType': 'Melee', 'Cost': 5.0, 'Damage': '1d6', 'DamageType': 'piercing', 'Weight': 4.0, 'Properties': "['Thrown (20/60)','Versatile (1d8)']"}, 'War pick': {'Expertise': 'Martial', 'CombatType': 'Melee', 'Cost': 5.0, 'Damage': '1d8', 'DamageType': 'piercing', 'Weight': 2.0, 'Properties': '[]'}, 'Warhammer': {'Expertise': 'Martial', 'CombatType': 'Melee', 'Cost': 15.0, 'Damage': '1d8', 'DamageType': 'bludgeoning', 'Weight': 2.0, 'Properties': "['Versatile (1d10)']"}, 'Whip': {'Expertise': 'Martial', 'CombatType': 'Melee', 'Cost': 2.0, 'Damage': '1d4', 'DamageType': 'slashing', 'Weight': 3.0, 'Properties': "['Finesse','Reach']"}, 'Blowgun': {'Expertise': 'Martial', 'CombatType': 'Ranged', 'Cost': 10.0, 'Damage': 1, 'DamageType': 'piercing', 'Weight': 1.0, 'Properties': "['Ammunition','Range (25/100)']"}, 'Hand Crossbow': {'Expertise': 'Martial', 'CombatType': 'Ranged', 'Cost': 75.0, 'Damage': '1d6', 'DamageType': 'piercing', 'Weight': 3.0, 'Properties': "['Ammunition','Range (30/120)']"}, 'Heavy Crossbow': {'Expertise': 'Martial', 'CombatType': 'Ranged', 'Cost': 50.0, 'Damage': '1d10', 'DamageType': 'piercing', 'Weight': 18.0, 'Properties': "['Ammunition','Range (100/400)']"}, 'Longbow': {'Expertise': 'Martial', 'CombatType': 'Ranged', 'Cost': 50.0, 'Damage': '1d8', 'DamageType': 'piercing', 'Weight': 2.0, 'Properties': "['Ammunition','Range (150/600)']"}, 'Special': {'Expertise': 'Martial', 'CombatType': 'Ranged', 'Cost': 1.0, 'Weight': 3.0, 'Properties': "['Net','Thrown (5/15)']"}}


simpleWeapons  = [weapon for weapon, info in weaponsDict.items() if info['Expertise'] == 'Simple']
martialWeapons = [weapon for weapon, info in weaponsDict.items() if info['Expertise'] == 'Martial']




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
    "Minor Illusion": {
        "level": 0,  # Cantrips are level 0
        "description": "You create a sound or an image of an object within range",
        "range": "30 feet",
        "components": ["S", "M"],
        "duration": "1 minute",
        "material":  "A bit of fleece"
    }
}

# Make spell list an attribute of charClass?
wizardSpellList = ["Light", "Nage Hand", "Prestidigitation"]





ASISchedules = {"Fighter":[4,6,8,12,14,16,19],"Monk":[4,8,12,16,19]}



# Would some of these be better as dictionaries?



class charClass():
    def __init__(self, name, HD, abilityPreference, saveProfs, classSkills, skillsToChoose, proficiencies, featureList, ASISchedule,optionalProfs = None):


        setupInputArgs(self,inspect.currentframe())


                    

class charSubclass():
    def __init__(self, name, parent, featureList, abilityPreference=[],optionalProfs = None):
        setupInputArgs(self,inspect.currentframe())




class background():
    def __init__(self, name, proficiencies, featureList,optionalProfs = None):
        setupInputArgs(self,inspect.currentframe())


class race():
    def __init__(self, name, size, speed, abilityBonus, proficiencies, featureList, needsSubrace = False,optionalProfs = None):
        setupInputArgs(self,inspect.currentframe())
        if needsSubrace:
            self.subraces = []



class subrace():
    def __init__(self, name, parent, abilityBonus, featureList = [], proficiencies = {},optionalProfs = None):
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
    
    combinedRace.optionalProfs = (inputRace.optionalProfs or []) + (inputSubrace.optionalProfs or [])



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



def stagedReplacePlaceholders(schedule,inputText,replaceText):

    def featureTextFunc(character):
        level = character.level
        text = inputText

        # Iterate over the schedule in reverse order to find the applicable feature text
        for key in sorted(schedule.keys()):
            if level >= key:
                text = text.replace(replaceText,schedule[key])

        
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

def matchToSchedule(schedule, character):
    level = character.level
    applicable_levels = [key for key in schedule if key <= level]
    if not applicable_levels:
        return None  # No matching level found
    return schedule[max(applicable_levels)]

class feature():
    def __init__(self, name, source, description, text, levelsActive = [1], function = None, textFunc = None,callback = None, hideFeature = False, replaces = None):
        setupInputArgs(self,inspect.currentframe())
        
        self.hasFunction = self.function is not None
        self.hasTextFunc = self.textFunc is not None
        self.hasCallback = self.callback is not None

        
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



ASIDesc = "You can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature."

def ASIFunc(character):
    #print(character.level)
    #print(character.charClass.ASISchedule)
    if character.level in character.charClass.ASISchedule:
        for i in range(2):  # Two ASI increases
            abilities = character.charClass.abilityPreference
            
            # Filter preferred abilities to exclude those already at 20
            eligibleAbilities = [ability for ability in abilities if character.abilities[ability] < 20]

            if eligibleAbilities:
                # Pick a preferred ability that is below 20
                chosenAbility = r.choice(eligibleAbilities)
            else:
                # If all preferred abilities are 20, pick randomly from all abilities below 20
                eligibleAbilities = [ability for ability in character.abilities if character.abilities[ability] < 20]
                if not eligibleAbilities:
                    #print("All abilities are already at 20. No ASI possible.")
                    return  # Exit the function since no abilities can be increased
                chosenAbility = r.choice(eligibleAbilities)

            # Increase the chosen ability
            character.abilities[chosenAbility] += 1



ASI = feature("ASI","Class",ASIDesc, allLevels,function = ASIFunc,hideFeature=True)
