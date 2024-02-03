import os

files = os.listdir('./')
#print(files)

curriculum = [file for file in files if file.endswith('.docx')][0]
#print(curriculum)

