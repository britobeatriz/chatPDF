import os
import aspose.words as aw

files = os.listdir('./')
#print(files)

curriculum = [file for file in files if file.endswith('.docx')][0]
#print(curriculum)

#transform word to pdf
doc = aw.Document(curriculum)
doc.save("curriculum.pdf")
