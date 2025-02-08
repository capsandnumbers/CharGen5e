from CharGen5e.classDefs import *
from CharGen5e.Sources.SRD.Classes.fighterClass import *




ImprovedCriticalDesc = "Beginning when you choose this archetype at 3rd level, your weapon attacks score a critical hit on a roll of 19 or 20."
ImprovedCriticalText = "Your weapon attacks score a critical hit on a roll of 19 or 20."
ImprovedCritical = feature("Improved Critical","Subclass",ImprovedCriticalDesc,ImprovedCriticalText,3)


SuperiorCriticalDesc = "Starting at 15th level, your weapon attacks score a critical hit on a roll of 18-20."
SuperiorCriticalText = "Your weapon attacks score a critical hit on a roll of 18-20."
SuperiorCritical = feature("Superior Critical","Subclass",SuperiorCriticalDesc,SuperiorCriticalText,15,replaces= ImprovedCritical)


RemarkableAthleteDesc = "Starting at 7th level, you can add half your proficiency bonus (rounded up) to any Strength, Dexterity, or Constitution check you make that doesn't already use your proficiency bonus. In addition, when you make a running long jump, the distance you can cover increases by a number of feet equal to your Strength modifier."
RemarkableAthleteText = "Add half your proficiency bonus (rounded up) to any physical check you make that you aren't already proficient in."


def RemarkableAthleteTextFunc(character):
    # Come back and actually add these numbers to proficiencies and jump distance
        miniProfBonus = str(int(np.ceil(character.profBonus/2)))
        return "Add " + miniProfBonus + " to any physical check that you aren't already proficient in. Your running long jump distance increases by " + str(character.abilityMods["Strength"]) + " feet."

def RemarkableAthleteCallback(character):
    
    character.longJumpDistance = character.abilities["Strength"] + character.abilityMods["Strength"]


    character.initMod = character.abilityMods["Dexterity"] 

    physicalChecks = [skill for skill, ability in allSkills.items() if ability in ["Strength", "Dexterity", "Constitution"]]
    for skill, mod in character.skillMods.items():
         if skill in physicalChecks and skill not in character.proficiencies["skill"]:
              character.skillMods[skill] = mod + int(np.ceil(character.profBonus/2))





RemarkableAthlete = feature("Remarkable Athlete","Subclass",RemarkableAthleteDesc,RemarkableAthleteText,7,textFunc = RemarkableAthleteTextFunc, callback=RemarkableAthleteCallback)



SurvivorDesc = "At 18th level, you attain the pinnacle of resilience in battle. At the start of each of your turns, you regain hit points equal to 5 + your Constitution modifier if you have no more than half of your hit points left. You don't gain this benefit if you have 0 hit points."
SurvivorText = "At the start of your turn, you regain HP equal to your Con mod + 5 if you have less than half of your total and more than 0."

def SurvivorTextFunc(character):
    return "At the start of your turn, regain " + str(int(5 + character.abilityMods["Constitution"])) +  " HP if you're on less than half, (" + str(int(np.ceil(character.HP/2))) + ") and more than 0."
Survivor = feature("Survivor","Subclass",SurvivorDesc,SurvivorText,18,textFunc = SurvivorTextFunc)

Champion = charSubclass("Champion",Fighter,[ImprovedCritical,RemarkableAthlete,SuperiorCritical,Survivor])
