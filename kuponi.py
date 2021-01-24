#1 zad sa zup 2016
k=[]
k2=[]
t=1000
for i in range(3):
	p=str(input())
	if '%' in p:
		p=p.strip('%')
		p=1-int(p)/100
		k.append(p)
	else:
		p=p.strip('kn')
		k2.append(int(p))
k.sort(reverse=True)
k2.sort()
k.append(1)
k2.append(0)
for i in range(3):
	pr=k[0]*t
	kr=t-k2[0]
	if pr>=kr:
		t=kr
		k2.pop(0)
	if pr<kr:
		t=pr
		k.pop(0)
print(t)