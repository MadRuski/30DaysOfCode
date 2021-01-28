#zadatak 3. sa skolskog 2018 za 8.razred
d=list(str(input()))
c=0

bh=d.count('H')
bb=d.count('B')
bj=d.count('J')

for i in range(bh):
	if d[i]!='H':
		c+=2
		
for i in range(bh,bh+bb):
	if d[i]!='B':
		c+=2
		
for i in range(len(d)-bj,len(d)):
	if d[i]!='J':
		c+=2

print(c)
