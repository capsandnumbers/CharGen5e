#FighterClass

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

ManeuverCodex = { 
    # Update these with functions one day
    "Commander's Strike": "When you take the Attack action on your turn, you can forgo one of your attacks and use a bonus action to direct one of your companions to strike. When you do so, choose a friendly creature who can see or hear you and expend one superiority die. That creature can immediately use its reaction to make one weapon attack, adding the superiority die to the attack's damage roll.",
    "Disarming Attack": "When you hit a creature with a weapon attack, you can expend one superiority die to attempt to disarm the target, forcing it to drop one item of your choice that it's holding. You add the superiority die to the attack's damage roll, and the target must make a Strength saving throw. On a failed save, it drops the object you choose. The object lands at its feet.",
    "Distracting Strike": "When you hit a creature with a weapon attack, you can expend one superiority die to distract the creature, giving your allies an opening. You add the superiority die to the attack's damage roll. The next attack roll against the target by an attacker other than you has advantage if the attack is made before the start of your next turn.",
    "Evasive Footwork": "When you move, you can expend one superiority die, rolling the die and adding the number rolled to your AC until you stop moving.",
    "Feinting Attack": "You can expend one superiority die and use a bonus action on your turn to feint, choosing one creature within 5 feet of you as your target. You have advantage on your next attack roll against that creature this turn. If that attack hits, add the superiority die to the attack's damage roll.",
    "Goading Attack": "When you hit a creature with a weapon attack, you can expend one superiority die to attempt to goad the target into attacking you. You add the superiority die to the attack's damage roll, and the target must make a Wisdom saving throw. On a failed save, the target has disadvantage on all attack rolls against targets other than you until the end of your next turn.",
    "Lunging Attack": "When you make a melee weapon attack on your turn, you can expend one superiority die to increase your reach for that attack by 5 feet. If you hit, you add the superiority die to the attack's damage roll.",
    "Maneuvering Attack": "When you hit a creature with a weapon attack, you can expend one superiority die to maneuver one of your comrades into a more advantageous position. You add the superiority die to the attack's damage roll, and you choose a friendly creature who can see or hear you. That creature can use its reaction to move up to half its speed without provoking opportunity attacks from the target of your attack.",
    "Menacing Attack": "When you hit a creature with a weapon attack, you can expend one superiority die to attempt to frighten the target. You add the superiority die to the attack's damage roll, and the target must make a Wisdom saving throw. On a failed save, it is frightened of you until the end of your next turn.",
    "Parry": "When another creature damages you with a melee attack, you can use your reaction and expend one superiority die to reduce the damage by the number you roll on your superiority die + your Dexterity modifier.",
    "Precision Attack": "When you make a weapon attack roll against a creature, you can expend one superiority die to add it to the roll. You can use this maneuver before or after making the attack roll, but before any effects of the attack are applied.",
    "Pushing Attack": "When you hit a creature with a weapon attack, you can expend one superiority die to attempt to drive the target back. You add the superiority die to the attack's damage roll, and if the target is Large or smaller, it must make a Strength saving throw. On a failed save, you push the target up to 15 feet away from you.",
    "Rally": "On your turn, you can use a bonus action and expend one superiority die to bolster the resolve of one of your companions. When you do so, choose a friendly creature who can see or hear you. That creature gains temporary hit points equal to the superiority die roll + your Charisma modifier.",
    "Riposte": "When a creature misses you with a melee attack, you can use your reaction and expend one superiority die to make a melee weapon attack against the creature. If you hit, you add the superiority die to the attack's damage roll.",
    "Sweeping Attack": "When you hit a creature with a melee weapon attack, you can expend one superiority die to attempt to damage another creature with the same attack. Choose another creature within 5 feet of the original target and within your reach. If the original attack roll would hit the second creature, it takes damage equal to the number you roll on your superiority die. The damage is of the same type dealt by the original attack.",
    "Trip Attack": "When you hit a creature with a weapon attack, you can expend one superiority die to attempt to knock the target down. You add the superiority die to the attack's damage roll, and if the target is Large or smaller, it must make a Strength saving throw. On a failed save, you knock the target prone."
}
    

    
CombatSuperiorityDesc = ""
CombatSuperiorityShowText = ""
def addManeuver(character,number):
    eligibleManeuvers = [maneuver for maneuver, manDesc in ManeuverCodex if maneuver not in character.maneuvers]
    chosenManeuvers = r.sample(eligibleManeuvers,number)
    addToList(character.maneuvers,chosenManeuvers)

def CombatSuperiorityFunc(character):
    setattr(character, "maneuvers", [])
    setattr(character, "supDiceNumber", 4)
    setattr(character, "supDiceSize", 8)
    setattr(character, "maneuverDC",8)
    if character.level == 3:
        addManeuver(character,3)         # Learn 3 maneuvers
        character.supDiceNumber = 4      # get 4 superiority dice
    elif character.level == 7:
        addManeuver(character,2)         # Learn 2 maneuvers
        character.supDiceNumber = 5      # Get superiority die 
    elif character.level == 10:
        addManeuver(character,2)         # Learn 2 maneuvers
        character.supDiceSize = 10       # Increase die size
    elif character.level == 15:
        addManeuver(character,2)         # Learn 2 maneuvers
        character.supDice = 5            # Get superiority die
    elif character.level == 18:
        character.supDiceSize = 12       # Increase die size
    #Update maneuver save DC:
    character.maneuverDC = 8+max(character.abilities["Strength"],character.abilities["Dexterity"])

    CombatSuperiorityShowDesc = "Superiority Dice: " + str(character.supDiceNumber) + "d" + str(character.supDiceSize) +", save DC: " + str(character.maneuverDC)
    for maneuver in character.maneuvers:
        CombatSuperiorityShowDesc = CombatSuperiorityShowDesc + "\n" + maneuver + ": " + ManeuverCodex[maneuver]

    for feature in character.features:
        if feature.name == "Combat Superiority":
            feature.showText = CombatSuperiorityShowDesc

