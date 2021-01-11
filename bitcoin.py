#1. zadatak sa zupanijskog 2018. Bitcoin.py
n=int(input())
min1=9999999999
min2=9999999999
b=[]
for i in range(n):
    b.append(float(input()))
if n==3:
    print(((10/b[0])*b[1])/b[2])

#k2=((10/max(b))*min(b[:b.index(max(b))+1])) / min(b[b.index(max(b))+1:])

k2=10/min(b[:b.index(max(b))+1])    

k2=k2*max(b)

k2=k2/ min(b[b.index(max(b))+1:])
#print(k2)
#k1=((10/max(b[b.index(min(b))+1:]))*min(b)) / min(b[b.index(max(b[b.index(min(b))+1:]))+1:])

k1=10/min(b)
k1=k1*max(b[b.index(min(b))+1:]) 
k1=k1/ min(b[b.index(max(b[b.index(min(b))+1:]))+1:])
#print(k1)
if k1>k2:
    print(k1)
if k1<k2:
    print(k2)
if k1==k2:
    print(k1)
    
