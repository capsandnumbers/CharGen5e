# Backgrounds
from classDefs import *


# SRD

ShelterOfTheFaithfulDesc = "As an acolyte, you command the respect of those who share your faith, and you can perform the religious ceremonies of your deity. You and your adventuring companions can expect to receive free healing and care at a temple, shrine, or other established presence of your faith, though you must provide any material components needed for spells. Those who share your religion will support you (but only you) at a modest lifestyle. You might also have ties to a specific temple dedicated to your chosen deity or pantheon, and you have a residence there. This could be the temple where you used to serve, if you remain on good terms with it, or a temple where you have found a new home. While near your temple, you can call upon the priests for assistance, provided the assistance you ask for is not hazardous and you remain in good standing with your temple." 
ShelterOfTheFaithfulText = "Those who share your religion will support you (but only you) at a modest lifestyle."
ShelterOfTheFaithful = feature("Shelter of the Faithful", "Background", ShelterOfTheFaithfulDesc, text = ShelterOfTheFaithfulText)

def AcolyteSetupFunc(character):
    eligibleLangs = [lang for lang in  allLanguages if lang not in character.proficiencies["language"] ]
    choices = r.sample(eligibleLangs,2)
    character.addProficiency({"language":choices})
AcolyteSetup = feature("AcolyteSetup", "Background", "", function = AcolyteSetupFunc, hideFeature = True)

Acolyte = background("Acolyte",{"skill":["Insight", "Religion"]},[ShelterOfTheFaithful,AcolyteSetup])

