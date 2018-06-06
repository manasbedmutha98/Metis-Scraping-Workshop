#coding: utf-8
import requests
import re
from bs4 import BeautifulSoup as bs
import csv

r = requests.get('http://stats.espncricinfo.com/ci/engine/records/batting/list_hundreds.html?id=117;type=trophy')
o = bs(r.content,'html.parser')
l = o.find_all('td',{"nowrap":"nowrap"})
for i in range(len(l)):
	l[i]=(l[i]).text

l2=o.find_all('a',{"class":"data-link"})
for i in range(len(l2)):
	l2[i]=(l2[i]).text
	
l1=[["name","score","balls","no. of six","no.of fours","strike rate","ground","team","opposition","date"]]
i = 0
j=0
while i<len(l):
	l1.append([l[i],l[i+1],l[i+2],l[i+3],l[i+4],l[i+5],l2[j+1],l[i+7],l[i+8][2:],l[i+9]])
	i+=11
	j+=3
#print(l1)
myFile = open('ipl_centuries.csv', 'w',encoding='utf-8')
with myFile:
    writer = csv.writer(myFile,lineterminator='\n')
    for i in l1:
    	writer.writerow(i)
myFile.close()
     
print("Writing complete")
