import random
l=[]
for i in range(100):
	r=random.randint(1,1000)
	if r not in l:
		l.append(r)

l.sort()
print(l)
n=int(input())

def bs(l,n):
	mali=0
	veli=len(l)-1
	while True:
		if veli-mali==1:
			return -1
			break

		if l[(mali+veli)//2]>n:
			veli=(mali+veli)//2

		if l[(mali+veli)//2]<n:
			mali=(mali+veli)//2

		if l[(mali+veli)//2]==n:
			return (mali+veli)//2
			break
a=bs(l,n)
print(a)


	
