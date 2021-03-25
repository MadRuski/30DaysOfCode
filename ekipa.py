n,m,k=map(int,input().split())
d=[0 for i in range(n)]
zbroj=0
for i in range(m):
	u=input().split(' ')
	for j in range(0,len(u),2):
		if d[int(u[j])-1]<float(u[j+1]):
			d[int(u[j])-1]=float(u[j+1])
for i in range(k):
	zbroj+=max(d)
	d.remove(max(d))
print(zbroj)