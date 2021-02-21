#2.zad 3 i 4 skolsko
spilja=[]
prazno=0
pamti=0
x,y=map(int,input().split())
for i in range(x):
	red=list(str(input()))
	if '#' not in red:
		prazno+=1
	else:
		spilja.append(red)
'''
for i in range(len(spilja)):
	for j in range(y):
		if pamti==i-1:
				if '.' == spilja[i][j]:
					if spilja[i-1][j] == '#':
						spilja[i][j]=='#'

		elif '.' in spilja[i]:
			if '#' == spilja[i][j]:
				if spilja[i+1][j] == '.':
					pamti=i
				else:
					break
spilja.pop(pamti)
'''

for i in range(prazno):
	spilja.insert(0,list('.'*y))
for i in spilja:
	print(''.join(i))

