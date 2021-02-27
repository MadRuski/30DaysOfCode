n,k=map(int,input().split())
unos=list(str(input()))
l=[]
for i in range(1,k+1):
	razmak=n//i
	od=0
	do=razmak
	suma=0
	for j in range(i):
		brojac1=unos[od:do].count('1')
		brojac0=razmak-brojac1
		if brojac0>brojac1:
			suma+=brojac1
		if brojac0<brojac1:
			suma+=brojac0
		if brojac0==brojac1:
			suma+=brojac0
		brojac1+=razmak
		brojac0+=razmak
	l.append(suma)
print(min(l))