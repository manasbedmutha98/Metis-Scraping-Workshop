d1=input("Please enter the start date in format of YYYY-MM-DD,for example 2017-10-01"+"\n")
d2=input("Now,please enter the end date in format of YYYY-MM-DD,for example 2017-10-01"+'\n')


print("please wait for the output")

from bs4 import BeautifulSoup as bs
import requests, requests.auth, json
import re
url_airtable =	"https://api.airtable.com/v0/appx5VDv2LcKJURTp/Talks?"
api_key = "keyCpwCkafbdtmJib"
headers = {'Content-type': 'application/json', 'Authorization': 'Bearer ' + api_key}
r = requests.get(url_airtable, headers=headers)
data = r.json()
url_airtable1 =	"https://api.airtable.com/v0/appx5VDv2LcKJURTp/Talks?&offset="+str(data['offset'])
r1 = requests.get(url_airtable1, headers=headers)
data1=r1.json()
dates=[]
di={}
c=0
s={}
d11=[]
d22=[]
for i in data['records']:
	dates.append(i['fields']['Date'])
	d11.append(i['fields']['Date'])
	d22.append(i['fields']['FullTitle'])
for i in data1['records']:
	dates.append(i['fields']['Date'])
	d11.append(i['fields']['Date'])
	d22.append(i['fields']['FullTitle'])
d1=d1+"A00:00:00.000Z"
d2=d2+"T24:00:00.000Z"
dates.append(d1)
dates.append(d2)
dates.sort()
f1=dates.index(d1)
f2=dates.index(d2)
Talks=[]
r9=5
if (f1<f2):
	for i in range(f1,f2):
		if dates[i] in d11:
			if not(d22[d11.index(dates[i])] in Talks):
		 		Talks.append(d22[d11.index(dates[i])])
			else:
				Talks.append(d22[d11.index(dates[i])+1]) 	
else:
	r9=0
	print("sorry the given start date is after the end date")
if len(Talks)>=1:
	cr=0
	for j in Talks:
		cr+=1
		print(str(cr)+") "+str(j))
else:
	if r9==5:
		print("Sorry No Talks were held in between")






