n=int(input())
m=int(input())
agenti={i:set() for i in range(1,n+1)}

c=0
for i in range(1,m+1):
	unos=str(input())
	unos=unos.split(' ')
	if unos[0]=='A':
		for j in unos[2:]:
			agenti[int(j)].add(i)
		c+=1
	elif unos[0]=='B':
		r=set()
		for j in unos[2:]:
			r=r|agenti[int(j)]
		for j in unos[2:]:
			agenti[int(j)]=r.copy()
			
t=False		
for i in agenti:
	if len(agenti[i])==c:
		t=True
		print(i)
if t==False:
	print(0)