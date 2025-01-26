#FighterClass

from CharGen5e.classDefs import *





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


ExtraAttackFighter = feature("Extra Attack","Class",ExtraAttackDesc,5,textFunc=stagedUpdate(ExtraAttackSchedule))


IndomitableDesc = "Beginning at 9th level, you can reroll a saving throw that you fail. If you do so, you must use the new roll, and you can't use this feature again until you finish a long rest. You can use this feature twice between long rests starting at 13th level and three times between long rests starting at 17th level."
IndomitableText = "Once per long rest you can reroll a saving throw that you fail. You must use the new roll."


IndomitableSchedule = {
    17: "Three times per long rest you can reroll a saving throw that you fail. You must use the new roll.",
    13: "Twice per long rest you can reroll a saving throw that you fail. You must use the new roll.",
    9: "Once per long rest you can reroll a saving throw that you fail. You must use the new roll."
}

Indomitable = feature("Indomitable","Class",IndomitableDesc,9,textFunc=stagedUpdate(IndomitableSchedule),text=IndomitableText)





FighterFeatureList = [FightingStyle,ActionSurge,SecondWind,ASI,ExtraAttackFighter,Indomitable]
Fighter = charClass("Fighter",10,["Strength","Constitution"],["Strength","Constitution"],['Acrobatics', 'Animal Handling', 'Athletics', 'History', 'Insight', 'Intimidation', 'Perception', 'Survival'],2,{"weapon": simpleWeapons+martialWeapons,"armor":allArmor},FighterFeatureList,ASISchedules["Fighter"])













#################################################################################
#################################################################################
