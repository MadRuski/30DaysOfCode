n=int(input())
p=str(input())
p=[p[0],p[2]]
l=[]
for i in range(n):
	unos=str(input())
	if unos[0]==p[0] and unos[len(unos)-1]==p[1]:
		l.append('DA')
	else:
		l.append('NE')
for i in l:
	print(i)