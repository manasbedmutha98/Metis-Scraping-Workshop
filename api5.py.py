from bs4 import BeautifulSoup as bs
import requests, requests.auth, json
import re
url_airtable =	"https://api.airtable.com/v0/appx5VDv2LcKJURTp/Talks?"
api_key = "keyCpwCkafbdtmJib"
headers = {'Content-type': 'application/json', 'Authorization': 'Bearer ' + api_key}
r = requests.get(url_airtable, headers=headers)
data7 = r.json()
url_airtable1 =	"https://api.airtable.com/v0/appx5VDv2LcKJURTp/Talks?&offset="+str(data7['offset'])
r1 = requests.get(url_airtable1, headers=headers)
data77=r1.json()
c=0
c1=0
g1=open('g.txt','w')
l11=[]
for j in data7['records']:
	if 'Discipline' in j['fields']:
		if not(j['fields']['Discipline'] in l11):
			l11.append(j['fields']['Discipline'])	
for j in data77['records']:
	if 'Discipline' in j['fields']:
		if not(j['fields']['Discipline'] in l11):
			l11.append(j['fields']['Discipline'])	
for i in l11:
	print(i)			
a=input()
for j in data7['records']:
	if 'Discipline' in j['fields']:
		if a==j['fields']['Discipline']:
			
			g1.write(j['fields']['FullTitle']+'\n')
			g1.write("By:"+j['fields']['Speaker']+'\n')
			g1.write(j['fields']['Date']+'\n')
			if 'Abstract' in j['fields']:
				g1.write(j['fields']['Abstract']+'\n')
			else:
				g1.write("Abstract not available"+'\n')				
			g1.write('\n')
			g1.write('\n')
for j in data77['records']:
	if 'Discipline' in j['fields']:
		if a==j['fields']['Discipline']:
			
			g1.write(j['fields']['FullTitle']+'\n')
			g1.write("By:"+j['fields']['Speaker']+'\n')
			g1.write(j['fields']['Date']+'\n')
			if 'Abstract' in j['fields']:
				g1.write(j['fields']['Abstract']+'\n')
			else:
				g1.write("Abstract not available"+'\n')				
			g1.write('\n')
			g1.write('\n')


