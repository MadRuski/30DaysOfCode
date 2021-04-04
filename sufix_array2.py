# r i n su stringovi. r je str u kojem zelimo naci sve indexe instanca stringa n
#p=str(input())
#d=str(input())
def suffix(r,n):
	l={}
	mali=0
	rez=[]
	suma=1

	for i in range(len(r)):
		l[ r[i:] ]=i
	veli=len(l)
	l=sorted(l.items())

	while True:
		if len(l)==0:
			return -2
			break
			
		if veli-mali==1:
			return -1
			break

		if l[(mali+veli)//2][0][:len(n)]>n:
			veli=(mali+veli)//2

		if l[(mali+veli)//2][0][:len(n)]<n:
			mali=(mali+veli)//2

		if l[(mali+veli)//2][0][:len(n)]==n:
			rez.append(l[(mali+veli)//2][1])
			while True:

				if ((mali+veli)//2)-suma>-1 and l[((mali+veli)//2)-suma][0][:len(n)]==n:
					rez.append(l[((mali+veli)//2)-suma][1])

				if ((mali+veli)//2)+suma<len(l) and l[((mali+veli)//2)+suma][0][:len(n)]==n:
					rez.append(l[((mali+veli)//2)+suma][1])

				else:
					break

				suma+=1
			break
			

	if len(rez)!=0:
		return rez
#print(suffix(p,d))