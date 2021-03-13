x,y=map(int,input().split())
l=[]
for i in range(x):
	l.append(list(str(input())))

for i in range(x):
	for j in range(y):
		if l[i][j]=='#':
			if l[i][j+1]=='.':
				l[i][j+1]='O'

			if l[i+1][j+1]=='.':
				l[i+1][j+1]='O'

			if l[i+1][j]=='.':
				l[i+1][j]='O'
#print(l)

for i in range(x):
	for j in range(y):
		if l[i][j]=='O':
			l[i][j]='#'
		if j==y-1:
			print(l[i][j])
			continue
		print(l[i][j],end='')


