import random
n1=int(input('Koliko testova zelite napraviti? '))
n=int(input('Koliko pokusaja? '))
l=[]
c=0
for i in range(n1):

	for j in range(n):
		x=random.randint(1,365)
		if x not in l:
			l.append(x)
		else:
			c+=1
			l=[]
			break
	l=[]
		

print(c,str((c/n1)*100)+'%',str(100-(c/n1)*100)+'%')