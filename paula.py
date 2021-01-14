#honi 6.kolo 2015/2016 2.zad paula.py
n=int(input())
c=0
for i in range(n):
    k=list(map(int,input().split()))
    if sum(k)>=40 and sum(k)>=40:
        continue
    else:
        c+=1
if c>0:
    print(c)
else:
    print('PAULA')
