# edits translations.py
import os
import platform
import getpass
import os, fnmatch


def find_files(directory, pattern):
    for root, dirs, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                filename = os.path.join(root, basename)
                yield filename


for filename in find_files('src', 'translations.py'):
    print (f'(Found dictionary source: {filename}))'


# first find the directory where the translations file is stored
os_name = platform.system()
user_str = getpass.getuser()

if 'windows' in os_name.lower(): #not tested !!!
    search_path = os.path.join('..','Documents and Settings',user_str)
elif 'linux' in os_name.lower():
    search_path = os.path.join('/home',user_str)

translations_file = find_file(search_path,'translations.py')

with open('/home/bransa/Documents/GitHub/landa/src/translations.py') as f:
    lines = f.readlines()
print(lines)

