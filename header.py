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
