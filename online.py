#1 zad sa skolskog 2021
s=int(input())
d=int(input())
r=int(input())
suma=0
brojevi=s
for i in range(2,r+1):
	for j in range(i):
		brojevi+=d
		#print(brojevi,i,suma)
		if i==r:
			suma+=brojevi
print(suma)