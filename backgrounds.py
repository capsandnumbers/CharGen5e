from classDefs import *

citySecretsDesc = 'You know the secret patterns and flow to cities and can find passages through the urban sprawl that others would miss. When you are not in combat, you (and companions you lead) can travel between any two locations in the city twice as fast as your speed would normally allow.'
CitySecretsShowText = "When not in combat, you and your party can travel in the city twice as fast as your usual speed."
CitySecrets = feature("City Secrets","Background",citySecretsDesc, showText=CitySecretsShowText)


Urchin = background("Urchin",["Sleight of Hand","Athletics"],{"tool": ["Disguise kit, Thieves' tools"]},[CitySecrets])

