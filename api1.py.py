from difflib import get_close_matches as gcm
Name_author=input()
from bs4 import BeautifulSoup as bs
import requests, requests.auth, json
import re
s={}
url_airtable1 =	"https://api.airtable.com/v0/appVUVS59ZtfLl6OO/Books?"
api_key = "keyCpwCkafbdtmJib"
headers = {'Content-type': 'application/json', 'Authorization': 'Bearer ' + api_key}
r1 = requests.get(url_airtable1, headers=headers)
data1 = r1.json()
url_airtable2 = "https://api.airtable.com/v0/appVUVS59ZtfLl6OO/Books?&offset="+str(data1['offset'])
r2 = requests.get(url_airtable2, headers=headers)
data2 = r2.json()
for j in data1['records']:
	s[j['id']]=[j['fields']['Name']]
for j in data2['records']:
	s[j['id']]=[j['fields']['Name']]	
url_airtable =	"https://api.airtable.com/v0/appVUVS59ZtfLl6OO/Guests?"
r = requests.get(url_airtable, headers=headers)
data = r.json()
s1={}
for j in data['records']:
	s1[j['fields']['Name']]=j['fields']['Books Recommended']
g=gcm(Name_author,s1)
if Name_author in s1:
	for i in s1[Name_author]:
		print(*s[i])
elif(len(g)>=1):
	print("please type one of the Names given in these close matches")
	print(g)
	b1=input()
	if b1 in s1:
		for i in s1[b1]:
			print(*s[i])
	else:
		print("Sorry there are no close matches for guest")			
else:
	print("Sorry there are no close matches for guest")