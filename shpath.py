import heapq as h
def dijkstra(G, start,poc):
    n = len(G)
    visited = [False]*n
    weights = [float('inf')]*n
    path = [None]*n
    queue = []
    weights[start] = 0
    h.heappush(queue, (0, start))
    while len(queue) > 0:
        tezina, cvor = h.heappop(queue)
        visited[cvor] = True
        for v, w in G[cvor]:
            if not visited[v]:
                ukupnaTezina = tezina + w
                if ukupnaTezina < weights[v]:
                    weights[v] = ukupnaTezina
                    path[v] = cvor
                    h.heappush(queue, (ukupnaTezina, v))
    return weights[poc]

s1=int(input())
for i in range(s1):
	n=int(input())
	s=[]
	gradovi={}
	l=[[] for i in range(n)]
	for i in range(n):
		gradovi[str(input())]=i
		p=int(input())
		for j in range(p):
			do,t=map(int,input().split())
			l[i].append((do-1,t))
	r=int(input())
	for i in range(r):
		x=str(input())
		x=x.split(' ')
		s.append(dijkstra(l,gradovi[x[0]],gradovi[x[1]]))
	for i in s:
		print(i)