x,y=map(int,input().split())
l=[]
c=0
poz=[]
for i in range(x):
	l.append(list(str(input())))
	l[i].insert(0,'.')
	l[i].append('.')
l.append(list('.'*(y+2)))
l.insert(0,list('.'*(y+2)))
for i in range(1,x+1):
	for j in range(1,y+1):
		
		if l[i][j]=='X':
			if l[i-1][j]=='.':
				c+=1
			if l[i+1][j]=='.':
				c+=1
			if l[i][j-1]=='.':
				c+=1
			if l[i][j+1]=='.':
				c+=1
			
		if c>=3:
			l[i][j]='$'
		c=0

for i in range(len(l)-1,-1,-1):
	if 'X' not in l[i]:
		del l[i]
		continue

	for j in range(len(l[i])):
		if l[i][j]=='X':
			poz.append(j)

		if l[i][j]=='$':
			l[i][j]='.'

if len(poz)!=0:
	for i in l:
		print(''.join(i[min(poz):max(poz)+1]))
else:
	for i in l:
		print(''.join(i))