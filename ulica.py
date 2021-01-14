#HONI 2019/2020 6.KOLO 2.ZAD ulica.py
n=int(input())
l=list(map(int,input().split()))
l2=[]
d=len(l)
j=2
j2=1
for i in l:
    #print(i)
    if i %2==0:
        l2.append(i)
        l[l.index(i)]=0
        d-=1

if len(l2)>d:
    while True:
        if j in l2:
            j+=2
        if j not in l2:
            print(j)
            break
        
if len(l2)<d:
    while True:
        if j2 in l:
            j2+=2
        if j2 not in l:
            print(j2)
            break
            
    
