#program koji u txt file zvan qt.txt stavlja dumb quoteove
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
f = open("qt.txt", "a")
reg_url = ("https://www.brainyquote.com/topics/dumb-quotes")
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}
for i in range(1,10):
     
    if i==1:
        req = Request(url=reg_url, headers=headers)
        
    else:
        req = Request(url=reg_url+'_'+str(i), headers=headers)
    html = urlopen(req).read()
    print(req.full_url)
    
    soup = BeautifulSoup(html, 'html.parser')

    nice=soup.find_all("div", class_="clearfix")

    for i in nice:
        t=(i.text).split('\n')
        del t[0]
    
        if len(t[0])==0 or len(t[1])==0:
            continue

        f.write(t[0]+'\n')
        f.write('-'+t[1]+'\n')
        f.write('\n')
    
    
f.close()
    
