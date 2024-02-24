import csv
import re
import os

translations_dict = {}
translations_list = [] 

# Get the directory of the Flask app file
app_dir = os.path.dirname(os.path.abspath(__file__))

csv_filename = 'translations.csv'
csv_filepath = os.path.join(app_dir, csv_filename)

if os.path.isfile(csv_filepath):   
    with open(csv_filepath, "r", newline='', encoding='utf-8') as source_file:
        source_obj = csv.reader(source_file)
        
        for pair in source_obj:
            if pair:
                key, value = pair[0], pair[1]
                translations_dict[key] = value
                translations_list.append([key, value])
else:
    print('Translations CSV not found.')

print(translations_dict)
