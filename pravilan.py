rijec=list(str(input()))
rijec.extend('.'*len(rijec))
rjesenja=[]
n=int(input())
tocno=0
for i in range(n):
	p=list(str(input()))
	if len(p)==2:
		rjesenja.append('DA')
		continue

	if p[0] not in rijec:
		rjesenja.append('NE')
		continue

	pslovo=rijec.index(p[0])

	if p[1] not in rijec[pslovo+1:]:
		rjesenja.append('NE')
		continue

	dslovo=rijec[pslovo+1:].index(p[1])+pslovo+1
	razmak=dslovo-pslovo

	for i in range(2,len(p)):
		#print(pslovo,dslovo,razmak,p[i],i)
		if rijec[dslovo+razmak] != p[i]:
			tocno=1
			rjesenja.append('NE')
			break
		dslovo+=razmak
	if tocno != 1:
		rjesenja.append('DA')
	tocno=0

for i in rjesenja:
	print(i)