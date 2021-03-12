import requests
import urllib
from bs4 import BeautifulSoup
import time

spremnik=''
while True:
    page = requests.get('https://www.blockchain.com/btc/blocks?page=1')
    soup = BeautifulSoup(page.content, 'html.parser')
    gag=soup.find(class_="sc-6nt7oh-0 PtIAf")
    gold=gag.find('a')['href']
    if spremnik != gold:
        spremnik=gold
        page=requests.get('https://www.blockchain.com'+gold)
        soup = BeautifulSoup(page.content, 'html.parser')
        gag=soup.find_all(class_="sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC")
        print(gag[0].text.strip(),end=' | ')
        print(gag[2].text.strip(),end=' | ')
        print(gag[3].text.strip(),end=' | ')
        gag2=soup.find(class_="sc-1r996ns-0 fLwyDF sc-1tbyx6t-1 kCGMTY iklhnl-0 eEewhk")
        print(gag2.text.strip(),end=' | ')
        print(gag[11].text.strip(),end=' | ')
        print(gag[13].text.strip(),end=' | ')
        print(str(float(gag[14].text.strip()[:5])+float(gag[15].text.strip()[:5]))+' BTC')
    time.sleep(30)
    