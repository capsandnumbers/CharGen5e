#FighterClass

from dndCharGenerator.classDefs import *
from dndCharGenerator.fighterClass import *



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
CombatSuperiorityText = ""
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
            feature.text = CombatSuperiorityShowDesc

CombatSuperiority = feature("Combat Superiority", "Subclass", CombatSuperiorityDesc,levelsActive = list(range(3,21)), text = CombatSuperiorityText, function = CombatSuperiorityFunc)



StudentOfWarDesc = "At 3rd level, you gain proficiency with one type of artisan's tools of your choice."
def StudentOfWarFunc(character):
    character.addProfFromList(artisansTools,"tool",1)

StudentOfWar = feature("Student of War","Subclass",StudentOfWarDesc,levelsActive = 3,function= StudentOfWarFunc, hideFeature = True)


KnowYourEnemyDesc = "Starting at 7th level, if you spend at least 1 minute observing or interacting with another creature outside combat, you can learn certain information about its capabilities compared to your own. The DM tells you if the creature is your equal, superior, or inferior in regard to two of the following characteristics of your choice: Strength score, Dexterity score, Constitution score, Armor Class, Current hit points, Total class levels, Fighter class levels"
KnowYourEnemyText = "If you spend at least 1 minute with another creature outside combat, you learn how it relates to you in regard to two of the following characteristics of your choice: Strength, Dexterity, Constitution, AC, Current HP, Total class levels, Fighter class levels."
KnowYourEnemy = feature("Know Your Enemy", "Subclass",KnowYourEnemyDesc,7,text = KnowYourEnemyText)

RelentlessDesc = "Starting at 15th level, when you roll initiative and have no superiority dice remaining, you regain 1 superiority die."
RelentlessText = "When you roll initiative and have no superiority dice remaining, you regain 1 die."
Relentless = feature("Relentless","Subclass",RelentlessDesc,15,text = RelentlessText)

BattleMaster = charSubclass("Battle Master",Fighter,[CombatSuperiority,StudentOfWar,KnowYourEnemy,Relentless])






#def SpellcastingEKnightFunc(character):
#    character.setUpCasting("Intelligence")



#SpellcastingEKnight = feature("Spellcasting","Class",)




#EldritchKnight = charSubclass("EldritchKnight",Fighter,[])















BonusProficiencySamuraiDesc = "When you choose this archetype at 3rd level, you gain proficiency in one of the following skills of your choice: History, Insight, Performance, or Persuasion. Alternatively, you learn one language of your choice."
def BonusProficiencySamuraiFunc(character):
    profs = ["History", "Insight", "Performance", "Persuasion"]
    eligibleProfs = [prof for prof in profs if prof not in character.proficiencies["skill"]]
    if not eligibleProfs:
        eligibleLanguages = [lang for lang in allLanguages if lang not in character.proficiencies["language"]]
        chosenLang = r.choice(eligibleLanguages)


        character.addProficiency({"language":[chosenLang]})
    else:
        chosenProf = r.choice(eligibleProfs)
        character.addProficiency({"skill":[chosenProf]})


BonusProficiencySamurai = feature("BonusProficiency","Subclass",BonusProficiencySamuraiDesc,3,BonusProficiencySamuraiFunc,hideFeature=True)




FightingSpiritDesc = "Starting at 3rd level, your intensity in battle can shield you and help you strike true. As a bonus action on your turn, you can give yourself advantage on all weapon attack rolls until the end of the current turn. When you do so, you also gain 5 temporary hit points. The number of hit points increases when you reach certain levels in this class, increasing to 10 at 10th level and 15 at 15th level. You can use this feature three times. You regain all expended uses of it when you finish a long rest."
FightingSpiritText = "As a bonus action on your turn, get advantage on weapon attacks for the turn, and gain 5 temporary HP. Three times per long rest."
FightingSpiritSchedule = {
    15: "As a bonus action on your turn, get advantage on weapon attacks for the turn, and gain 15 temporary HP. Three times per long rest.",
    10: "As a bonus action on your turn, get advantage on weapon attacks for the turn, and gain 10 temporary HP. Three times per long rest.",
    3: "As a bonus action on your turn, get advantage on weapon attacks for the turn, and gain 5 temporary HP. Three times per long rest.",
}

FightingSpirit = feature("Fighting Spirit","Subclass",FightingSpiritDesc,3,text=FightingSpiritText)





ElegantCourtierDesc = "Starting at 7th level, your discipline and attention to detail allow you to excel in social situations. Whenever you make a Charisma (Persuasion) check, you gain a bonus to the check equal to your Wisdom modifier. Your self-control also causes you to gain proficiency in Wisdom saving throws. If you already have this proficiency, you instead gain proficiency in Intelligence or Charisma saving throws (your choice)."
ElegantCourtierText = "Whenever you make a Persuasion check, you gain a bonus equal to your Wisdom modifier ({WIS})."
def ElegantCourtierFunc(character):
        if "Wisdom" in character.savingThrows:
            eligibleSaves = [save for save in ["Intelligence", "Charisma"] if save not in character.savingThrows]
            chosenSave = r.choice(eligibleSaves)
            addToList(character.savingThrows,chosenSave)
        else:
            addToList(character.savingThrows,"Wisdom")

ElegantCourtier = feature("Elegant Courtier","Subclass",ElegantCourtierDesc,7,function=ElegantCourtierFunc,text=ElegantCourtierText)



TirelessSpiritDesc = "Starting at 10th level, when you roll initiative and have no uses of Fighting Spirit remaining, you regain one use."
TirelessSpiritText = "When you roll initiative and have no uses of Fighting Spirit remaining, you regain one use."
TirelessSpirit = feature("Tireless Spirit","Subclass",TirelessSpiritDesc,10,text=TirelessSpiritText)


RapidStrikeDesc = "Starting at 15th level, you learn to trade accuracy for swift strikes. If you take the Attack action on your turn and have advantage on an attack roll against one of the targets, you can forgo the advantage for that roll to make an additional weapon attack against that target, as part of the same action. You can do so no more than once per turn."
RapidStrikeText = "Once per turn, if you take the Attack action on your turn and have advantage on an attack roll against one of the targets, you can forgo advantage for that roll to make an additional weapon attack against that target, in the same action."
RapidStrike = feature("Rapid Strike","Subclass",RapidStrikeDesc,15,text=RapidStrikeText)



StrengthBeforeDeathDesc = "Starting at 18th level, your fighting spirit can delay the grasp of death. If you take damage that reduces you to 0 hit points, you can use your reaction to delay falling unconscious, and you can immediately take an extra turn. While you have 0 hit points during that extra turn, taking damage causes death saving throw failures as normal, and three death saving throw failures can still kill you. When the extra turn ends, you fall unconscious if you still have 0 hit points. Once you use this feature, you can’t use it again until you finish a long rest."
StrengthBeforeDeathText = "Once per long rest, if you drop to 0 HP, use your reaction to immediately take an extra turn, after which you fall unconscious if you're still at 0. Taking damage causes death saving throw failures which can still kill you."
StrengthBeforeDeath = feature("Strength Before Death","Subclass",StrengthBeforeDeathDesc,18,text=StrengthBeforeDeathText)


Samurai = charSubclass("Samurai",Fighter,[BonusProficiencySamurai,FightingSpirit,ElegantCourtier,TirelessSpirit,RapidStrike,StrengthBeforeDeath],["Strength", "Constitution", "Wisdom"])
