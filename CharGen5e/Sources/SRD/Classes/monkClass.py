#MonkClass

from CharGen5e.classDefs import *


MartialArtsDesc = "At 1st level, your practice of martial arts gives you mastery of combat styles that use unarmed strikes and monk weapons, which are shortswords and any simple melee weapons that don't have the two-handed or heavy property. You gain the following benefits while you are unarmed or wielding only monk weapons and you aren't wearing armor or wielding a shield: You can use Dexterity instead of Strength for the attack and damage rolls of your unarmed strikes and monk weapons. You can roll a d4 in place of the normal damage of your unarmed strike or monk weapon. This die changes as you gain monk levels, as shown in the Martial Arts column of the Monk table. When you use the Attack action with an unarmed strike or a monk weapon on your turn, you can make one unarmed strike as a bonus action. For example, if you take the Attack action and attack with a quarterstaff, you can also make an unarmed strike as a bonus action, assuming you haven't already taken a bonus action this turn."
MartialArtsText = "When using monk weapons and unarmored you may: Use DEX for attacks, roll a d{damageDie} for damage, and make an extra attack as a bonus action after using the Attack action "


MartialArtsSchedule = {
    17:str(10),
    11:str(8),
    5:str(6),
    1:str(4)
}

def MartialArtsCallback(character):
    1


MartialArts = feature("Martial Arts","Class",MartialArtsDesc,MartialArtsText,textFunc = stagedReplacePlaceholders(MartialArtsSchedule,MartialArtsText,"{damageDie}"),callback = MartialArtsCallback)



UnarmoredDefenseDesc = "Beginning at 1st level, while you are wearing no armor and not wielding a shield, your AC equals 10 + your Dexterity modifier + your Wisdom modifier."
UnarmoredDefenseText = "While unarmored, your AC equals 10 + DEX + WIS"

def UnarmoredDefenseTextFunc(character):
    return "While unarmored, your AC equals "+ str(10 + character.abilityMods["Dexterity"] + character.abilityMods["Wisdom"])

def UnarmoredDefenceCallback(character):
    if character.equipment["armor"] == "None" and character.equipment["offhand"] != "Shield":
        character.AC = 10 + character.abilityMods["Dexterity"] + character.abilityMods["Wisdom"]


UnarmoredDefense = feature("Unarmored Defense","Class",UnarmoredDefenseDesc,UnarmoredDefenseText,callback=UnarmoredDefenceCallback)






KiDesc = "Starting at 2nd level, your training allows you to harness the mystic energy of ki. Your access to this energy is represented by a number of ki points. Your monk level determines the number of points you have, as shown in the Ki Points column of the Monk table. You can spend these points to fuel various ki features. You start knowing three such features: Flurry of Blows, Patient Defense, and Step of the Wind. You learn more ki features as you gain levels in this class. When you spend a ki point, it is unavailable until you finish a short or long rest, at the end of which you draw all of your expended ki back into yourself. You must spend at least 30 minutes of the rest meditating to regain your ki points. Some of your ki features require your target to make a saving throw to resist the feature's effects. The saving throw DC is calculated as follows: Ki save DC = 8 + your proficiency bonus + your Wisdom modifier"
KiText = "You have {level} ki points which refresh on a rest with 30 minutes of meditation. Ki save DC = {kiSave}."
def KiTextFunc(character):
    return "You have " + str(character.level) +  " ki points which refresh on a rest with 30 minutes of meditation. Ki save DC = "+ str(8 + character.profBonus + character.abilityMods["Wisdom"]) +"."

Ki = feature("Ki","Class",KiDesc,KiText,2,textFunc=KiTextFunc)


FlurryOfBlowsDesc = "Immediately after you take the Attack action on your turn, you can spend 1 ki point to make two unarmed strikes as a bonus action."
FlurryOfBlowsText = "Immediately after taking the Attack action on your turn, spend 1 ki to make two unarmed strikes as a bonus action."
FlurryOfBlows = feature("Flurry of Blows","Class",FlurryOfBlowsDesc,FlurryOfBlowsText,2)

PatientDefenseDesc = "You can spend 1 ki point to take the Dodge action as a bonus action on your turn."
PatientDefenseText = "Spend 1 ki to take the Dodge action as a bonus action on your turn."
PatientDefense = feature("Patient Defense","Class",PatientDefenseDesc, PatientDefenseText,2)


StepOfTheWindDesc = "You can spend 1 ki point to take the Disengage or Dash action as a bonus action on your turn, and your jump distance is doubled for the turn."
StepOfTheWindText = "Spend 1 ki to take the Disengage or Dash action as a bonus action on your turn, and your jump distance is doubled to for the turn."

