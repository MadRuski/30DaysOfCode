n=int(input())
hal=[]
for i in range(n):
	x,y=map(int,input().split())
	l=[]
	q=[]

	p=[]
	d={}
	c=0
	
	for i in range(x):
		l.append( list(str(input())) )
		for j in range(len(l[i])):
			if l[i][j] == '1':
				q.append((i*y)+j+1)
				
	while len(d)!= x*y:

		for i in range(len(q)):

			if q[i]==1:
				p.extend([q[i]+1,q[i]+y])
			elif q[i]==y:
				p.extend([q[i]-1,q[i]+y])
			elif q[i]==(x*y)-(y-1):
				p.extend([q[i]+1,q[i]-y])
			elif q[i]==x*y:
				p.extend([q[i]-1,q[i]-y])

			elif q[i]%y==0:
				p.extend([q[i]-1,q[i]-y,q[i]+y])
			elif q[i]%y==1:
				p.extend([q[i]+1,q[i]-y,q[i]+y])

			elif q[i]>x*(y-1):
				p.extend([q[i]-1 , q[i]-y , q[i]+1])

			elif q[i]<y:
				p.extend([q[i]-1,q[i]+y,q[i]+1])

			else:
				p.extend([q[i]-1,q[i]-y,q[i]+y,q[i]+1])

			d[q[i]]=str(c)
		q=[]
		for j in range(len(p)):
			if p[j] not in d.keys() and p[j] <= x*y:
				q.append(p[j])
		p=[] 
		c+=1

	for i in range(x):
		hal.append([])
		for j in range(y):
			hal[len(hal)-1].append(d[(i*y)+j+1])

	d={}
	
for i in range(len(hal)):
	print(' '.join(hal[i]))