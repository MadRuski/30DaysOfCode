n=int(input())
n2=int(input())
l1=[]
l2=[]
suma=0
for i in range(n2):
	l1.append(int(input()))
for i in range(5):
	l2.append(int(input()))
for i in range(n2):
	if l1[i] in l2:
		suma+=1
if suma!=0:
	print(suma)
else:
	print(1)