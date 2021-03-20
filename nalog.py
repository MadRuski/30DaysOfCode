c=int(input())
n=int(input())
l=[]
dani=[0,31,59,90,120,151,181,212,243,273,304,334]
c1=c-n*100
c1=c1//100

for i in range(n):
	s=str(input())
	s=s[:5]
	s=s.split('.')
	l.append(int(s[0])+dani[int(s[1])-1])

for i in range(len(l)):
	if l[i]+c1>365:
		c1=c1-(365-l[i])
		l[i]=365
	elif l[i]+c1<=365:
		l[i]+=c1
		c1=0
		break

for i in range(len(l)):
	for j in range(len(dani)-1,-1,-1):
		if l[i]>dani[j]:
			if l[i]-dani[j]<10:
				print('0'+str(l[i]-dani[j]),end='.')
			else:
				print(str(l[i]-dani[j]),end='.')
			if j<9:
				print('0'+str(j+1)+'.')
			else:
				print(str(j+1)+'.')
			break