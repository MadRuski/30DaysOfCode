r=list(str(input()))
r.sort()
duzina=[]
duzina.append(len(r))
epoint=0

s=""
l=[]
i=0
b=0

while len(l)<duzina[0]:
	#print(l,r)
	if len(r)==1 and r[0] in l:
		l.insert(0,'@')
		for i in range(len(l)-2, -1, -1):
			
			if l[i+1]!=r[0] and l[i]!=r[0]:
				
				l.insert(i+1,r[0])
				l.pop(0)
				r.pop(0)
				epoint=2
				break
	if epoint==1 or epoint==2:
            break
	if r[i]!=s:
		l.append(r[i])
		s=r[i]
		r.pop(i)
		i=0

	else:
		i+=1
    
	if len(r)>1:
		for j in set(r):
			b+=1
			if j==s and b==len(set(r)):
				print(-1)
				epoint=1
				break
			else:
				break
            	
		b=0
        
if epoint!=1:
	print("".join(l))
