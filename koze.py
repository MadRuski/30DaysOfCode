x,y=map(int,input().split())
l=[]
q=[]
vukovi=[0]
koze=[0]
for i in range(x):
	l.append( list(str(input())) )
for i in range(x):
	for j in range(y):
		if l[i][j]=='.' or l[i][j]=='v' or l[i][j]=='k':
			q.append([i,j])
			vukovi.insert(0,0)
			koze.insert(0,0)

		while len(q)>0:
			if l[q[0][0]][q[0][1]]=='#' or l[q[0][0]][q[0][1]]=='X':
				q.pop(0)
				continue

			if l[q[0][0]][q[0][1]]=='v':
				vukovi[0]+=1

			if l[q[0][0]][q[0][1]]=='k':
				koze[0]+=1

			if q[0][0]!=0:
				q.append([ q[0][0]-1, q[0][1] ])

			if q[0][0]!= x-1:
				q.append([ q[0][0]+1, q[0][1] ])

			if q[0][1]!=0:
				q.append([ q[0][0], q[0][1]-1 ])

			if q[0][1]!= y-1:
				q.append([ q[0][0], q[0][1]+1 ])

			l[q[0][0]][q[0][1]]='X'
			q.pop(0)

		if koze[0]>vukovi[0]:
			vukovi[0]=0
		else:
			koze[0]=0
print(sum(koze),sum(vukovi))