#libraries imported
import requests
from bs4 import BeautifulSoup

url='https://en.wikipedia.org/wiki/Category:Russian_masculine_given_names'
r=requests.get(url)
c=r.content
#c


soup=BeautifulSoup(c,"html.parser")
#searching for data
imena=soup.find("div", {"class":"mw-category"}) # div class="mw-category-generated"
#i also tested this one, to see if it would yield better results, but went with imena
imena_items=soup.find_all('li')

l=[]
#i should change names of my variables and lists, for sure ....
for i in imena:    
    g= i.find_all('a')
    #yields a list, so another loop was necesary
    for k in g:
        #gives the whole "a" tag, but get_text()
        #gives you the text only
        k =k.get_text()
        #packs the names in the list
        l.append(k)
    
#now some of these names have some added info next to them
#if you visit that wiki page you will see what i am talking about
#(given name), ( name ) and others which are not usable for my generator, 
#so another loop was necessary

l1=[]
for i in l:
    if "(given name)" or "(name)" or "(disambiguation)" or "(Slavic name)" in i:
        i=i.replace('(given name)', '')
        i=i.replace("(name)", '')
        i=i.replace('(disambiguation)','')
        i=i.replace('(Slavic name)',"")
        l1.append(i)
    else:
        l1.append(i)
        
print(l1)
