#program cita opis s wikipedije
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import requests
import re
from PIL import Image


l=''
f = str(input())
f=f.split(' ')
fl=''
for i in f:
    i=i.lower()
    i=i.capitalize()
    fl+=i
    fl+='_'
fl=fl[:len(fl)-1]
#print(fl)


reg_url = "https://en.m.wikipedia.org/wiki/"+fl
file = open(fl.replace(' ','_')+".jpg", "wb")

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}  

req = Request(url=reg_url, headers=headers)
html = urlopen(req).read()
     
soup = BeautifulSoup(html, 'html.parser')

nice=soup.find(class_="mf-section-0")
for i in range(0,len(nice.find_all('p'))):
    l=l+'\n'
    l=l+nice.find_all('p')[i].text
    

nice2=soup.find(class_='image')
nice2=nice2.img['src']
response = requests.get('https:'+nice2)


file.write(response.content)
file.close()

print(l.replace('\n'+'\n',''))

image = Image.open(fl.replace(' ','_')+".jpg")
image.show()

