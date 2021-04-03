r=str(input())
n=str(input())

def suffix(r,n):
	l={}
	mali=0
	rez=[]
	bit=False

	for i in range(len(r)):
		l[ r[i:] ]=i
	veli=len(l)
	l=sorted(l.items())

	while True:
		if len(l)==0:
			return -2
			break
			
		if veli-mali==1:
			if bit==False:
				return -1
			break

		if l[(mali+veli)//2][0][:len(n)]>n:
			veli=(mali+veli)//2

		if l[(mali+veli)//2][0][:len(n)]<n:
			mali=(mali+veli)//2

		if l[(mali+veli)//2][0][:len(n)]==n:
			rez.append(l[(mali+veli)//2][1])
			del l[(mali+veli)//2]

			veli=len(l)
			mali=0
			bit=True

	if len(rez)!=0:
		return rez
		

print(suffix(r,n))