n,m=map(int,input().split())
j=[]
for i in range(m):
	u=str(input())
	u=u.split(' ')
	if u[0]=='1' and u[2]=='1':
		j.append(int(u[1]))
	elif int(u[0])>1:
		for i in range(2,len(u),2):
			if u[i]=='1':
				if int(u[i-1]) not in j:
					j.append(int(u[i-1]))
				break
for i in range(n-1):
	if i+1 in j:
		print('1',end=' ')
	else:
		print('0',end=' ')
if n in j:
	print('1')
else:
	print('0') 