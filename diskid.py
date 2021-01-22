#1.zad sa zupanijskog 2013
n=int(input())
l=[0]
l1=[]
s=''
nc=0
suma1=0
for i in range(n):
	a=int(input())
	l.append(a)

	

l1.extend(l)


l1.remove(max(l1))
l1.sort()
#print(l1)

l1[0]=1
for i in range(l1.count(1)):
	l1.remove(1)
l1.insert(0,2)
#print(l1,suma1)
for i in range(len(l1)):
	nc=nc+l1[i]
#	print(nc)
	for j in range(len(str(nc))):
		suma1+=int(str(nc)[j])
		print(suma1, int(str(nc)[j]))
	
#print(l1,suma1, suma1%255)
suma1=hex(suma1)

suma2=hex(sum(l))
suma2=suma2.split('x')
suma2=suma2[1]

suma1=suma1.split('x')
suma1=suma1[1]

nb=hex(n)
nb=nb.split('x')
nb=nb[1]

s=s+(2-len(suma1))*'0'+suma1
s=s+(4-len(suma2))*'0'+suma2
s=s+(2-len(nb))*'0'+nb
print(s)
