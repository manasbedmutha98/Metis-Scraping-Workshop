#coding: utf-8
import requests
import re
from bs4 import BeautifulSoup as bs
import csv

r = requests.get('https://www.nobelprize.org/nobel_prizes/lists/all/')
o = bs(r.content,'html.parser')
l = o.find_all('h6')

l1=[['Year','Field','Laureates']]
for i in range(len(l)):
	s = str(l[i])
	w1 = s.find('nobel_prizes/')
	w2 = s.find('/laureates')
	s1 = s[w1+13:w2]
	s2 = s[w2+11:w2+15]
	s3 = str(l[i].text)
	s3 = s3.replace(' and ',', ')
	lw = s3.split(', ')
	l1.append([s2,s1] + lw)

myFile = open('nobel_laureates_v2.csv', 'w',encoding='utf-8')
with myFile:
    writer = csv.writer(myFile,lineterminator='\n')
    for i in l1:
    	writer.writerow(i)
myFile.close()
     
print("Writing complete")