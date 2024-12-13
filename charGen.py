from os import remove
import numpy as np
import random as r
import inspect


def setupInputArgs(self,frame):
        args, _, _, values = inspect.getargvalues(frame)
        for arg in args:
            if arg != 'self':
                setattr(self, arg, values[arg])

def abMod(abilityScore):
    return np.floor((abilityScore-10)/2)

def addToList(oldList, newEntry):
    if isinstance(newEntry, list):  # Check if newEntry is a list
        oldList.extend(newEntry)
    else:
        oldList.append(newEntry)
    # Deduplicate the list in-place
    unique_entries = list(dict.fromkeys(oldList))
    oldList.clear()
    oldList.extend(unique_entries)
  
def arrayChoose(inputArray, number, remove=True):
    # Check if we can safely choose `number` items
    if number > len(inputArray) and remove:
        raise ValueError("Cannot choose more items than are available when `remove` is True.")
    
    # If removing elements, work on a copy to avoid modifying the original list
    workingArray = inputArray[:] if remove else inputArray
    
    # Select items
    outputArray = []
    for _ in range(number):
        choice = r.choice(workingArray)  # Randomly select an element
        outputArray.append(choice)
        if remove:
            workingArray.remove(choice)  # Remove the chosen element only if `remove` is True
    
    return outputArray

#    setattr(character, attribute_name, value)


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
allAbilities = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]

allArmor = ["Light Armor","Medium Armor","Heavy Armor","Shields"]
simpleWeapons = ["Quarterstaff","Whip"]
martialWeapons = ["Shortsword", "Longsword"]









class charClass():
    def __init__(self, name, HD, abilityPreference, saveProfs, classSkills, skillsToChoose, armorProfs, weaponProfs, toolProfs, featureList):
        setupInputArgs(self,inspect.currentframe())

class background():
    def __init__(self, name, skillProfs, toolProfs, languages, featureList):
        setupInputArgs(self,inspect.currentframe())


class race():
    def __init__(self, name, size, speed, abilityBonus, languages, featureList, needsSubrace = True):
        setupInputArgs(self,inspect.currentframe())
        if needsSubrace:
            self.subraces = []


class subrace():
    def __init__(self, name, parent, abilityBonus, featureList):
        setupInputArgs(self,inspect.currentframe())

        self.parent.subraces.append(self)

#class lineage():
def combineRace(inputRace, inputSubrace):
    # Make a shallow copy of the race to avoid modifying the original
    combinedRace = race(
        name=inputRace.name,  # Combine names
        size=inputRace.size,
        speed=inputRace.speed,
        abilityBonus=inputRace.abilityBonus.copy(),
        featureList=inputRace.featureList[:],  
        languages=inputRace.languages[:],      
    )
    
    # Merge ability bonuses from subrace
    for ability, bonus in inputSubrace.abilityBonus.items():
        combinedRace.abilityBonus[ability] = bonus
    

    combinedRace.featureList.extend(inputSubrace.featureList)  # Extend, not append
    
    return combinedRace



class feature():
    def __init__(self, name, source, description, levelsActive = [1], function = None, hasFunction = False, hideFeature = False):
        setupInputArgs(self,inspect.currentframe())
        if self.function is not None:
            self.hasFunction = True

    




#class spell():
#    def __init__(self, name, spellLevel, hasVerbal, hasSomatic, hasMaterial, isRitual ):
        





















