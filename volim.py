k=int(input())
n=int(input())
t=210
l=[]
for i in range(n):
	v,o=map(str,input().split(' '))
	l.append(int(v))
	l.append(o)
for i in range(0,n*2,2):

	if l[i+1]=='N' or l[i+1]=='P':
		t-=l[i]

	if  l[i+1]=='T':
		t-=l[i]
		if t<=0:
			if k%8==0:
				print(8)
			else:
				print(k%8)
			break
		k+=1

	

	
