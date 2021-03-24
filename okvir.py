m,n=map(int,input().split())
u,l,r,d=map(int,input().split())
k=[]
for i in range(m):
	k.append(str(input()))
s=''
mat=[]
for i in range(m+u+d):
	mat.append([])
	if i%2==0:
			mat[i].append('#')
	if i%2==1:
		mat[i].append('.')

	for j in range(n+l+r-1):
		if mat[i][j]=='#':
			mat[i].append('.')

		elif mat[i][j]=='.':
			mat[i].append('#')

for i in range(len(k)):
	del mat[u+i][abs(l-1):n+1]
	mat[u+i].insert(l,k[i])

for i in mat:
	print(''.join(i))