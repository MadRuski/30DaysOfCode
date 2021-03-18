l=[]
k=['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'H']
k2=[4,3,3,3,2,2]
k3=[4,11,7,2,9,4]
prom=[]
for i in range(6):
	l.append(list(str(input())))
	l[i].pop(0)
	l[i].pop(len(l[i])-1)

for i in range(len(l[0])):
	for j in range(6):
		if l[j][i]!='-':
			num=l[j][i]

			if l[j][i+1]!='-':
				num+=l[j][i+1]
				l[j][i+1]='-'

			num=int(num)
			print(k[(k3[j]+num)%12],end='')
			print(k2[j]+((k3[j]+num)//12))
			break