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


UnarmoredDefenseDesc = "Beginning at 1st level, while you are wearing no armor and not wielding a shield, your AC equals 10 + your Dexterity modifier + your Wisdom modifier."
UnarmoredDefenseText = "While unarmored, your AC equals 10 + DEX + WIS"

def UnarmoredDefenseTextFunc(character):
    return "While unarmored, your AC equals "+ str(10 + character.abilityMods["Dexterity"] + character.abilityMods["Wisdom"])

def UnarmoredDefenceCallback(character):
    if character.equipment["armor"] == "None" and character.equipment["offhand"] != "Shield":
        character.AC = 10 + character.abilityMods["Dexterity"] + character.abilityMods["Wisdom"]


UnarmoredDefense = feature("Unarmored Defense","Class",UnarmoredDefenseDesc,text=UnarmoredDefenseText,callback=UnarmoredDefenceCallback)

MartialArts = feature("Martial Arts","Class",MartialArtsDesc,type="Callback",textFunc = stagedReplacePlaceholders(MartialArtsSchedule,MartialArtsText,"{damageDie}"),callback = MartialArtsCallback)





KiDesc = "Starting at 2nd level, your training allows you to harness the mystic energy of ki. Your access to this energy is represented by a number of ki points. Your monk level determines the number of points you have, as shown in the Ki Points column of the Monk table. You can spend these points to fuel various ki features. You start knowing three such features: Flurry of Blows, Patient Defense, and Step of the Wind. You learn more ki features as you gain levels in this class. When you spend a ki point, it is unavailable until you finish a short or long rest, at the end of which you draw all of your expended ki back into yourself. You must spend at least 30 minutes of the rest meditating to regain your ki points. Some of your ki features require your target to make a saving throw to resist the feature's effects. The saving throw DC is calculated as follows: Ki save DC = 8 + your proficiency bonus + your Wisdom modifier"
KiText = "You have {level} ki points which refresh on a rest with 30 minutes of meditation. Ki save DC = {kiSave}."
def KiTextFunc(character):
    return "You have " + str(character.level) +  " ki points which refresh on a rest with 30 minutes of meditation. Ki save DC = "+ str(8 + character.profMod + character.abilityMods["Wisdom"]) +"."

Ki = feature("Ki","Class",KiDesc,2,textFunc=KiTextFunc)


FlurryOfBlowsDesc = "Immediately after you take the Attack action on your turn, you can spend 1 ki point to make two unarmed strikes as a bonus action."
FlurryOfBlowsText = "Immediately after taking the Attack action on your turn, spend 1 ki to make two unarmed strikes as a bonus action."
FlurryOfBlows = feature("Flurry of Blows","Class",FlurryOfBlowsDesc,2,text = FlurryOfBlowsText)

PatientDefenseDesc = "You can spend 1 ki point to take the Dodge action as a bonus action on your turn."
PatientDefenseText = "Spend 1 ki to take the Dodge action as a bonus action on your turn."
PatientDefense = feature("Patient Defense","Class",PatientDefenseDesc,2,text = PatientDefenseText)


StepOfTheWindDesc = "You can spend 1 ki point to take the Disengage or Dash action as a bonus action on your turn, and your jump distance is doubled for the turn."
StepOfTheWindText = "Spend 1 ki to take the Disengage or Dash action as a bonus action on your turn, and your jump distance is doubled to for the turn."

def StepOfTheWindTextFunc(character):
    return "Spend 1 ki to take the Disengage or Dash action as a bonus action on your turn, and your jump distances are doubled for the turn. Long jump: "+ str(2*character.longJumpDistance) +"ft., High jump: "+ str(2*character.highJumpDistance) +" ft."

StepOfTheWind = feature("Step of the Wind","Class",StepOfTheWindDesc,2,text = StepOfTheWindText)


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

UnarmoredMovement = feature("Unarmored Movement","Class",UnarmoredMovementDesc,2,textFunc=stagedUpdate(UnarmoredMovementTextSchedule),callback = UnarmoredMovementCallback)



Monk = charClass("Monk",8,["Strength","Constitution","Charisma"],["Strength","Dexterity"],['Acrobatics', 'Athletics', 'History', 'Insight', 'Religion', 'Stealth'],2,{"weapon": simpleWeapons+  ["Shortsword"]},[MartialArts, UnarmoredDefense,Ki,FlurryOfBlows,PatientDefense,StepOfTheWind,UnarmoredMovement],ASISchedules["Monk"],optionalProfs = [(artisansTools+musicalInstruments,"tool",1)])
Empty = charSubclass("Empty",Monk,[])
