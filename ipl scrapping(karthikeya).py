import requests
import re
import csv
from bs4 import BeautifulSoup as bs
r1 = requests.get("http://stats.espncricinfo.com/ci/engine/records/batting/list_hundreds.html?id=117;type=trophy")
#soup = bs(r1.content,"html.parser")
soup = bs(r1.content,'html.parser')
k1=soup.find_all('a',{'class':"data-link"})
k2=soup.find_all('td',{'nowrap':"nowrap"})
l5=[]
jr=[]
for j in range(len(k1)):
	jr.append(k1[j].text)	
for i in k2:
	l5.append(i.text)
k6=[]	
for i in range(len(l5)):
	if (i-6)%11!=0:
		k6.append(l5[i])
jr1=[]
for i in range(len(jr)):
	if (i-1)%3==0:
		jr1.append(jr[i])
u1=[]
for i in range(len(k6)):
	if (i-7)%10==0:
		u1.append(k6[i])
		u1.append(jr1[(i-7)//10])
	else:
		u1.append(k6[i])
i1=0
p=[]
for i in range(len(u1)//11):
	p.append(u1[i1:i1+10])
	i1+=11
print(p)
import csv
 
myData = [['Player', "Runs", "Balls",'4s','6s','SR','Team','Opposition','Ground','Match date']]+p
 
myFile = open('r.csv', 'w')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(myData)
     
print("Writing complete")




