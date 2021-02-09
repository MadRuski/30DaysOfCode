#1.zad sa skolskog 3/4 razredi
s,r=map(int,input().split())
l=[]
brojac=0
xd=[]
for i in range(r+2):
	xd.append('.')

l.append(xd)
for i in range(s):
	l.append(list(str(input())))
	l[i+1].append('.')
	l[i+1].insert(0,'.')

l.append(xd)

for i in range(s+2):
	for j in range(r+2):
		if l[i][j] == "#":
			if l[i][j+1] == "#":

				if '#' not in l[i+1][j-1:j+3] and '#' not in l[i-1][j-1:j+3]:
					
					if l[i][j-1] == '.' and l[i][j+2] == '.':
						brojac+=1

			elif l[i+1][j] == "#":
				
				if '#' not in l[i+2][j-1:j+2] and '#' not in l[i-1][j-1:j+2]:

					if l[i][j-1] != '#' and l[i][j+1] != '#' and l[i+1][j-1] != '#' and l[i+1][j+1] != '#':
						brojac+=1

print(brojac)
