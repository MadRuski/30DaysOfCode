#HONI 2019/2020 3.kolo 2.zadatak hajduk.py
n=int(input())
t=int(input())
l=[]
g=True
for i in range(n):
    k=int(input())
    l.append(k)
c=l.count(1)
for i in range(2,t+1): 
    if l.count(i)>c:
        print('NE')
        break
    if g is not False:
        g=False
        if c<(len(l)/2):
            print('NE')
        else:
            print('DA')