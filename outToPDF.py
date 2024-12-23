# outToPDF

import pdfrw
import header


def printCharSheet(character):



    input_pdf  = pdfrw.PdfReader("CharSheet.pdf")


    output_pdf = character.name + '.pdf'

    form_data = {
        'Background': character.background.name,
        'CHA': str(character.abilities["Charisma"]),
        'CHamod': str(abMod(character.abilities["Charisma"])),
        'CharacterName': character.name,
        'Check Box 12': "Y",
        'ClassLevel': str(character.charClass.name) + " " + str(character.level),
        'CON': str(character.abilities["Constitution"]),
        'CONmod': str(abMod(character.abilities["Constitution"])),
        'DEX': str(character.abilities["Dexterity"]),
        'DEXmod': str(abMod(character.abilities["Dexterity"])),
        'HPCurrent': str(character.HP),
        'HPMax': str(character.HP),
        'INT': str(character.abilities["Intelligence"]),
        'INTmod': str(abMod(character.abilities["Constitution"])),
        'PlayerName': character.rank,
        'ProfBonus': str(character.profBonus),
        'Race ': character.race.name,
        'Speed': str(character.speed) + " ft.",
        'STR': str(character.abilities["Strength"]),
        'STRmod': str(abMod(character.abilities["Strength"])),
        'WIS': str(character.abilities["Wisdom"]),
        'WISmod': str(abMod(character.abilities["Intelligence"])),




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
