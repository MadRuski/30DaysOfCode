x,y=map(int,input().split())
l=[]
q=[]
p=[]
l2=[]
c=0

for i in range(x):
	a=list(str(input()))

	l2.append([])
	l.append([])

	l[i].extend(a)
	l2[i].extend(a)

for i in range(x):
	for j in range(y):
		if l[i][j]=='*':
			q.append([i,j])

		if l[i][j]=='S':
			s=[i,j]

		if l[i][j]=='X':
			l[i][j]=-6
			l2[i][j]=-6

while len(q)>0:
	if l2[q[0][0]][q[0][1]]!='.' and l2[q[0][0]][q[0][1]]!='*' and l2[q[0][0]][q[0][1]]!='S':
		q.pop(0)
		if len(q)==0 and len(p)>0:
			c+=1
			q.extend(p)
			p=[]
		continue

	if q[0][0]!=0:
		p.append([ q[0][0]-1, q[0][1] ])

	if q[0][0]!= x-1:
		p.append([ q[0][0]+1, q[0][1] ])

	if q[0][1]!=0:
		p.append([ q[0][0], q[0][1]-1 ])

	if q[0][1]!= y-1:
		p.append([ q[0][0], q[0][1]+1 ])

	l2[q[0][0]][q[0][1]]=c
	q.pop(0)
	if len(q)==0 and len(p)>0:
		c+=1
		q.extend(p)
		p=[]

q.append(s)
p=[]
c=0

while len(q)>0:
	if l[q[0][0]][q[0][1]]!='.' and l[q[0][0]][q[0][1]]!='S' and l[q[0][0]][q[0][1]]!='*':
		q.pop(0)
		if len(q)==0 and len(p)>0:
			c+=1
			q.extend(p)
			p=[]
		continue

	if q[0][0]!=0:
		p.append([ q[0][0]-1, q[0][1] ])

	if q[0][0]!= x-1:
		p.append([ q[0][0]+1, q[0][1] ])

	if q[0][1]!=0:
		p.append([ q[0][0], q[0][1]-1 ])

	if q[0][1]!= y-1:
		p.append([ q[0][0], q[0][1]+1 ])

	l[q[0][0]][q[0][1]]=c
	q.pop(0)
	if len(q)==0 and len(p)>0:
		c+=1
		q.extend(p)
		p=[]

o=[]
r=False

for i in range(x):
	for j in range(y):
		if l[i][j]=='D':

			if i !=0:
				if type(l2[i-1][j]) is str and type(l[i-1][j]) is str:
					pass

				elif type(l2[i-1][j]) is str or l[i-1][j]<l2[i-1][j]:
					o.append(l[i-1][j]+1)
					r=True
					

			if i != x-1:
				if type(l2[i+1][j]) is str and type(l[i+1][j]) is str:
					pass

				elif type(l2[i+1][j]) is str or l[i+1][j]<l2[i+1][j]:
					o.append(l[i+1][j]+1)
					r=True
					
			if j != 0:
				if type(l2[i][j-1]) is str and type(l[i][j-1]) is str:
					pass

				elif type(l2[i][j-1]) is str or l[i][j-1]<l2[i][j-1]:
					o.append(l[i][j-1]+1)
					r=True
					
			if j != y-1:
				if type(l2[i][j+1]) is str and type(l[i][j+1]) is str:
					pass

				elif type(l2[i][j+1]) is str or l[i][j+1]<l2[i][j+1]:
					o.append(l[i][j+1]+1)
					r=True
					
if r==False:
	print('KAKTUS')
else:
	print(min(o))
