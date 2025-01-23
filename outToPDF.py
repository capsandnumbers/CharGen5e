# outToPDF

import pdfrw
from dndCharGenerator.header import *

def printCharSheet(character):



    input_pdf  = pdfrw.PdfReader("CharSheet.pdf")


    output_pdf = character.name + '.pdf'


    abilityFieldDict = {"Strength": '',
        "Dexterity": '',
        "Constitution" : '',
        "Intelligence" : '',
        "Wisdom": '',
        "Charisma" :''}


    skillDict = {
    "Acrobatics": '',
    "Animal Handling": '',
    "Arcana": '',
    "Athletics": '',
    "Deception": '',
    "History": '',
    "Insight": '',
    "Intimidation": '',
    "Investigation":'',
    "Medicine":'',
    "Nature":  '',
    "Perception": '',
    "Performance":'',
    "Persuasion": '',
    "Religion":   '',
    "Sleight of Hand": '',
    "Stealth":         '',
    "Survival":        ''
}





    for ability in character.savingThrows:
        abilityFieldDict[ability] = 'Yes'
            #print('Proficient in ',ability, ' saves')

    for skill in skillDict:
        if skill in character.proficiencies["skill"]:
            skillDict[skill] = 'Yes'

    form_data = {



        'Check Box 11': abilityFieldDict["Strength"],
        'Check Box 18': abilityFieldDict["Dexterity"],
        'Check Box 19': abilityFieldDict["Constitution"],
        'Check Box 20': abilityFieldDict["Intelligence"],
        'Check Box 21': abilityFieldDict["Wisdom"],
        'Check Box 22': abilityFieldDict["Charisma"],
        #'Check Box 12': 'Yes', Death save successes
        #'Check Box 13': 'Yes',
        #'Check Box 14': 'Yes',
        #'Check Box 15': 'Yes', Death save failures
        #'Check Box 16': 'Yes',
        #'Check Box 17': 'Yes',
        'Check Box 23': '',  # Acrobatics
        'Check Box 24': '',  # Animal Handling
        'Check Box 25': '',  # Arcana
        'Check Box 26': '',  # Athletics
        'Check Box 27': '',  # Deception
        'Check Box 28': '',  # History
        'Check Box 29': '',  # Insight
        'Check Box 30': '',  # Intimidation
        'Check Box 31': '',  # Investigation
        'Check Box 32': '',  # Medicine
        'Check Box 33': '',  # Nature
        'Check Box 34': '',  # Perception
        'Check Box 35': '',  # Performance
        'Check Box 36': '',  # Persuasion
        'Check Box 37': '',  # Religion
        'Check Box 38': '',  # Sleight of Hand
        'Check Box 39': '',  # Stealth
        'Check Box 40': '',  # Survival

#Performance (Cha)  Persuasion (Cha)  Religion (Int)  Sleight of Hand (Dex)  Stealth (Dex)  Survival (Wis)

        'HPCurrent': str(character.HP),
        'HPMax': str(character.HP),

        'CharacterName': character.name,
        'PlayerName': character.rank,
        'ProfBonus': str(character.profBonus),
        'Race ': character.race.name,
        'ClassLevel': str(character.charClass.name) + " " + str(character.level),
        'Background': character.background.name,
        'Speed': str(character.speed) + " ft.",


        'STR': str(character.abilities["Strength"]),
        'STRmod': str(character.abilityMods["Strength"]),
        'ST Strength'       : str(10),
        'DEX': str(character.abilities["Dexterity"]),
        'DEXmod ': str(character.abilityMods["Dexterity"]),        
        'CON': str(character.abilities["Constitution"]),
        'CONmod': str(character.abilityMods["Constitution"]),
        'INT': str(character.abilities["Intelligence"]),
        'INTmod': str(character.abilityMods["Intelligence"]),
        'WIS': str(character.abilities["Wisdom"]),
        'WISmod': str(character.abilityMods["Wisdom"]),
        'CHA': str(character.abilities["Charisma"]),
        'CHAmod': str(character.abilityMods["Charisma"]),

       # 'ST Strength'       : 
       # 'ST Dexterity'      :
       # 'ST Constitution'   :
       # 'ST Intelligence'   :
       # 'ST Wisdom'         :
       # 'ST Charisma'       :



    }

    for page in input_pdf.pages:
        for annotation in page['/Annots']:
            if annotation['/Subtype'] == '/Widget':
                try:
                    form_name = annotation['/T'].to_unicode()
                    #print(f'{form_name=}')
                except: 
                    continue

                if form_name in form_data:
                    #print(form_data[form_name])
                    value = pdfrw.objects.pdfstring.PdfString.encode(
                        form_data[form_name]
                    )
                    annotation.update(pdfrw.PdfDict(V=value))

    

    input_pdf.Root.AcroForm.update(
        pdfrw.PdfDict(NeedAppearances=pdfrw.PdfObject('true'))
    )

    pdfrw.PdfWriter().write(output_pdf, input_pdf)
