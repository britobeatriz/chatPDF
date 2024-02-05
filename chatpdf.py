import os
import aspose.words as aw
import requests
from dotenv import load_dotenv

#env
env = ".env"
load_dotenv(env)
API_KEY = os.getenv('headers')

files = os.listdir('./')
#print(files)

curriculum = [file for file in files if file.endswith('.docx')][0]
#print(curriculum)

#transform word to pdf
doc = aw.Document(curriculum)
doc.save("curriculum.pdf")
doc = [file for file in files if file.endswith('.pdf')][0]

#upload
headers =  {'x-api-key': API_KEY,
}

files = [
    ('file', ('file', open(doc, 'rb'), 'application/octet-stream'))
]

source_ID = ""

response = requests.post(
    'https://api.chatpdf.com/v1/sources/add-file', headers=headers, files=files)

if response.status_code == 200:
    print('Source ID:', response.json()['sourceId'])
    source_ID = response.json()['sourceId']
else:
    print('Status:', response.status_code)
    print('Error:', response.text)

#asking-request
data = {
   "sourceId": source_ID,
   "messages": [
    {
       "role": "user",
       "content": "qual o nome da pessoa?"
    }
   ]
}

response = requests.post(
    'https://api.chatpdf.com/v1/chats/message', headers=headers, json=data)

if response.status_code == 200:
    print('Result:', response.json()['content'])
else:
    print('Status:', response.status_code)
    print('Error:', response.text)