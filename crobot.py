def bfs(l2,q,d):
	p=[]
	visited=[]
	t=0
	while len(q)>0:
		if l2[q[0][0]][q[0][1]]=='x' or q[0] in visited:
			q.pop(0)
			if len(q)==0 and len(p)>0:
				t+=1
				q.extend(p)
				p=[]
			continue
		if type(l2[q[0][0]][q[0][1]]) is int:
			d[ l2[q[0][0]] [q[0][1]] ]=t

		if q[0][0]!=0:
			p.append([ q[0][0]-1, q[0][1] ])

		if q[0][0]!= x-1:
			p.append([ q[0][0]+1, q[0][1] ])

		if q[0][1]!=0:
			p.append([ q[0][0], q[0][1]-1 ])

		if q[0][1]!= y-1:
			p.append([ q[0][0], q[0][1]+1 ])

		visited.append(q[0])
		q.pop(0)

		if len(q)==0 and len(p)>0:
			t+=1
			q.extend(p)
			p=[]
	return d

r=float('inf')

def tsp(graph, v, currPos, count, cost):
	if (count == len(graph) and graph[currPos][0]):
		global r
		if cost<r:
			r=cost
		#answer.append(cost + graph[currPos][0]) za cijeli krug
		return


	for i in range(len(graph)):
		if (v[i] == False and graph[currPos][i]):

			v[i] = True
			tsp(graph, v, i, count + 1,
				cost + graph[currPos][i])
			v[i] = False

puts=[]
while True:
	y,x=map(int,input().split())
	k=0
	if x==0 and y==0:
		break
	w=[]
	l=[]
	c=1
	for i in range(x):
		l.append( list(str(input())) )
	for i in range(x):
		for j in range(y):
			if 'o' == l[i][j]:
				w.insert(0,[i,j])
				l[i][j]=0

			elif '*' == l[i][j]:
				w.append([i,j])
				l[i][j]=c
				c+=1
	d=[[ 0 for j in range(c)] for i in range(c)]
	ii=0
	while len(w)!=0:
		d[ii]=bfs(l,[w[0]],d[ii])
		w.pop(0)
		ii+=1
	
	v = [False for i in range( len(d) )]
	v[0]=True
	tsp(d,v,0,1,0)
	if r==float('inf') and c==1:
		puts.append(0)
	elif r==float('inf') and c!=1:
		puts.append(-1)
	else:
		puts.append(r)
	r=float('inf')
for i in puts:
	print(i)
