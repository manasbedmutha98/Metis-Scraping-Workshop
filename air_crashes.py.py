import re
import requests
from bs4 import BeautifulSoup as bs
dicti = {"January":"1","February":'2','March':'3','April':'4','May':'5','June':'6','July':'7','August':'8','September':'9','October':'10','November':'11','December':'12'}
#dictionary for month conversion to index
r = requests.get('https://en.wikipedia.org/wiki/List_of_accidents_and_incidents_involving_commercial_aircraft#')
soup = bs(r.content,'html.parser')
a = soup.find_all('body')

l = [] #list of accident description
x = str(a[0]).split('<h3>')#List of all data corresponding to a single year
x = x[1:-1]#Removed unwantd data
b = soup.find_all('h3')#Year headings
d = []#List of all Links
b=b[:-11]#Removed unwanted data
for j in range(len(b)):
	b[j] = (b[j].text)#Collected Years
	b[j]= b[j].replace('[edit]','')#Removed unwanted '[edit]'
for i in range(len(x)):
	y = re.findall(r'(?<=<li>).*?(?=</li>)',x[i])#Main data regarding an accident
	z = []
	for k in range(len(y)):
		y[k] = y[k].replace('<i>','')#Removed unwanted data
		y[k] = y[k].replace('</i>','')#Removed unwanted data
		y[k] = y[k].replace('<b>','')#Removed unwanted data
		y[k] = y[k].replace('</b>','')#Removed unwanted data
		y[k] = y[k].replace('</a>','')#Removed unwanted data
		z1 = re.findall(r'(?<=href\=\").*?(?=\")',str(y[k]))#Collecting Links
		if len(z1) != 0:
			z.append('https://en.wikipedia.org' + z1[0])
		else:
			z.append('')
		z2 = re.findall(r'<.*?>',y[k])
		if len(z2)!=0:
			for g in range(len(z2)):
				y[k] = y[k].replace(z2[g],'')
		
	l.append(y)
	d.append(z)
l[-1] = l[-1][:5]#Removed unwanted data
d[-1] = d[-1][:5]#Removed unwanted data
for w1 in range(len(l)):#To remove lines which do not denote an event
	for w2 in l[w1]:
		if w2[:w2.index(' ')] not in dicti:
			l[w1][l[w1].index(w2)-1] = l[w1][l[w1].index(w2)-1] + ' ' + w2
			del l[w1][l[w1].index(w2)] 

e=[]#list of dates
for la in range(len(l)):
	e2 = []
	for wa in range(len(l[la])):
		e1=[]
		ba = l[la][wa][:l[la][wa].index(' ')]
		mo = dicti[ba]#month
		da = l[la][wa][l[la][wa].index(' ')+1:l[la][wa].index(' ')+3]#date
		e1 = da.strip() + '/' + mo + '/' + b[la]
		e2.append(e1)
	e.append(e2)
for lw in range(len(l)):#To remove the date at beginning of description
	for lk in range(len(l[lw])):
		z3 = re.findall(r'(?<=–\s).*',l[lw][lk])
		if len(z3) != 0:
			l[lw][lk] = z3[0]
l1 = []#Final 2D list of complete data
for w in range(len(b)):
	for v in range(len(l[w])):
	    l1.append([b[w],e[w][v],l[w][v],d[w][v]])
Y = '2004'#str(input())#input as Year
if Y in b:
	ck = ''
	for j in range(len(l1)):
		if l1[j][0] ==  Y:
			ck = 'Date: ' + l1[j][1] + '\n' + 'Brief Description of The Event:\n'+ l1[j][2] + '\n' + 'For more details, click here: '+l1[j][3] + '\n\n'
			print(ck)#Printing the required data
else:
	if int(Y)>2017:
		print(Y ,'has not occurred yet.')#For future dates
	else:
		print('No Accident occured in ' + Y)#A year when no event happened