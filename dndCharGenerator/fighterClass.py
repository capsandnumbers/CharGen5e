#FighterClass

from dndCharGenerator.classDefs import *



ASIDesc = "You can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature."

def ASIFunc(character):

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

            # Print for debugging purposes
            #print(f"{chosenAbility} is now {character.abilities[chosenAbility]}")


ASIFighter = feature("ASI","Class",ASIDesc, allLevels,ASIFunc,hideFeature=True)

ActionSurgeDesc = "On your turn, you can take one additional action. Once you use this feature, you must finish a short or long rest before you can use it again. Starting at 17th level, you can use it twice before a rest, but only once on the same turn."

ActionSurgeSchedule = {
    17: "On your turn, you can take one additional action. Use twice per rest, but only once per turn",
    1: "On your turn, you can take one additional action. Use once per rest"
}

ActionSurge = feature("Action Surge","Class",ActionSurgeDesc,[1,17],textFunc=stagedUpdate(ActionSurgeSchedule))



SecondWindDesc = "You have a limited well of stamina that you can draw on to protect yourself from harm. On your turn, you can use a bonus action to regain hit points equal to 1d10 + your fighter level. Once you use this feature, you must finish a short or long rest before you can use it again."
SecondWindText = "As a bonus action on your turn: Regain HP equal to 1d10 + {level}. Use once per rest."

SecondWind = feature("Second Wind","Class",SecondWindDesc,allLevels,text=SecondWindText)

FightingStyleDesc = "You adopt a particular style of fighting as your specialty. Choose one of the following options. You can't take a Fighting Style option more than once, even if you later get to choose again."
FightingStyleText = "You have a particular style of fighting as a specialty: "
def FightingStyleFunc(character):




    styles = {
        '1': "Archery: You gain a +2 bonus to attack rolls you make with ranged weapons.",
        '2': "Defense: While you are wearing armor, you gain a +1 bonus to AC.",
        '3': "Dueling: When you are wielding a melee weapon in one hand and no other weapons, you gain a +2 bonus to damage rolls with that weapon.",
        '4': "Great Weapon Fighting: When you roll a 1 or 2 on a damage die for an attack you make with a melee weapon that you are wielding with two hands, you can reroll the die and must use the new roll, even if the new roll is a 1 or a 2. The weapon must have the two-handed or versatile property for you to gain this benefit.",
        '5': "Protection: When a creature you can see attacks a target other than you that is within 5 feet of you, you can use your reaction to impose disadvantage on the attack roll. You must be wielding a shield.",
        '6': "Two-Weapon Fighting: When you engage in two-weapon fighting, you can add your ability modifier to the damage of the second attack."
    }


    for feature in character.features:
        if feature.name == "Fighting Style":
            choice = str(r.randint(1, len(styles)))


            if choice in styles:
                feature.text = styles[choice]

FightingStyle = feature("Fighting Style","Class", FightingStyleDesc,1,FightingStyleFunc,text=FightingStyleText)
    

ExtraAttackDesc = "Beginning at 5th level, you can attack twice, instead of once, whenever you take the Attack action on your turn. The number of attacks increases to three when you reach 11th level in this class and to four when you reach 20th level in this class."
ExtraAttackText = "You can attack twice instead of once whenever you take the Attack action on your turn."

ExtraAttackSchedule = {
    20: "You can attack four times instead of once whenever you take the Attack action on your turn.",
    11: "You can attack three times instead of once whenever you take the Attack action on your turn.",
    5: "You can attack twice instead of once whenever you take the Attack action on your turn."
}


ExtraAttack = feature("Extra Attack","Class",ExtraAttackDesc,[5,11,20],textFunc=stagedUpdate(ExtraAttackSchedule),text=ExtraAttackText)


IndomitableDesc = "Beginning at 9th level, you can reroll a saving throw that you fail. If you do so, you must use the new roll, and you can't use this feature again until you finish a long rest. You can use this feature twice between long rests starting at 13th level and three times between long rests starting at 17th level."
IndomitableText = "Once per long rest you can reroll a saving throw that you fail. You must use the new roll."


IndomitableSchedule = {
    17: "Three times per long rest you can reroll a saving throw that you fail. You must use the new roll.",
    13: "Twice per long rest you can reroll a saving throw that you fail. You must use the new roll.",
    9: "Once per long rest you can reroll a saving throw that you fail. You must use the new roll."
}

Indomitable = feature("Indomitable","Class",IndomitableDesc,9,textFunc=stagedUpdate(IndomitableSchedule),text=IndomitableText)






Fighter = charClass("Fighter",10,["Strength","Constitution"],["Strength","Constitution"],['Acrobatics', 'Animal Handling', 'Athletics', 'History', 'Insight', 'Intimidation', 'Perception', 'Survival'],2,{"weapon": simpleWeapons+martialWeapons,"armor":allArmor},[FightingStyle,ActionSurge,SecondWind,ASIFighter,ExtraAttack,Indomitable],ASISchedules["Fighter"])








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








#################################################################################
#################################################################################
