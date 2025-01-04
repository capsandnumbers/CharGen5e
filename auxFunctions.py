

from classDefs import *


def makeFeature(input,s = 0,f = 0, h = 0):
    
    
    if " " in input:
        input2 = input.title().replace(" ","")
    else:
        input2 = input    
    


    output0 = input2.replace(" ","") + " = feature('" + input + "', 'Background', " 


    if not s and f and h:
        output0 = output0 + '""'
    else:
        output0 = output0 + input2 + "Desc"


        print(input2+'Desc = ""')
    

    if s == 1:
        output0 = output0 + ", showText = "+input2+"ShowText"
        print(input2+'ShowText = ""')
    if f == 1:
        output0 = output0 + ", function = "+input2+"Func"
        print('def '+input2+'Func(character):')
        print()
    
    if h == 1:
        output0 = output0 + ", hideFeature = True"

    output0 = output0 + ")"
    print(output0.replace("'",'"'))
 
makeFeature("Shelter of the Faithful",1,0,0)