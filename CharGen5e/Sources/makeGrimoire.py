import os
import json

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'spells.json')

# Load the JSON file
with open(file_path, 'r', encoding='utf-8') as spellsFile:
    sample_load_file = json.load(spellsFile)
first_spell = sample_load_file[0]

print("First Spell Information:")
print(json.dumps(first_spell, indent=2))