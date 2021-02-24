n=int(input())
r=list(str(input()))
mirko=[]
slavko=[]
r1=''.join(r)

r1=list(r1)

r1.sort()

while len(r)>0:
	mirko.append(r[len(r)-1])
	r1.remove(r[len(r)-1])
	r.pop(len(r)-1)

	slavko.append(r1[0])
	r.remove(r1[0])
	r1.pop(0)


for i in range(len(mirko)):
	if mirko==slavko:
		print('NE')
		break
	if ord(mirko[i])<ord(slavko[i]):
		print('NE')
		break
	if ord(mirko[i])>ord(slavko[i]):
		print('DA')
		break

print(''.join(slavko))