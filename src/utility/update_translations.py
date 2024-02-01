import csv
import re
import os

translations_dict={}
translations_list=[]
	
translations_dict = {}

fpath = os.getcwd() + "/lib" # should probably replace with canary or else
fpath = fpath.replace('/src','')
fname = 'translations.csv'
pattern = r'(\w+),(\w+)'
if os.path.isfile(fpath+"/"+fname):
    source_file = open(fpath+"/"+fname, 'r')
    source_obj = csv.reader(source_file)

    for pair in source_obj:
        if pair:
            key   = pair[0]
            value = pair[1]
            translations_dict[key] = value
            translations_list.append([key,value])
       
            
    '''with open(fpath+"/"+fname, "r") as source_file:
        reader_obj = csv.reader(source_file)
        
        for line in reader_obj:
            for pair in line:
                match = re.match(r'(\w+),(\w+)',pair)
                if match:
                    key, value = match.groups()
                    translations_dict[key] = value
                    '''
else:
    print('translations csv not found.\n')    

print(translations_dict)