CombatSuperiority = feature("Combat Superiority", "Subclass", CombatSuperiorityDesc,levelsActive = list(range(3,21)), showText = CombatSuperiorityShowText, function = CombatSuperiorityFunc)



StudentOfWarDesc = "At 3rd level, you gain proficiency with one type of artisan's tools of your choice."
def StudentOfWarFunc(character):
    eligibleTools = [tool for tool in ArtisansTools if tool not in character.proficiencies["tool"]]
    chosenTool = r.sample(eligibleTools,1)
    character.addProficiency({"tool":chosenTool})

StudentOfWar = function("Student of War","Subclass",StudentOfWarDesc,levelsActive = 3,function= StudentOfWarFunc, hideFeature = True)


KnowYourEnemyDesc = "Starting at 7th level, if you spend at least 1 minute observing or interacting with another creature outside combat, you can learn certain information about its capabilities compared to your own. The DM tells you if the creature is your equal, superior, or inferior in regard to two of the following characteristics of your choice: Strength score, Dexterity score, Constitution score, Armor Class, Current hit points, Total class levels, Fighter class levels"
KnowYourEnemyShowText = "If you spend at least 1 minute with another creature outside combat, you learn how it relates to you in regard to two of the following characteristics of your choice: Strength, Dexterity, Constitution, AC, Current HP, Total class levels, Fighter class levels."
KnowYourEnemy = feature("Know Your Enemy", "Subclass",KnowYourEnemyDesc,7,showText = KnowYourEnemyShowText)

RelentlessDesc = "Starting at 15th level, when you roll initiative and have no superiority dice remaining, you regain 1 superiority die."
RelentlessShowText = "When you roll initiative and have no superiority dice remaining, you regain 1 die."
Relentless = feature("Relentless","Subclass",RelentlessDesc,15,showText = RelentlessShowText)

BattleMaster = subclass("Battle Master",Fighter,[CombatSuperiority,StudentOfWar,KnowYourEnemy,Relentless])






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
    eligibleProfs = [prof for prof in profs if prof not in character.proficiencies["skill"]]
    if not eligibleProfs:
        eligibleLanguages = [lang for lang in allLanguages if lang not in character.proficiencies["language"]]
        chosenLang = r.choice(eligibleLanguages)
        #character.proficiencies["Language"] = chosenLang
        #print(chosenLang)
        character.addProficiency({"language":[chosenLang]})
    else:
        chosenProf = r.choice(eligibleProfs)
        character.addProficiency({"skill":[chosenProf]})
        #addToList(character.skillProfs,chosenProf)


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
ElegantCourtierShowText = "Whenever you make a Persuasion check, you gain a bonus equal to your Wisdom modifier."
def ElegantCourtierFunc(character):
        if "Wisdom" in character.savingThrows:
            eligibleSaves = [save for save in ["Intelligence", "Charisma"] if save not in character.savingThrows]
            chosenSave = r.choice(eligibleSaves)
            addToList(character.savingThrows,chosenSave)
        else:
            addToList(character.savingThrows,"Wisdom")

ElegantCourtier = feature("Elegant Courtier","Subclass",ElegantCourtierDesc,7,function=ElegantCourtierFunc,showText=ElegantCourtierShowText)



TirelessSpiritDesc = "Starting at 10th level, when you roll initiative and have no uses of Fighting Spirit remaining, you regain one use."
TirelessSpiritShowText = "When you roll initiative and have no uses of Fighting Spirit remaining, you regain one use."
TirelessSpirit = feature("Tireless Spirit","Subclass",TirelessSpiritDesc,10,showText=TirelessSpiritShowText)


RapidStrikeDesc = "Starting at 15th level, you learn to trade accuracy for swift strikes. If you take the Attack action on your turn and have advantage on an attack roll against one of the targets, you can forgo the advantage for that roll to make an additional weapon attack against that target, as part of the same action. You can do so no more than once per turn."
RapidStrikeShowText = "If you take the Attack action on your turn and have advantage on an attack roll against one of the targets, you can forgo the advantage for that roll to make an additional weapon attack against that target, as part of the same action. You can do so no more than once per turn."
RapidStrike = feature("Rapid Strike","Subclass",RapidStrikeDesc,15,showText=RapidStrikeShowText)



StrengthBeforeDeathDesc = "Starting at 18th level, your fighting spirit can delay the grasp of death. If you take damage that reduces you to 0 hit points, you can use your reaction to delay falling unconscious, and you can immediately take an extra turn. While you have 0 hit points during that extra turn, taking damage causes death saving throw failures as normal, and three death saving throw failures can still kill you. When the extra turn ends, you fall unconscious if you still have 0 hit points. Once you use this feature, you can’t use it again until you finish a long rest."
StrengthBeforeDeathShowText = "Once per long rest, if you drop to 0 HP, you can use your reaction to immediately take an extra turn, after which you fall unconscious if you're still at 0. Taking damage causes death saving throw failures which can still kill you."
StrengthBeforeDeath = feature("Strength Before Death","Subclass",StrengthBeforeDeathDesc,18,showText=StrengthBeforeDeathShowText)


Samurai = charSubclass("Samurai",Fighter,[BonusProficiencySamurai,FightingSpirit,ElegantCourtier,TirelessSpirit,RapidStrike,StrengthBeforeDeath],["Strength", "Constitution", "Wisdom"])