def StepOfTheWindTextFunc(character):
    return "Spend 1 ki to take the Disengage or Dash action as a bonus action on your turn, and your jump distances are doubled for the turn. Long jump: "+ str(2*character.longJumpDistance) +"ft., High jump: "+ str(2*character.highJumpDistance) +" ft."

StepOfTheWind = feature("Step of the Wind","Class",StepOfTheWindDesc,StepOfTheWindText,2)


UnarmoredMovementSchedule = {
    18:30,
    14:25,
    10:20,
    6:15,
    2:10,
}

def UnarmoredMovementCallback(character):
    if character.equipment["armor"] == "None" and character.equipment["offhand"] != "Shield":
        character.speed = character.race.speed + matchToSchedule(UnarmoredMovementSchedule,character)

UnarmoredMovementDesc = "Starting at 2nd level, your speed increases by 10 feet while you are not wearing armor or wielding a shield. This bonus increases when you reach certain monk levels, as shown in the Monk table. At 9th level, you gain the ability to move along vertical surfaces and across liquids on your turn without falling during the move."
UnarmoredMovementTextSchedule = {
    9: "While unarmored your speed increases. You may move along vertical surfaces and across liquids.",
    2: "While unarmored your speed increases."
}

UnarmoredMovement = feature("Unarmored Movement","Class",UnarmoredMovementDesc,None,2,textFunc=stagedUpdate(UnarmoredMovementTextSchedule),callback = UnarmoredMovementCallback)

DeflectMissilesDesc = "Starting at 3rd level, you can use your reaction to deflect or catch the missile when you are hit by a ranged weapon attack. When you do so, the damage you take from the attack is reduced by 1d10 + your Dexterity modifier + your monk level. If you reduce the damage to 0, you can catch the missile if it is small enough for you to hold in one hand and you have at least one hand free. If you catch a missile in this way, you can spend 1 ki point to make a ranged attack with a range of 20/60 using the weapon or piece of ammunition you just caught, as part of the same reaction. You make this attack with proficiency, regardless of your weapon proficiencies, and the missile counts as a monk weapon for the attack."
DeflectMissilesText = "As a reaction, catch a missile that hit you, reducing the damage by 1d10 + your Dexterity modifier + your monk level. If you reduce the damage to 0, you can catch the missile. Then spend 1 ki to redirect it, range 20/60. The missile is a monk weapon you're proficient with."
def DeflectMissilesTextFunc(character):
    damage = str(character.abilities["Dexterity"]+ character.level)
    return "As a reaction, catch a missile that hit you, reducing the damage by 1d10 + " + damage + ". If you reduce the damage to 0 you can catch the missile. Then spend 1 ki to immediately redirect it, range 20/60. The missile is a monk weapon you're proficient with."
DeflectMissiles = feature("Deflect Missiles","Class",DeflectMissilesDesc,DeflectMissilesText,3,textFunc=DeflectMissilesTextFunc)




SlowFallDesc = "Beginning at 4th level, you can use your reaction when you fall to reduce any falling damage you take by an amount equal to five times your monk level."
SlowFallText = "Use your reaction when you fall to reduce any falling damage you take by five times your monk level."
def SlowFallTextFunc(character):
    return "Use your reaction when you fall to reduce any falling damage you take by five times your monk level, ("+str(5*character.level)+")."
SlowFall = feature("Slow Fall","Class",SlowFallDesc,SlowFallText,4,textFunc=SlowFallTextFunc)




ExtraAttackDesc = "Beginning at 5th level, you can attack twice, instead of once, whenever you take the Attack action on your turn."
ExtraAttackText = "You can attack twice when you take the Attack action on your turn."
ExtraAttackMonk = feature("Extra Attack","Class",ExtraAttackDesc,None,5)


StunningStrikeDesc = "Starting at 5th level, you can interfere with the flow of ki in an opponent's body. When you hit another creature with a melee weapon attack, you can spend 1 ki point to attempt a stunning strike. The target must succeed on a Constitution saving throw or be stunned until the end of your next turn."
StunningStrikeText = "When you hit with a melee weapon, spend 1 ki to force the target to make a CON save, or be stunned until the end of your next turn."
StunningStrike  = feature("Stunning Strike","Class",StunningStrikeDesc,StunningStrikeText,5)

KiEmpoweredStrikesDesc = "Starting at 6th level, your unarmed strikes count as magical for the purpose of overcoming resistance and immunity to nonmagical attacks and damage."
KiEmpoweredStrikesText = "Your unarmed strikes count as magical weapons"
KiEmpoweredStrikes = feature("Ki-Empowered Strikes","Class",KiEmpoweredStrikesDesc,KiEmpoweredStrikesText,6)

