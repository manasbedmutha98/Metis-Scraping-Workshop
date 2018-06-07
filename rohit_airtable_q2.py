from bs4 import BeautifulSoup as bs
import requests, requests.auth, json
import re
import difflib


guests=[]
#first loading the books data for names(as we have ids from data2)
url_airtable = "https://api.airtable.com/v0/appsxElVPcbYynH1C/Books \
"
api_key = "keyysNkZszj05Mpom"

headers = {'Content-type': 'application/json', 'Authorization': 'Bearer ' + api_key}

r = requests.get(url_airtable, headers=headers)
data = r.json()



url_airtable2 = "https://api.airtable.com/v0/appsxElVPcbYynH1C/Guests \
"
api_key2 = "keyysNkZszj05Mpom"

headers2 = {'Content-type': 'application/json', 'Authorization': 'Bearer ' + api_key}

r = requests.get(url_airtable2, headers=headers2)
data2 = r.json()

a=input()
ids=[]
recbooks=[]
#first append all guest in guestlist
for b in data2['records']:
	guests.append(b['fields']['Name'])

if a in guests:
	oo=5# we don't have to change value of a
else:
	print("Guest doesn't exist")		
	print("Did you mean",difflib.get_close_matches(a,guests,6))
	a=input("select guest ")
		
for b in data2['records']:
	if b['fields']['Name']==a:
		for lp in range(len(b['fields']['Books Recommended'])): 
			ids.append(b['fields']['Books Recommended'][lp])

for j in data['records']:
	for i in ids:
		if j['id']==i:
			recbooks.append(j['fields']['Name'])
while 'offset' in data:
	if 'offset' in data:
		newoffset = str(data['offset'])
	url_airtable="https://api.airtable.com/v0/appsxElVPcbYynH1C/Books?offset="+newoffset
	headers = {'Content-type': 'application/json', 'Authorization': 'Bearer ' + api_key}
	r = requests.get(url_airtable, headers=headers)
	data = r.json()
	for j in data['records']:
		for i in ids:
			if j['id']==i:
				recbooks.append(j['fields']['Name'])
for i in recbooks:
	print(i)			

