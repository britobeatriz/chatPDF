import os
import aspose.words as aw
import requests
from dotenv import load_dotenv
import pandas as pd

#env
env = ".env"
load_dotenv(env)
API_KEY = os.getenv('BASEAPI_TOKEN')

files = os.listdir('./arquivos')
#print(files)

curriculum = [file for file in files if file.endswith('.docx')]
#print(curriculum)

#transform word to pdf
for c in curriculum:
    doc = aw.Document('./arquivos/'+c)
    doc.save('./curriculum/'+c+'.pdf')

#upload
def uploadFile(document):
    headers =  {'x-api-key': API_KEY,
    }

    files = [
        ('file', ('file', open(document, 'rb'), 'application/octet-stream'))
    ]

    source_ID = ""

    response = requests.post(
        'https://api.chatpdf.com/v1/sources/add-file', headers=headers, files=files)

    if response.status_code == 200:
        print('Source ID:', response.json()['sourceId'])
        source_ID = response.json()['sourceId']
        return source_ID
    else:
        print('Status:', response.status_code)
        print('Error:', response.text)

#asking-request
def askingReq(src_id,questions):
    headers =  {'x-api-key': API_KEY,
    }

    data = {
    "sourceId": src_id,
    "messages": [
        {
        "role": "user",
        "content": questions
        }
    ]
    }

    response = requests.post(
        'https://api.chatpdf.com/v1/chats/message', headers=headers, json=data)

    if response.status_code == 200:
        #print('Result:', response.json()['content'])
        return response.json()['content']
    else:
        print('Status:', response.status_code)
        print('Error:', response.text)


questions = ['Responda de forma abreviada. Qual o nome da pessoa?','Responda de forma abreviada. Qual a profisssão da pessoa?','Responda de forma abreviada. Qual a localidade da pessoa?','Responda de forma abreviada. Qual o cargo atual?']

pdfs = os.listdir('./curriculum')
documents = [pdf for pdf in pdfs if pdf.endswith('.pdf')]

data = pd.DataFrame()

for doc in documents:
    curriculo_selecionado = './curriculum/'+doc
    print(curriculo_selecionado)
    response = []
    cod_document = uploadFile(curriculo_selecionado)

    for question in questions:
        re = askingReq(cod_document, question)
        columns = f'Pergunta{questions.index(question)}'
        response.append(re)

    new_line = pd.DataFrame({'nome': [response[0]], 'profissao': [response[1]], 'localidade': [response[2]], 'cargo_atual': [response[3]]})
    data = pd.concat([data, new_line], ignore_index=True)
        
#print(data)
# rename-columns
#data.rename(columns={'Pergunta0':'nome','Pergunta1':'profissao','Pergunta2':'localidade','Pergunta3':'cargo_atual'}, inplace=True)
data.to_csv('informacao.csv', index=False)