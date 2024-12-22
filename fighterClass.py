from classDefs import *



ASIDesc = "You can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature."

def ASIFunc(character):
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


ASIFighter = feature("ASI","Class",ASIDesc, [4,6,8,12,14,16,19],ASIFunc,hideFeature=True)

ActionSurgeDesc = "On your turn, you can take one additional action. Once you use this feature, you must finish a short or long rest before you can use it again. Starting at 17th level, you can use it twice before a rest, but only once on the same turn."
ActionSurgeShowText1 = "On your turn, you can take one additional action. Once you use this feature, you must finish a short or long rest before you can use it again"
ActionSurgeShowText2 = "On your turn, you can take one additional action. Use twice per short or long rest, but only once on the same turn"

def ActionSurgeFunc(character):
    for feature in character.features:
        if feature.name == "Action Surge" and character.level == 17:
            feature.showText = ActionSurgeShowText2

ActionSurge = feature("Action Surge","Class",ActionSurgeDesc,[1,17],ActionSurgeFunc,showText=ActionSurgeShowText1)



SecondWindDesc = "You have a limited well of stamina that you can draw on to protect yourself from harm. On your turn, you can use a bonus action to regain hit points equal to 1d10 + your fighter level. Once you use this feature, you must finish a short or long rest before you can use it again."
SecondWindShowText1 = "As a bonus action on your turn: Regain HP equal to 1d10 + fighter level. Use once per short or long rest."
def SecondWindFunc(character):
    for feature in character.features:
        if feature.name == "Second Wind" and character.level in allLevels:
            feature.showText =  "As a bonus action on your turn: Regain HP equal to 1d10 + "+ str(int(character.level)) + ". Use once per short or long rest."

SecondWind = feature("Second Wind","Class",SecondWindDesc,allLevels,SecondWindFunc,showText=SecondWindShowText1)

FightingStyleDesc = "You adopt a particular style of fighting as your specialty. Choose one of the following options. You can't take a Fighting Style option more than once, even if you later get to choose again."
FightingStyleShowText = "You have a particular style of fighting as a specialty: "
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
                feature.showText = styles[choice]

FightingStyle = feature("Fighting Style","Class", FightingStyleDesc,1,FightingStyleFunc,showText=FightingStyleShowText)
    

ExtraAttackDesc = "Beginning at 5th level, you can attack twice, instead of once, whenever you take the Attack action on your turn. The number of attacks increases to three when you reach 11th level in this class and to four when you reach 20th level in this class."
ExtraAttackShowText = "You can attack twice instead of once whenever you take the Attack action on your turn."
def ExtraAttackFunc(character):
    for feature in character.features:
        if feature.name == "Extra Attack":
            if character.level == 11:
                feature.showText = "You can attack three times instead of once whenever you take the Attack action on your turn."
            elif character.level == 20:
                feature.showText = "You can attack four times instead of once whenever you take the Attack action on your turn."                
ExtraAttack = feature("Extra Attack","Class",ExtraAttackDesc,[5,11,20],ExtraAttackFunc,showText=ExtraAttackShowText)


IndomitableDesc = "Beginning at 9th level, you can reroll a saving throw that you fail. If you do so, you must use the new roll, and you can't use this feature again until you finish a long rest. You can use this feature twice between long rests starting at 13th level and three times between long rests starting at 17th level."
IndomitableShowText = "Once per long rest you can reroll a saving throw that you fail. If you do so, you must use the new roll."
def IndomitableFunc(character):
    for feature in character.features:
        if feature.name == "Indomitable":
            if character.level == 13:
                feature.showText = "Twice per long rest you can reroll a saving throw that you fail. If you do so, you must use the new roll."
            elif character.level == 17:
                feature.showText = "Three times per long rest you can reroll a saving throw that you fail. If you do so, you must use the new roll."

Indomitable = feature("Indomitable","Class",IndomitableDesc,[9,13,17],function=IndomitableFunc,showText=IndomitableShowText)






Fighter = charClass("Fighter",10,["Strength","Constitution"],["Strength","Constitution"],['Acrobatics', 'Animal Handling', 'Athletics', 'History', 'Insight', 'Intimidation', 'Perception', 'Survival'],2,{"weapon": simpleWeapons+martialWeapons,"armor":allArmor},[FightingStyle,ActionSurge,SecondWind,ASIFighter,ExtraAttack,Indomitable])











