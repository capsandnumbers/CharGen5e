from os import remove
import numpy as np
import random as r
import inspect

def setupInputArgs(self,frame):
        args, _, _, values = inspect.getargvalues(frame)
        for arg in args:
            if arg != 'self':
                setattr(self, arg, values[arg])

def abMod(abilityScore):
    return int(np.floor((abilityScore-10)/2))

def addToList(oldList, newEntry):
    if isinstance(newEntry, list):  # Check if newEntry is a list
        oldList.extend(newEntry)
    else:
        oldList.append(newEntry)
    # Deduplicate the list in-place
    unique_entries = list(dict.fromkeys(oldList))
    oldList.clear()
    oldList.extend(unique_entries)






def arrayChoose(inputArray, number, remove=True):
    # Check if we can safely choose `number` items
    if number > len(inputArray) and remove:
        raise ValueError("Cannot choose more items than are available when `remove` is True.")
    
    # If removing elements, work on a copy to avoid modifying the original list
    workingArray = inputArray[:] if remove else inputArray
    
    # Select items
    outputArray = []
    for _ in range(number):

        choice = r.choice(workingArray)  # Randomly select an element
        outputArray.append(choice)
        if remove:
            workingArray.remove(choice)  # Remove the chosen element only if `remove` is True
    
    return outputArray



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