EvasionDesc = "At 7th level, your instinctive agility lets you dodge out of the way of certain area effects, such as a blue dragon's lightning breath or a fireball spell. When you are subjected to an effect that allows you to make a Dexterity saving throw to take only half damage, you instead take no damage if you succeed on the saving throw, and only half damage if you fail."
EvasionText = "When you make a DEX save to take half damage, you instead take no damage on a success and half damage on a failure."
Evasion = feature("Evasion","Class",EvasionDesc,EvasionText,7)

StillnessOfMindDesc = "Starting at 7th level, you can use your action to end one effect on yourself that is causing you to be charmed or frightened."
StillnessOfMindText = "As an action, end one effect making you charmed or frightened."
StillnessOfMind = feature("Stillness of Mind","Class",StillnessOfMindDesc,StillnessOfMindText,7)

PurityOfBodyDesc = "At 10th level, your mastery of the ki flowing through you makes you immune to disease and poison."
PurityOfBodyText = "You are immune to disease and poison"
def PurityOfBodyFunc(character):
    addToList(character.damageImmunities,"Poison")
PurityOfBody = feature("Stillness of Mind","Class",PurityOfBodyDesc,PurityOfBodyText,10,function=PurityOfBodyFunc)



TongueOfTheSunAndMoonDesc = "Starting at 13th level, you learn to touch the ki of other minds so that you understand all spoken languages. Moreover, any creature that can understand a language can understand what you say."
TongueOfTheSunAndMoonText = "You understand all spoken languages and any creature that can understand a language can understand you."

def TongueOfTheSunAndMoonCallback(character):
    character.proficiencies["language"] = ["All Spoken Languages"]
TongueOfTheSunAndMoon = feature("Tongue of the Sun and Moon","Class",TongueOfTheSunAndMoonDesc,TongueOfTheSunAndMoonText,13,callback=TongueOfTheSunAndMoonCallback,hideFeature=True)

DiamondSoulDesc = "Beginning at 14th level, your mastery of ki grants you proficiency in all saving throws. Additionally, whenever you make a saving throw and fail, you can spend 1 ki point to reroll it and take the second result."
DiamondSoulText = "Spend 1 ki to reroll a failed save."
def DiamondSoulFunc(character):
    addToList(character.savingThrows,["Strength","Dexterity","Constitution","Intelligence","Wisdom","Charisma"])
DiamondSoul = feature("Diamond Soul","Class",DiamondSoulDesc,DiamondSoulText,14,function = DiamondSoulFunc)


TimelessBodyDesc = "At 15th level, your ki sustains you so that you suffer none of the frailty of old age, and you can't be aged magically. You can still die of old age, however. In addition, you no longer need food or water."
TimelessBodyText = "You suffer no frailty of old age, can't be aged magically, don't need food or water, but old age will still get you."
TimelessBody = feature("Timeless Body","Class",TimelessBodyDesc, TimelessBodyText,15)

EmptyBodyDesc = "Beginning at 18th level, you can use your action to spend 4 ki points to become invisible for 1 minute. During that time, you also have resistance to all damage but force damage. Additionally, you can spend 8 ki points to cast the astral projection spell, without needing material components. When you do so, you can't take any other creatures with you."
EmptyBodyText = "As an action, spend 4 ki to go invisible for 1 minute, with resistance to all but force damage. Spend 8 ki to cast Astral Projection without material components. When you do, you go alone."
EmptyBody = feature("Empty Body","Class",EmptyBodyDesc, EmptyBodyText,18)

PerfectSelfDesc = "At 20th level, when you roll for initiative and have no ki points remaining, you regain 4 ki points."
PerfectSelfText = "When you roll initiative and have no ki points remaining, you regain 4 ki."
PerfectSelf = feature("Perfect Self","Class",PerfectSelfDesc, PerfectSelfText,19)









MonkFeatureList = [MartialArts, UnarmoredDefense,Ki,FlurryOfBlows,PatientDefense,StepOfTheWind,UnarmoredMovement,DeflectMissiles,ASI,SlowFall,ExtraAttackMonk,StunningStrike,KiEmpoweredStrikes,Evasion,StillnessOfMind,PurityOfBody,TongueOfTheSunAndMoon,DiamondSoul,TimelessBody,EmptyBody,PerfectSelf]


Monk = charClass("Monk",8,["Dexterity","Wisdom"],["Strength","Dexterity"],['Acrobatics', 'Athletics', 'History', 'Insight', 'Religion', 'Stealth'],2,{"weapon": simpleWeapons+  ["Shortsword"]},MonkFeatureList,ASISchedules["Monk"],optionalProfs = [(artisansTools+musicalInstruments,"tool",1)])
Empty = charSubclass("Empty",Monk,[])
