#HONI 2019/2020 1.kolo 2.zadatak Lijepi.py
n=int(input())
l=[]
l1=[]
for i in range(n):
    l.append([])
    l[i]=list(map(str,input().split()))
    l1.append(int(l[i][0]+l[i][1]))
print (sum(l1))
#Author: Matej Ban