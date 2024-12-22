from classDefs import *
from outToPDF import *


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


        self.HP = int(0)
        self.HPRolls = []
        
        self.level = 0


        # List of features
        self.features = []

        # List of spells. This will be such a headache with spells coming from different sources. Include in class?
        self.spells = []

        # Lists of strings
        self.skillProfs = []

        self.proficiencies = {
            "armor": [],
            "weapon": [],
            "tool": [],
            "language": []
        }


        self.savingThrows = []
        self.damageResistances = []
        self.damageImmunities = []


        self.rank = "Senior Officer"   # Set this somehow
        



            


        self.rollAbilities()




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



        
        if newLevel == 1:
            HPRoll = self.HD
        else:
            HPRoll = r.randint(1,self.HD)
        self.HPRolls.append(HPRoll)


        



        for featureSource in [self.race, self.charClass, self.charSubclass, self.background]:
            for feature in featureSource.featureList:
                # Normalize levelsActive to always be a list
                levelsActive = feature.levelsActive if isinstance(feature.levelsActive, list) else [feature.levelsActive]
                
                if self.level in levelsActive:
                    addToList(self.features, feature)
                    if feature.hasFunction: 
                        feature.function(self)

                      #print(f"{feature.name} happened at level {self.level}, HP is {self.HP}")


        self.HP += int(HPRoll + abMod(self.abilities["Constitution"]))


        self.profBonus = int(np.ceil(self.level/4) + 1)
        self.carryWeight = int(self.abilities["Strength"]*15)
        self.dragWeight = int(self.abilities["Strength"]*30)

    def rollAbilities(self):
        # Define all ability names and remove the preferred one(s)

        nonPreferred = [ability for ability in allAbilities if ability not in self.charClass.abilityPreference]
        
        # Shuffle the non-preferred abilities
        np.random.shuffle(nonPreferred)
        
        # Final order: preferred first, then shuffled non-preferred
        abilitiesInOrder = self.charClass.abilityPreference.copy()
        abilitiesInOrder.extend(nonPreferred)
        
        # print(abilitiesInOrder)

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
        





    def addProficiency(self, source_proficiencies):
        for category, items in source_proficiencies.items():
            if category in self.proficiencies:
                # Add only unique items using set difference
                self.proficiencies[category] = list(set(self.proficiencies[category] + items))
            else:
                self.proficiencies[category] = list(set(items))






    def applyBackground(self):
        for skill in self.background.skillProfs:
            if skill in self.skillProfs:
                1 # Pick another from class' favoured skills
                  # If you've got all your class' favoured skills somehow, pick at random from what remains
            else:
                addToList(self.skillProfs,skill)

        self.addProficiency(self.background.proficiencies)
        #addToList(self.proficiencies,self.background.proficiencies)

    def applyRace(self): # And subrace
        
        # Add race and subrace bonuses to ability scores
        #self.abilities += self.race.abilityBonus

        for ability, bonus in self.race.abilityBonus.items():
           self.abilities[ability] = self.abilities.get(ability) + bonus
        
        
        # print(self.abilities)
 

        # Get speed
        self.speed = self.race.speed
        self.size = self.race.size
        
        # Add proficiencies
        self.addProficiency(self.race.proficiencies)
        #addToList(self.proficiencies, self.race.proficiencies)

    



    def applyClass(self):
        availableSkills = self.charClass.classSkills
        for skill in self.skillProfs:
            if skill in availableSkills:
                availableSkills.remove(skill)
        classSkillChoices = arrayChoose(availableSkills,self.charClass.skillsToChoose)
        addToList(self.skillProfs,classSkillChoices)
    
        # Add proficiencies

        self.addProficiency(self.charClass.proficiencies)

        addToList(self.savingThrows,self.charClass.saveProfs)

    def exportCharacter(self):
        printCharSheet(self)
