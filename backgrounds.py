# Backgrounds
from classDefs import *


# Basic Rules

ShelterOfTheFaithfulDesc = "As an acolyte, you command the respect of those who share your faith, and you can perform the religious ceremonies of your deity. You and your adventuring companions can expect to receive free healing and care at a temple, shrine, or other established presence of your faith, though you must provide any material components needed for spells. Those who share your religion will support you (but only you) at a modest lifestyle. You might also have ties to a specific temple dedicated to your chosen deity or pantheon, and you have a residence there. This could be the temple where you used to serve, if you remain on good terms with it, or a temple where you have found a new home. While near your temple, you can call upon the priests for assistance, provided the assistance you ask for is not hazardous and you remain in good standing with your temple." 
ShelterOfTheFaithfulShowText = "Those who share your religion will support you (but only you) at a modest lifestyle."
ShelterOfTheFaithful = feature("Shelter of the Faithful", "Background", ShelterOfTheFaithfulDesc, showText = ShelterOfTheFaithfulShowText)

def AcolyteSetupFunc(character):
    eligibleLangs = [lang for lang in  allLanguages if lang not in character.proficiencies["language"] ]
    choices = r.sample(eligibleLangs,2)
    character.addProficiency({"language":choices})
AcolyteSetup = feature("AcolyteSetup", "Background", "", function = AcolyteSetupFunc, hideFeature = True)

Acolyte = background("Acolyte",{"skill":["Insight", "Religion"]},[ShelterOfTheFaithful,AcolyteSetup])



CriminalContactDesc = "You have a reliable and trustworthy contact who acts as your liaison to a network of other criminals. You know how to get messages to and from your contact, even over great distances; specifically, you know the local messengers, corrupt caravan masters, and seedy sailors who can deliver messages for you."
CriminalContactShowText = "You have a reliable and trustworthy contact who acts as your liaison to a network of other criminals."
CriminalContact = feature("Criminal Contact", "Background", CriminalContactDesc, showText = CriminalContactShowText)

Criminal = background("Criminal",{"skill":["Deception", "Stealth"], "tool": ["Dragonchess Set", "Thieves' Tools"]},[CriminalContact])



RusticHospitalityDesc = "Since you come from the ranks of the common folk, you fit in among them with ease. You can find a place to hide, rest, or recuperate among other commoners, unless you have shown yourself to be a danger to them. They will shield you from the law or anyone else searching for you, though they will not risk their lives for you."
RusticHospitalityShowText = "You can find a place to hide, rest, or recuperate among other commoners, unless you have shown yourself to be a danger to them."
RusticHospitality = feature("Rustic Hospitality", "Background", RusticHospitalityDesc, showText = RusticHospitalityShowText)

FolkHero = background("Folk Hero",{"skill":["Animal Handling","Survival"],"tool":["Weaver's Tools","Land Vehicles"]},[RusticHospitality])


def NobleSetupFunc(character):
    eligibleLangs = [lang for lang in allLanguages if lang not in character.proficiencies["language"] ]
    choices = r.sample(eligibleLangs,1)
    character.addProficiency({"language":choices})

NobleSetup = feature("NobleSetup", "Background", "", function = NobleSetupFunc, hideFeature = True)

PositionOfPrivilegeDesc = "Thanks to your noble birth, people are inclined to think the best of you. You are welcome in high society, and people assume you have the right to be wherever you are. The common folk make every effort to accommodate you and avoid your displeasure, and other people of high birth treat you as a member of the same social sphere. You can secure an audience with a local noble if you need to."
PositionOfPrivilegeShowText = "The common folk make every effort to accommodate you and avoid your displeasure, and other people of high birth treat you as a member of the same social sphere."
PositionOfPrivilege = feature("Position of Privilege", "Background", PositionOfPrivilegeDesc, showText = PositionOfPrivilegeShowText)

Noble = background("Noble",{"skill": ["History","Persuasion"]},[PositionOfPrivilege, NobleSetup])





ResearcherDesc = "When you attempt to learn or recall a piece of lore, if you do not know that information, you often know where and from whom you can obtain it. Usually, this information comes from a library, scriptorium, university, or a sage or other learned person or creature. Your DM might rule that the knowledge you seek is secreted away in an almost inaccessible place, or that it simply cannot be found. Unearthing the deepest secrets of the multiverse can require an adventure or even a whole campaign."
ResearcherShowText = "When you attempt to learn or recall a piece of lore, if you do not know that information, you often know where and from whom you can obtain it."
Researcher = feature("Researcher", "Background", ResearcherDesc, showText = ResearcherShowText)

SageSetupDesc = ""
def SageSetupFunc(character):
    eligibleLangs = [lang for lang in  allLanguages if lang not in character.proficiencies["language"] ]
    choices = r.sample(eligibleLangs,2)
    character.addProficiency({"language":choices})
SageSetup = feature("SageSetup", "Background", SageSetupDesc, function = SageSetupFunc, hideFeature = True)


Sage = background("Sage",{"skill": ["Arcana","History"]},[Researcher, SageSetup])


MilitaryRankDesc = "You have a military rank from your career as a soldier. Soldiers loyal to your former military organization still recognize your authority and influence, and they defer to you if they are of a lower rank. You can invoke your rank to exert influence over other soldiers and requisition simple equipment or horses for temporary use. You can also usually gain access to friendly military encampments and fortresses where your rank is recognized."
MilitaryRankShowText = "You have a military rank from your career as a soldier which people loyal to your former organization still recognise."
MilitaryRank = feature("Military Rank","Background",MilitaryRankDesc, showText=MilitaryRankShowText)

Soldier = background("Soldier",{"skill":["Athletics","Intimidation"],"tool": ["Dragonchess Set", "Land Vehicles"]},[MilitaryRank]) # Come back and randomise the Dragonchess Set maybe




# Wider PHB

citySecretsDesc = 'You know the secret patterns and flow to cities and can find passages through the urban sprawl that others would miss. When you are not in combat, you (and companions you lead) can travel between any two locations in the city twice as fast as your speed would normally allow.'
CitySecretsShowText = "When not in combat, you and your party can travel in the city at twice your usual speed."
CitySecrets = feature("City Secrets","Background",citySecretsDesc, showText=CitySecretsShowText)


Urchin = background("Urchin",{"skill": ["Sleight of Hand","Athletics"],"tool": ["Disguise Kit", "Thieves' Tools"]},[CitySecrets])
