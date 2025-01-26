from CharGen5e.classDefs import *
from CharGen5e.Sources.SRD.Classes.fighterClass import *




ImprovedCriticalDesc = "Beginning when you choose this archetype at 3rd level, your weapon attacks score a critical hit on a roll of 19 or 20."
ImprovedCriticalText = "Your weapon attacks score a critical hit on a roll of 19 or 20."
ImprovedCritical = feature("Improved Critical","Subclass",ImprovedCriticalDesc,3,text=ImprovedCriticalText)


SuperiorCriticalDesc = "Starting at 15th level, your weapon attacks score a critical hit on a roll of 18-20."
SuperiorCriticalText = "Your weapon attacks score a critical hit on a roll of 18-20."
def SuperiorCriticalFunc(character):
    for feature in character.features:
        if feature.name == "Improved Critical":
            feature.hideFeature = True

SuperiorCritical = feature("Superior Critical","Subclass",SuperiorCriticalDesc,15,function = SuperiorCriticalFunc,text=SuperiorCriticalText)


RemarkableAthleteDesc = "Starting at 7th level, you can add half your proficiency bonus (rounded up) to any Strength, Dexterity, or Constitution check you make that doesn't already use your proficiency bonus. In addition, when you make a running long jump, the distance you can cover increases by a number of feet equal to your Strength modifier."
RemarkableAthleteText = "Add half your proficiency bonus (rounded up) to any physical check you make that you aren't already proficient in."
def RemarkableAthleteFunc(character):
    # Come back and actually add these numbers to proficiencies and jump distance
    for feature in character.features:
        if feature.name == "Remarkable Athlete" and character.level in range(7,21):
            miniProfBonus = int(np.ceil(character.profBonus/2))
            feature.text =  "Add " + str(miniProfBonus) + " to any physical check that you aren't already proficient in. Your running long jump distance increases by " + str(abMod(character.abilities["Strength"])) + " feet."
RemarkableAthlete = feature("Remarkable Athlete","Subclass",RemarkableAthleteDesc,list(range(7, 21)),RemarkableAthleteFunc,text=RemarkableAthleteText)



SurvivorDesc = "At 18th level, you attain the pinnacle of resilience in battle. At the start of each of your turns, you regain hit points equal to 5 + your Constitution modifier if you have no more than half of your hit points left. You don't gain this benefit if you have 0 hit points."
SurvivorText = "At the start of your turn, you regain HP equal to your Con mod + 5 if you have less than half of your total and more than 0."

def SurvivorTextFunc(character):
    return "At the start of your turn, regain " + str(int(5 + character.abilityMods["Constitution"])) +  " HP if you have less than half of your total (" + str(int(np.floor(character.HP/2))) + ") and more than 0."
Survivor = feature("Survivor","Subclass",SurvivorDesc,list(range(18,21)),textFunc = SurvivorTextFunc,text=SurvivorText)

Champion = charSubclass("Champion",Fighter,[ImprovedCritical,RemarkableAthlete,SuperiorCritical,Survivor])



