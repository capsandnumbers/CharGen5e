# Character

from CharGen5e.classDefs import *
from CharGen5e.outToPDF import *

def ACDefaultFunc(self):
    return 10 + self.abilities["Dexterity"]


class character():
    def __init__(self,name,inputLevel, background, charClass,charSubclass, race, subrace = None):
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
        
        self.abilityMods = {
            "Strength": 0,
            "Dexterity": 0,
            "Constitution": 0,
            "Intelligence": 0,
            "Wisdom": 0,
            "Charisma": 0,
        }

        self.spellDict = {} # Records list of spells with relevant spellcasting ability

        self.HP = int(0)
        self.HPRolls = []
        self.profMod = 2
        self.level = 0


        # List of features
        self.features = []

        # Dictionary for all proficiencies
        self.proficiencies = {
            "skill": [],
            "armor": [],
            "weapon": [],
            "tool": [],
            "language": []
        }

        self.equipment = {
            "armor": "None",
            "mainhand": "None",
            "offhand": "None",
        }

        self.savingThrows = []
        self.damageResistances = []
        self.damageImmunities = []

        self.skillMods = {
            "Acrobatics": 0,
            "Animal Handling": 0,
            "Arcana": 0,
            "Athletics": 0,
            "Deception": 0,
            "History": 0,
            "Insight": 0,
            "Intimidation": 0,
            "Investigation": 0,
            "Medicine": 0,
            "Nature": 0,
            "Perception": 0,
            "Performance": 0,
            "Persuasion": 0,
            "Religion": 0,
            "Sleight of Hand": 0,
            "Stealth": 0,
            "Survival":0
        }


        self.rank = "Senior Officer"   # Set this somehow
        



            


        self.rollAbilities()
        self.updateAbilityMods()

        self.longJumpDistance = self.abilities["Strength"]
        self.highJumpDistance = 3 + self.abilityMods["Strength"]



        self.equippedArmor = "None"
        self.equippedHand2 = "None"

        self.ACFunc = ACDefaultFunc
        self.updateAC()        
        

        if self.race.needsSubrace:
            if self.subrace is None:
                self.subrace = r.choice(self.race.subraces)
            self.race = combineRace(self.race,self.subrace)












        self.applyBackground()
        self.applyRace()

        self.applyClass()



        for l in range(self.inputLevel):
            self.attainLevel(l+1)




    def attainLevel(self,newLevel,verbose = False):
        self.level = newLevel
        if verbose:
            print(self.name + " is now level " + str(self.level))



        HPRoll = r.randint(1,self.HD)        
        
        if newLevel == 1:
            self.HPRolls.append(self.HD)
        else:
            self.HPRolls.append(HPRoll)


        
        



        for featureSource in [self.race, self.charClass, self.charSubclass, self.background]:
            for feature in featureSource.featureList:
                # Normalize levelsActive to always be a list
                levelsActive = feature.levelsActive if isinstance(feature.levelsActive, list) else [feature.levelsActive]
                
                if self.level in levelsActive:
                    addToList(self.features, feature)
                    if feature.function is not None: 
                        feature.function(self)





        self.performUpdates()


    def rollAbilities(self):
        # Define all ability names and remove the preferred one(s)

        nonPreferred = [ability for ability in allAbilities if ability not in self.charClass.abilityPreference]
        
        # Shuffle the non-preferred abilities
        np.random.shuffle(nonPreferred)
        
        # Final order: preferred first, then shuffled non-preferred
        abilitiesInOrder = self.charClass.abilityPreference.copy()
        abilitiesInOrder.extend(nonPreferred)
        
        # Roll 6 sets of abilities
        rolledAbilities = []
        for _ in range(6):
            rolls = np.random.randint(1, 7, 4)  # Roll 4d6
            best_three = np.sort(rolls)[1:]  # Drop the lowest
            rolledAbilities.append(sum(best_three))
        
        # Assign rolls to abilities in descending order
        rolledAbilities.sort(reverse=True)
        for ability, value in zip(abilitiesInOrder, rolledAbilities):
            self.abilities[ability] = int(value)
        

    def updateAC(self):
        self.AC = self.ACFunc(self)



    def addProficiency(self, source_proficiencies):
        for category, items in source_proficiencies.items():
            if category in self.proficiencies:
                # Add only unique items using set difference
                self.proficiencies[category] = list(set(self.proficiencies[category] + items))
            else:
                self.proficiencies[category] = list(set(items))

    def addProfFromList(self,listToChooseFrom,profCategory,numberToChoose = 1):
        eligibleProfs = [prof for prof in listToChooseFrom if prof not in self.proficiencies[profCategory]]
        chosenProfs = r.sample(eligibleProfs,numberToChoose)
        self.addProficiency({profCategory:chosenProfs})


    def handleOptionalProfs(self, source):
        if source.optionalProfs:
            for entry in source.optionalProfs:
                array = entry[0]
                category = entry[1]
                number = entry[2]
                self.addProfFromList(array, category, number)


    def applyBackground(self):


        self.addProficiency(self.background.proficiencies)
        self.handleOptionalProfs(self.background)

    def applyRace(self): # And subrace
        
        # Add race and subrace bonuses to ability scores
        for ability, bonus in self.race.abilityBonus.items():
           self.abilities[ability] = self.abilities.get(ability) + bonus
        
        

        # Get speed and size
        self.speed = self.race.speed
        self.size = self.race.size
        
        # Add proficiencies
        self.addProficiency(self.race.proficiencies)
        self.handleOptionalProfs(self.race)
        
    



    def applyClass(self):



        eligibleSkills = [skill for skill in self.charClass.classSkills if skill not in self.proficiencies["skill"]]

        # Separate skills into "good" and "bad" based on positive ability modifiers
        goodSkills = [skill for skill in eligibleSkills if self.abilityMods[allSkills[skill]] > 0]
        #print(goodSkills, self.abilityMods)
        badSkills = [skill for skill in eligibleSkills if skill not in goodSkills]
        #print(badSkills)
        # Choose as many good skills as possible, up to the required number
        choices = []
        if len(goodSkills) >= self.charClass.skillsToChoose:
            choices = r.sample(goodSkills, self.charClass.skillsToChoose)
        else:
            # Add all good skills and fill the rest from bad skills
            choices.extend(goodSkills)
            remainingToChoose = self.charClass.skillsToChoose - len(goodSkills)
            choices.extend(r.sample(badSkills, remainingToChoose))

        # Add selected skills to proficiencies
        self.addProficiency({"skill":choices})



        # Add proficiencies
        self.addProficiency(self.charClass.proficiencies)
        self.handleOptionalProfs(self.charClass)

        addToList(self.savingThrows,self.charClass.saveProfs)


    def featureSort(self):




        source_order = {
            "Race": 0,
            "Subrace": 1,
            "Background": 2,
            "Class": 3,
            "Subclass": 3
        }
        # Sort Race, Subrace, Background features alphabetically
        sortedFeatures = sorted(
            self.features,
            key=lambda feature: (
                source_order[feature.source],  # Primary: Source order
                feature.levelObtained if feature.source in {"Class", "Subclass"} else 0,  # Secondary: Level for Class/Subclass
                feature.name  # Tertiary: Alphabetical order for all
            )
        )
        self.features = sortedFeatures

    def listFeatures(self):
        for feature in self.features:
            if not feature.hideFeature:
                print(feature.name)
                print(feature.getText(self))

    def updateAbilityMods(self):
        for ability in self.abilityMods:
            self.abilityMods[ability] = abMod(self.abilities[ability])

    def updateSkillMods(self):
        for skill in self.skillMods:
            governingAbility = allSkills[skill]
            governingAbilityMod = self.abilityMods[governingAbility]
            skillMod = governingAbilityMod
            if skill in self.proficiencies["skill"]:
                skillMod += self.profMod
            self.skillMods[skill] = skillMod

    def updateHP(self):
        self.HP = int(sum(self.HPRolls) + self.level*self.abilityMods["Constitution"])
    
    def performFeatureCallbacks(self):
        for feature in (f for f in self.features if f.hasCallback):
        
            feature.callback(self)



    def setUpCasting(self,casterAbility):
        self.casterAbility = casterAbility
        self.spellList = wizardSpellList


    def performUpdates(self):
        self.updateAbilityMods()
        self.updateSkillMods()
        self.updateHP()
        self.profBonus = int(np.ceil(self.level/4) + 1)
        self.carryWeight = int(self.abilities["Strength"]*15)
        self.dragWeight = int(self.abilities["Strength"]*30)

        self.performFeatureCallbacks()


    def exportCharacter(self):
        printCharSheet(self)