class character():
    def __init__(self,name,inputLevel, background, charClass,subclass, race, subrace = None):
        setupInputArgs(self,inspect.currentframe())
        
        self.HD = self.charClass.HD
        
        self.abilities = {
            "Strength": 0,
            "Dexterity": 0,
            "Constitution": 0,
            "Intelligence": 0,
            "Wisdom": 0,
            "Charisma": 0,
        }
        
        self.HP = 0
        self.HPRolls = []
        
        self.level = 0


        # List of features
        self.features = []

        # List of spells. This will be such a headache with spells coming from different sources. Include in class?
        self.spells = []

        # Lists of strings
        self.skillProfs = []
        self.weaponProfs = []
        self.armorProfs = []
        self.toolProfs = []
        self.languages = []

        self.damageResistances = []
        self.damageImmunities = []


        self.toughnessTracker = 0
        



            


        self.rollAbilities()




        if self.race.needsSubrace:
            if self.subrace is None:
                self.subrace = r.choice(self.race.subraces)
            self.race = combineRace(self.race,self.subrace)












        self.applyBackground()
        self.applyRace()

        self.applyClass()


        # Adding all the sundry proficiencies from race, class and background
        for attr in ["armorProfs", "weaponProfs", "toolProfs"]:
            for source in [self.charClass, self.background, self.race]:
                addToList(getattr(self, attr), getattr(source, attr))



        for l in range(self.inputLevel):
            self.attainLevel(l+1)
        
        
        



    
    def attainLevel(self,newLevel):
        self.level = newLevel



        
        if newLevel == 1:
            HPRoll = self.HD
        else:
            HPRoll = r.randint(1,self.HD)
        self.HPRolls.append(HPRoll)

        self.HP += HPRoll + abMod(self.abilities["Constitution"])
        



        for featureSource in [self.race, self.charClass, self.background]:

            for feature in featureSource.featureList:
                if self.level in feature.levelsActive:
                    addToList(self.features,feature)
                    if feature.hasFunction: 
                      feature.function(self)
                      print(f"{feature.name} happened at level {self.level}, HP is {self.HP}")





        self.profBonus = np.ceil(self.level/4) + 1
        self.carryWeight = self.abilities["Strength"]*15
        self.dragWeight = self.abilities["Strength"]*30

    def rollAbilities(self):
        # Define all ability names and remove the preferred one(s)

        nonPreferred = [ability for ability in allAbilities if ability not in self.charClass.abilityPreference]
        
        # Shuffle the non-preferred abilities
        np.random.shuffle(nonPreferred)
        
        # Final order: preferred first, then shuffled non-preferred
        abilitiesInOrder = self.charClass.abilityPreference.copy()
        abilitiesInOrder.extend(nonPreferred)
        
        print(abilitiesInOrder)

        # Roll 6 sets of abilities
        rolledAbilities = []
        for _ in range(6):
            rolls = np.random.randint(1, 7, 4)  # Roll 4d6
            best_three = np.sort(rolls)[1:]  # Drop the lowest
            rolledAbilities.append(sum(best_three))
        
        # Assign rolls to abilities in descending order
        rolledAbilities.sort(reverse=True)
        for ability, value in zip(abilitiesInOrder, rolledAbilities):
            self.abilities[ability] = value
        


    def applyBackground(self):
        for skill in self.background.skillProfs:
            if skill in self.skillProfs:
              1 # Pick another
            else:
                self.skillProfs.append(skill)

        addToList(self.languages,self.background.languages)

    def applyRace(self): # And subrace
        
        # Add race and subrace bonuses to ability scores
        #self.abilities += self.race.abilityBonus

        for ability, bonus in self.race.abilityBonus.items():
           self.abilities[ability] = self.abilities.get(ability) + bonus
        print(self.abilities)
 

        # Get speed
        self.speed = self.race.speed
        
        # Add languages
        addToList(self.languages, self.race.languages)

    



    def applyClass(self):
        availableSkills = self.charClass.classSkills
        for skill in self.skillProfs:
            if skill in availableSkills:
                availableSkills.remove(skill)
        classSkillChoices = arrayChoose(availableSkills,self.charClass.skillsToChoose)
        addToList(self.skillProfs,classSkillChoices)





citySecretsDesc = 'You know the secret patterns and flow to cities and can find passages through the urban sprawl that others would miss. When you are not in combat, you (and companions you lead) can travel between any two locations in the city twice as fast as your speed would normally allow.'
CitySecrets = feature("City Secrets","Background",citySecretsDesc)
Urchin = background("Urchin",["Sleight of Hand","Athletics"],["Disguise kit, Thieves' tools"],[],[CitySecrets])










DarkvisionDesc = 'You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can''t discern color in darkness, only shades of gray.'
Darkvision = feature("Darkvision", "Race", DarkvisionDesc)


DwarvenResilienceDesc = 'You have advantage on saving throws against poison, and you have resistance against poison damage.'
def DwarvenResilienceFunc(character):
    addToList(character.damageResistances,"Poison")

