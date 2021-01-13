#HONI 2019/2020 5.KOLO 2.ZAD DUEL.py
n=int(input())
l=[[],[]]

for i in range(2):
    z=int(input())
    for j in range(z):
        l[i].append(int(input()))
nr1=len(l[0])
nr2=len(l[1])
for i in range(len(l[i])):
    if l[0][i] in l[1]:
        nr1-=1
        nr2-=1
print(nr1)
print(nr2)
