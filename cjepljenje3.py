def bs(l,n):
	mali=0
	veli=len(l)
	while True:
		if len(l)==0:
			return -2
			break
			
		if veli-mali==1:
			l.insert(veli,n)
			
			return l
			break

		if l[(mali+veli)//2]>n:
			veli=(mali+veli)//2

		if l[(mali+veli)//2]<n:
			mali=(mali+veli)//2

		if l[(mali+veli)//2]==n:
			#l[(mali+veli)//2-1]+=1
			return l
			break

		    
n,m=map(int,input().split())
poz2=[-1,9]
brojac=0
maxi=[0 for i in range(m)]
for i in range(m):
    unos=int(input())
    poz2=bs(poz2,unos-1)
    for j in range(1,len(poz2)):
        if poz2[j]-poz2[j-1]-1>maxi[i]:
            maxi[i]=poz2[j]-poz2[j-1]-1
            #print('maxi',maxi)
for i in maxi:
    print(i)