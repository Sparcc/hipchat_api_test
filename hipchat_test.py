import json
import sys
import requests

room = {'QA': 'https://rxpservices.hipchat.com/v2/room/4154443',
	'CCA': 'https://rxpservices.hipchat.com/v2/room/3554226',
	'TEST': 'http://api.hipchat.com/v2/room/4216688',
	'CCA_Notif': 'https://rxpservices.hipchat.com/v2/room/4292319'
	};
	
roomToken = {'QA': '',
	'CCA': '',
	'TEST': 'aIwsPTQjE3Tqji9ziCfGKzqDam5hKmcA7NTYvYVu',
	'CCA_Notif': ''
	};
	
personalToken = 'mzOQ3uqTjS9SqxPM6aZ3x9j4JAc96vDY3ppFAgCP'

def getUrl(key, usePersonalToken=True):
	returnUrl = ""
	if usePersonalToken:
		returnUrl = room[key] +'/notification?auth_token='+ personalToken
	else:
		returnUrl = room[key] +'/notification?auth_token='+ roomToken[key]
	#return room[key]
	return returnUrl
	
def getToken(key, usePersonalToken=True):
	if usePersonalToken:
		token = personalToken
	else:
		token = roomToken[key]
	return token


url = getUrl('TEST')
f = open('payload.json','r') #read 
payload = f.read()
headers = {'Content-type': 'application/json'}
#headers['Authorization'] = "Bearer " + getToken('TEST')

r = requests.post(url, data=json.dumps(payload), headers=headers)
r.raise_for_status()