#################################################################################
#################################################################################







ImprovedCriticalDesc = "Beginning when you choose this archetype at 3rd level, your weapon attacks score a critical hit on a roll of 19 or 20."
ImprovedCriticalShowText = "Your weapon attacks score a critical hit on a roll of 19 or 20."
ImprovedCritical = feature("Improved Critical","Subclass",ImprovedCriticalDesc,3,showText=ImprovedCriticalShowText)


SuperiorCriticalDesc = "Starting at 15th level, your weapon attacks score a critical hit on a roll of 18-20."
SuperiorCriticalShowText = "Your weapon attacks score a critical hit on a roll of 18-20."
def SuperiorCriticalFunc(character):
    for feature in character.features:
        if feature.name == "Improved Critical":
            feature.hideFeature = True

SuperiorCritical = feature("Superior Critical","Subclass",SuperiorCriticalDesc,15,function = SuperiorCriticalFunc,showText=SuperiorCriticalShowText)


RemarkableAthleteDesc = "Starting at 7th level, you can add half your proficiency bonus (rounded up) to any Strength, Dexterity, or Constitution check you make that doesn't already use your proficiency bonus. In addition, when you make a running long jump, the distance you can cover increases by a number of feet equal to your Strength modifier."
RemarkableAthleteShowText = "Add half your proficiency bonus (rounded up) to any physical check you make that you aren't already proficient in."
def RemarkableAthleteFunc(character):
    # Come back and actually add these numbers to proficiencies and jump distance
    for feature in character.features:
        if feature.name == "Remarkable Athlete" and character.level in range(7,21):
            miniProfBonus = int(np.ceil(character.profBonus/2))
            feature.showText =  "Add " + str(miniProfBonus) + " to any physical check that you aren't already proficient in. Your running long jump distance increases by " + str(abMod(character.abilities["Strength"])) + " feet."
RemarkableAthlete = feature("Remarkable Athlete","Subclass",RemarkableAthleteDesc,list(range(7, 21)),RemarkableAthleteFunc)



SurvivorDesc = "At 18th level, you attain the pinnacle of resilience in battle. At the start of each of your turns, you regain hit points equal to 5 + your Constitution modifier if you have no more than half of your hit points left. You don't gain this benefit if you have 0 hit points."
SurvivorShowText = "At the start of your turn, you regain HP equal to 5 + CON if you have less than half of your total and more than 0."
def SurvivorFunc(character):
    for feature in character.features:
        if feature.name == "Survivor":
            feature.showText =  "At the start of your turn, regain " + str(int(5 + abMod(character.abilities["Strength"]))) +  " HP if you have less than half of your total (" + str(int(np.ceil(character.HP/2))) + ") and more than 0."
Survivor = feature("Survivor","Subclass",SurvivorDesc,list(range(18,21)),function = SurvivorFunc,showText=SurvivorShowText)

Champion = charSubclass("Champion",Fighter,[ImprovedCritical,RemarkableAthlete,SuperiorCritical,Survivor])









BonusProficiencySamuraiDesc = "When you choose this archetype at 3rd level, you gain proficiency in one of the following skills of your choice: History, Insight, Performance, or Persuasion. Alternatively, you learn one language of your choice."
def BonusProficiencySamuraiFunc(character):
    profs = ["History", "Insight", "Performance", "Persuasion"]
    eligibleProfs = [prof for prof in profs if prof not in character.skillProfs]
    if not eligibleProfs:
        eligibleLanguages = [lang for lang in allLanguages if lang not in character.proficiencies["language"]]
        chosenLang = r.choice(eligibleLanguages)
        #character.proficiencies["Language"] = chosenLang
        print(chosenLang)
        character.addProficiency({"language":[chosenLang]})
    else:
        chosenProf = r.choice(eligibleProfs)
        addToList(character.skillProfs,chosenProf)
    print(eligibleProfs)


BonusProficiencySamurai = feature("BonusProficiency","Subclass",BonusProficiencySamuraiDesc,3,BonusProficiencySamuraiFunc,hideFeature=True)

