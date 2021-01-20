from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import time
import requests, zipfile
import io

sf='https://static.titlovi.com/titlovicom/content/images/flags/hr3.png'
sf2=[]
f = str(input('What movie subtitles? '))
k=int(input('Which title by popularitiy? '))
fl=f.lower()

reg_url = "https://titlovi.com/titlovi/?prijevod="+fl.replace(' ','_')

print('getting to the website:'+reg_url)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}  

req = Request(url=reg_url, headers=headers)
html = urlopen(req).read()
     
soup = BeautifulSoup(html, 'html.parser')

nice2=soup.find_all(class_="download")

nice=soup.find_all(class_="lang")


for i in range(len(nice)):
    if sf==nice[i]['src']:
        sf2.append(i)
        
saviour=nice2[sf2[int(k)-1]].a['href']

saviour=saviour[:len(saviour)-1]
saviour=saviour.split('-')
time.sleep(2)

elm='https://titlovi.com/download/?type=1&mediaid='+saviour[1]
print('Downloading subtitles from website:'+elm)

r = requests.get(elm)
z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall('C:\\Users\\Matej\\Documents\\fun\\titl')
print('Done!')