DwarvenResilience = feature("Dwarven Resilience", "Race", DwarvenResilienceDesc, function = DwarvenResilienceFunc)







DwarvenCombatTrainingDesc = 'You have proficiency with the battleaxe, handaxe, light hammer, and warhammer.'
def DwarvenCombatTrainingFunc(character):
    addToList(character.weaponProfs,['Battleaxe', 'Handaxe', 'Light hammer'])
DwarvenCombatTraining = feature("Dwarven Combat Training","Race",DwarvenCombatTrainingDesc, function = DwarvenCombatTrainingFunc) 



ToolProficiencyDwarfDesc = "You gain proficiency with the artisan's tools of your choice: smith's tools, brewer's supplies, or mason's tools."
def ToolProficiencyDwarfFunc(character):
    choice = arrayChoose(["Smith's tools", "Brewer's supplies", "Mason's tools"], 1)
    addToList(character.toolProfs, choice)
ToolProficiencyDwarf = feature('Tool Proficiency', 'Race', ToolProficiencyDwarfDesc, function = ToolProficiencyDwarfFunc) 


StonecunningDesc = "Whenever you make an Intelligence (History) check related to the origin of stonework, you are considered proficient in the History skill and add double your proficiency bonus to the check, instead of your normal proficiency bonus."
Stonecunning = feature("Stonecunning","Race", StonecunningDesc) 







DwarvenToughnessDesc = "Your hit point maximum increases by 1, and it increases by 1 every time you gain a level."
def DwarvenToughnessFunc(character):
    character.HP += 1
    #print(f"it really did occur, HP: {character.HP}")
    character.toughnessTracker += 1
DwarvenToughness = feature("Dwarven Toughness","Subrace",DwarvenToughnessDesc,levelsActive = allLevels, function = DwarvenToughnessFunc)


DwarvenArmorTrainingDesc = "You have proficiency with light and medium armor."
def DwarvenArmorTrainingFunc(character):
    addToList(character.armorProfs,["Light armor, Medium Armor"])
DwarvenArmorTraining = feature("Dwarven Armor Training", "Subrace", DwarvenArmorTrainingDesc,function = DwarvenArmorTrainingFunc)
DwarfFeatureList = [Darkvision, DwarvenResilience, DwarvenCombatTraining, ToolProficiencyDwarf, Stonecunning]


DwarfBonuses = {"Constitution": 2}
Dwarf = race("Dwarf","Medium",25,DwarfBonuses,["Common","Dwarvish"], DwarfFeatureList, needsSubrace=True)



HillDwarfBonuses = {"Wisdom": 1}
HillDwarf = subrace("Hill Dwarf",Dwarf,HillDwarfBonuses,[DwarvenToughness])


MountainDwarfBonuses = {"Strength": 2}
MountainDwarf = subrace("MountainDwarf",Dwarf,MountainDwarfBonuses,[DwarvenArmorTraining])



#Wizard = charClass("Wizard",6,(3,2),(3,2),[],0,[])
Rogue = charClass("Rogue",8,["Dexterity","Wisdom"],["Dexterity", "Intelligence"],["Acrobatics", "Athletics", "Deception", "Insight", "Intimidation", "Investigation", "Perception", "Performance", "Persuasion"],4,[],[],[],[])


ActionSurgeDesc = "On your turn, you can take one additional action. Once you use this feature, you must finish a short or long rest before you can use it again. Starting at 17th level, you can use it twice before a rest, but only once on the same turn."
ActionSurge = feature("Action Surge","Class",ActionSurgeDesc,[1,17])
Fighter = charClass("Fighter",10,["Strength","Constitution"],["Strength","Constitution"],['Acrobatics', 'Animal Handling', 'Athletics', 'History', 'Insight', 'Intimidation', 'Perception', 'Survival'],2,allArmor,simpleWeapons+martialWeapons,[],[])







Owain = character("Owain",5,Urchin,Fighter,"Champion",Dwarf,subrace=HillDwarf)




print(Owain.name)
print(Owain.level)
print(Owain.race.name)
print(Owain.subrace.name)
print(Owain.abilities)
print(Owain.HP)
print(Owain.weaponProfs)


for feature in Owain.features:
  print(feature.name)

print(Owain.toughnessTracker)











