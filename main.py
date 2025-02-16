import os
from collections import defaultdict

ARCHIVE =['7zip','rar','7z','zip']
IMAGE = ['img','png','ico','svg','jpg','jpeg', 'gif']
APPS = ['exe','msi','bat']
DOCS = ['doc','docx','pdf','xls','xlsx', 'txt', 'csv', 'html']
CODE = ['xml','py','js']

path = R"C:\Users\$USERNAME\Downloads"
MAIN_PATH = os.path.expandvars(path)
folders = ['Audio','Video','Documents','Images','Apps','Code','Others','Archive']
files_list = []
# Create empty dictonary of lists
files_mapping = defaultdict(list)

print(MAIN_PATH)
#print(os.listdir(MAIN_PATH))

# Create folders from folders list  in Downloads if they not exist
for folder in folders:
    directory = os.path.join(MAIN_PATH,folder)
    if not(os.path.isdir(directory)):
        os.mkdir(directory)

files_list = os.listdir(MAIN_PATH)

#print(files_list)

# Grouping files from Download in the dictonary by extension as a key
for file in files_list:
    extension = file.split('.')[-1]
    print(extension)
    files_mapping[extension].append(file)
#print(files_mapping)

for f_extension, f_list in files_mapping.items():

    if f_extension in ARCHIVE:
        for f in f_list:
            os.rename(os.path.join(MAIN_PATH,f), os.path.join(MAIN_PATH,'Archive',f))
            #print(os.path.join(MAIN_PATH,f))
            #print(os.path.join(MAIN_PATH,'Apps',f))
    elif f_extension in IMAGE:
        for f in f_list:
            os.rename(os.path.join(MAIN_PATH,f), os.path.join(MAIN_PATH,'Images',f))
    elif f_extension in APPS:
        for f in f_list:
            os.rename(os.path.join(MAIN_PATH,f), os.path.join(MAIN_PATH,'Apps',f))
    elif f_extension in DOCS:
        for f in f_list:
            os.rename(os.path.join(MAIN_PATH,f), os.path.join(MAIN_PATH,'Documents',f))
    elif f_extension in CODE:
        for f in f_list:
            os.rename(os.path.join(MAIN_PATH,f), os.path.join(MAIN_PATH,'Code',f))
