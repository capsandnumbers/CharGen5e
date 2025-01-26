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

Tranquility
Tranquility
Tranquility
Tranquility


OpenHandFeatures = [OpenHandTechnique,WholenessOfBody]
OpenHand = charSubclass("Way of the Open Hand",Monk,OpenHandFeatures)
