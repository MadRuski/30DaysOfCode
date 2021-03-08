import urllib.request
import os  
 
def skiniga(url,name):
    urllib.request.urlretrieve(url, name)

url = 'https://hsin.hr/honi/arhiva/'
   
for i in range(2006,2021):
    directory = str(i)+'_'+str(i+1)
    parent_dir = "E:\projekt_h"
     
    path = os.path.join(parent_dir, directory)  
      
    os.makedirs(path)
    print(path)
    for j in range(1,7):
        if i==2020:
            url2='https://hsin.hr/honi/kolo'+str(j)+'_zadaci.pdf'
            skiniga(url2, path+'/'+str(i)+'_'+str(i+1)+'_kolo'+str(j)+'_zadaci.pdf')
            print(url2)
        else:
            url2=url+str(i)+'_'+str(i+1)+'/kolo'+str(j)+'_zadaci.pdf'
            skiniga(url2, path+'/'+str(i)+'_'+str(i+1)+'_kolo'+str(j)+'_zadaci.pdf')
            print(url2)
#2007_2008/kolo2_zadaci.pdf