#1.zadatak s 2017. zupanijskog 1.razred
c=list(map(int,input().split()))
mali=min(c)
veli=max(c)
raz=veli-mali

if c.index(veli)==0:
	h=((c[1]-c[2])/raz)*60

if c.index(veli)==1:
	h=(((c[2]-c[0])/raz)+2)*60

if c.index(veli)==2:
	h=(((c[0]-c[1])/raz)+4)*60

if h<0:
	h+=360

print(h)