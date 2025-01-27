from CharGen5e.classDefs import *
from CharGen5e.Sources.SRD.Classes.monkClass import *


OpenHandTechniqueDesc = "Starting when you choose this tradition at 3rd level, you can manipulate your enemy's ki when you harness your own. Whenever you hit a creature with one of the attacks granted by your Flurry of Blows, you can impose one of the following effects on that target: It must succeed on a Dexterity saving throw or be knocked prone. It must make a Strength saving throw. If it fails, you can push it up to 15 feet away from you. It can't take reactions until the end of your next turn."
OpenHandTechniqueText = "When you hit with Flurry of Blows, impose an effect on the target: It must make a DEX save or be knocked prone. It must make a STR save or be pushed up to 15 ft. It can't take reactions until the end of your next turn."
OpenHandTechnique = feature("Open Hand Technique","Subclass",OpenHandTechniqueDesc,3,text=OpenHandTechniqueText)

WholenessOfBodyDesc = "At 6th level, you gain the ability to heal yourself. As an action, you can regain hit points equal to three times your monk level. You must finish a long rest before you can use this feature again."
WholenessOfBodyText = "As an action once per long rest, regain hit points equal to three times your monk level."
def WholenessOfBodyTextFunc(character):
    return "As an action once per long rest, regain hit points equal to three times your monk level ("+ str(3*character.level)+")."
WholenessOfBody = feature("Wholeness of Body","Subclass",WholenessOfBodyDesc,6,text=WholenessOfBodyText, textFunc=WholenessOfBodyTextFunc)

TranquilityDesc = "Beginning at 11th level, you can enter a special meditation that surrounds you with an aura of peace. At the end of a long rest, you gain the effect of a Sanctuary spell that lasts until the start of your next long rest (the spell can end early as normal). The saving throw DC for the spell equals 8 + your Wisdom modifier + your proficiency bonus."
TranquilityText = "After a long rest you gain the effect of a Sanctuary spell that lasts until the start of your next long rest. Uses Ki save DC."
Tranquility = feature("Tranquility","Subclass",TranquilityDesc,11,text = TranquilityText)

QuiveringPalmDesc = "At 17th level, you gain the ability to set up lethal vibrations in someone's body. When you hit a creature with an unarmed strike, you can spend 3 ki points to start these imperceptible vibrations, which last for a number of days equal to your monk level. The vibrations are harmless unless you use your action to end them. To do so, you and the target must be on the same plane of existence. When you use this action, the creature must make a Constitution saving throw. If it fails, it is reduced to 0 hit points. If it succeeds, it takes 10d10 necrotic damage. You can have only one creature under the effect of this feature at a time. You can choose to end the vibrations harmlessly without using an action."
QuiveringPalmText = "On an unarmed strike hit, spend 3 ki to start vibrations lasting {level} days. As an action, force the creature to make a CON save: On a fail it drops to 0 HP, otherwise it takes 10d10 necrotic damage. One victim at a time, on the same plane as you when you strike."
QuiveringPalm = feature("Quivering Palm","Subclass",QuiveringPalmDesc,17,text=QuiveringPalmText)

OpenHandFeatures = [OpenHandTechnique,WholenessOfBody,Tranquility,QuiveringPalm]
OpenHand = charSubclass("Way of the Open Hand",Monk,OpenHandFeatures)