FightingSpiritDesc = "Starting at 3rd level, your intensity in battle can shield you and help you strike true. As a bonus action on your turn, you can give yourself advantage on all weapon attack rolls until the end of the current turn. When you do so, you also gain 5 temporary hit points. The number of hit points increases when you reach certain levels in this class, increasing to 10 at 10th level and 15 at 15th level. You can use this feature three times. You regain all expended uses of it when you finish a long rest."
FightingSpiritShowText = "As a bonus action on your turn, you can give yourself advantage on all weapon attack rolls until the end of your turn. When you do so, you also gain 5 temporary HP. You can use this feature three times per long rest."
def FightingSpiritFunc(character):
    for feature in character.features:
        if feature.name == "FightingSpirit":
            if character.level == 10:
                feature.showText = "As a bonus action on your turn, you can give yourself advantage on all weapon attack rolls until the end of your turn. When you do so, you also gain 10 temporary HP. You can use this feature three times per long rest."
            elif character.level == 15:
                feature.showText = "As a bonus action on your turn, you can give yourself advantage on all weapon attack rolls until the end of your turn. When you do so, you also gain 15 temporary HP. You can use this feature three times per long rest."

FightingSpirit = feature("Fighting Spirit","Subclass",FightingSpiritDesc,[3,10,15],FightingSpiritFunc,showText=FightingSpiritShowText)





ElegantCourtierDesc = "Starting at 7th level, your discipline and attention to detail allow you to excel in social situations. Whenever you make a Charisma (Persuasion) check, you gain a bonus to the check equal to your Wisdom modifier. Your self-control also causes you to gain proficiency in Wisdom saving throws. If you already have this proficiency, you instead gain proficiency in Intelligence or Charisma saving throws (your choice)."
ElegantCourtierShowText = "Whenever you make a Charisma (Persuasion) check, you gain a bonus equal to your Wisdom modifier. You also gain proficiency in Wisdom saving throws. If you already have this proficiency, you instead gain proficiency in Intelligence or Charisma saving throws (your choice)."
def ElegantCourtierFunc(character):
        if "Wisdom" in character.savingThrows:
            eligibleSaves = [save for save in ["Intelligence", "Charisma"] if save not in character.savingThrows]
            chosenSave = r.choice(eligibleSaves)
            character.addToList(character.savingThrows,chosenSave)
        else:
            character.addToList(character.savingThrows,"Wisdom")

ElegantCourtier = feature("Elegant Courtier","Subclass",ElegantCourtierDesc,7,function=ElegantCourtierFunc,showText=ElegantCourtierShowText)



TirelessSpiritDesc = "Starting at 10th level, when you roll initiative and have no uses of Fighting Spirit remaining, you regain one use."
TirelessSpiritShowText = "When you roll initiative and have no uses of Fighting Spirit remaining, you regain one use."
TirelessSpirit = feature("Tireless Spirit","Subclass",TirelessSpiritDesc,10,showText=TirelessSpiritShowText)


RapidStrikeDesc = "Starting at 15th level, you learn to trade accuracy for swift strikes. If you take the Attack action on your turn and have advantage on an attack roll against one of the targets, you can forgo the advantage for that roll to make an additional weapon attack against that target, as part of the same action. You can do so no more than once per turn."
RapidStrikeShowText = "If you take the Attack action on your turn and have advantage on an attack roll against one of the targets, you can forgo the advantage for that roll to make an additional weapon attack against that target, as part of the same action. You can do so no more than once per turn."
RapidStrike = feature("RapidStrike","Subclass",RapidStrikeDesc,15,showText=RapidStrikeShowText)



StrengthBeforeDeathDesc = "Starting at 18th level, your fighting spirit can delay the grasp of death. If you take damage that reduces you to 0 hit points, you can use your reaction to delay falling unconscious, and you can immediately take an extra turn. While you have 0 hit points during that extra turn, taking damage causes death saving throw failures as normal, and three death saving throw failures can still kill you. When the extra turn ends, you fall unconscious if you still have 0 hit points. Once you use this feature, you can’t use it again until you finish a long rest."
StrengthBeforeDeathShowText = "Once per long rest, if you drop to 0 HP, you can use your reaction to immediately take an extra turn, after which you fall unconscious if you're still at 0. Taking damage causes death saving throw failures which can still kill you."
StrengthBeforeDeath = feature("Strength Before Death","Subclass",StrengthBeforeDeathDesc,18,showText=StrengthBeforeDeathShowText)


Samurai = charSubclass("Samurai",Fighter,[BonusProficiencySamurai,FightingSpirit,ElegantCourtier,TirelessSpirit,RapidStrike,StrengthBeforeDeath],["Strength", "Constitution", "Wisdom"])









