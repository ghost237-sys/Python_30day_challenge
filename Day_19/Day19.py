#REST APIs in python.-i will only cover for accessing apis and not actually build one
#to build one you need to learn flask or django
#Apis work like websites through sending and receiving requests but instead of html it uses json data
#methodes
#GET - retreive 
#POST - write new data
#DELETE - delete
#PUT - write...update.....put is idempotent
#CRUD -Create Read Update Delete
#consuming an API
import requests
import json
response = requests.get('https://api.stackexchange.com/docs/questions/2.3/questions?order=desc&sort=activity&site=stackoverflow')
print(response.json())

for data in response.json()['items']:
	if data['answer_count'] == 0:
		print(data['title'])
		print(data['link'])
	else:
		print('skipped')
