n=int(input())
l=[]
z=0
brojac=1
suma=0
for i in range(n):
	l.append(int(input()))
l.sort()
l.reverse()
for i in range(n):
	for j in range(n):
		if l[i]+n < l[j]+brojac and j!=i:
			z=1
			break

		elif l[i]+n >= l[j]+brojac and j!=i:
			brojac+=1

	if z==0:
		suma+=1
	z=0
	brojac=1
print(suma)