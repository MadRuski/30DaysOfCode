#testni zad sa zup probe baloni.py
n,m=map(int,input().split())
crv=[]
plav=[]
minc=10**10
#maxc=-1
point=0
minp=10**10
#maxp=-1
suma=0
for i in range(n):
	c1,c2,p1,p2=map(int,input().split())
	crv.append([c1,c2])
	plav.append([p1,p2])
	if c1<minc:
		minc=c1
	if p1<minp:
		minp=p1
	'''
	if c2>maxc:
		maxc=c2
	if p2>maxp:
		maxp=p2
	'''
for i in range(minc,m+1):
	for j in range(minp,m+1):
		for x in range(n):
			if crv[x][0]<=i and crv[x][1]>=i:
				point+=1
			elif plav[x][0]<=j and plav[x][1]>=j:
				point+=1
		if point==n:
			suma+=1
			point=0
		if point!=n:
			point=0
print(suma)