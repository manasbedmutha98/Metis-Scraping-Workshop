print(1)
a='Chemistry'
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
c=0
c1=0
l=[]
for j in data['records']:
	print(j)
	print(2)