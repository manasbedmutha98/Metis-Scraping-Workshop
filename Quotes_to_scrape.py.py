import re
import requests
from bs4 import BeautifulSoup as bs 
T = set() #To create a set of all the tags
for k in range(1,11): #There are 10 pages in total
	m = requests.get('http://quotes.toscrape.com/page/' + str(k) + '/')
	o = bs(m.content,'html.parser')
	p = o.find_all('a',{'class':'tag'}) # All tags are inside the <a>
	l1  = [] # A list of all string values of the searches in p
	for w in range(len(p)):
		l1.append(str(p[w]))
		for u in range(len(l1)):
			z = re.findall(r'(?<=>).*(?=<)',l1[u]) #REGEX considering only the tags
			for v in range(len(z)):
				T.add(z[v])

t = input("Enter a tag: ") # Input taking tag

n = int(input("Enter an index: ")) # Input taking index

if t in T: #Checking if t is a tag or not
    try: #if n value in range
        r = requests.get('http://quotes.toscrape.com/tag/' + t + '/page/' + str(n//10 + 1 ) + '/') #Each page consists of 10 quotes. So we take n//10 to got to particular page.
        n = n%10 # Index of quote in the page.(Each page consists of 10 quotes)
        soup = bs(r.content,'html.parser')
        c = soup.find_all('span', {"class" : "text"}) # All quotes are in <span>
        d = soup.find_all('small',{'class':'author'}) # All authors are in <small>
        try: # If n value in range
            q = str(c[n-1]) #Index in page will be n-1
            a = str(d[n-1]) #Index in page will be n - 1
            x = re.findall(r'(?<=>).*(?=<)',q) #REGEX to get the quotes
            y = re.findall(r'(?<=>).*(?=<)',a) #REGEX to get the authors
            print(x[0][1:-1]) #As we do not require quotation marks, we print only the quote.
            print('by' , y[0]) #Printing Author
        except: # if n value not valid(out of range)
            print('Index out of range.')
    except: #If n value out of range
        print('Index out of range.')
else: #if t is not a tag
	print("No such tag found.")
