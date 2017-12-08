import json
import sys
import requests

room = {'QA': 'https://rxpservices.hipchat.com/v2/room/4154443',
	'CCA': 'https://rxpservices.hipchat.com/v2/room/3554226',
	'TEST': 'http://rxpservices.hipchat.com/v2/room/4216688',
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
	return returnUrl
	
def getToken(key, usePersonalToken=True):
	if usePersonalToken:
		token = personalToken
	else:
		token = roomToken[key]
	return token


url = getUrl('TEST',False)
#url = 'https://rxpservices.hipchat.com/v2/room/4216688/notification?auth_token=vpgCm6XfSX3cLVrHNerPZWWINXCPBgizAV3yIe53'
#url = 'https://requestb.in/1esu8nr1'
f = open('payload.json','r') #read 
payload = f.read()
#payload = payload[1:-1]
headers = {'Content-type': 'application/json'}
headers['Authorization'] = "Bearer " + getToken('TEST',False)
#headers['Authorization'] = "Bearer " + personalToken
#r = requests.post(url, headers=headers, data=payload)
r = requests.post(url, data=json.dumps(payload), headers=headers)
#r = requests.post(url, data=payload)
#r = requests.post(url, data=json.dumps(payload))

r.raise_for_status()