n=int(input())
o=int(input())
dio=round(o/((n-1)/n))-1
l=[]
for i in range(dio-1,n*o+1):
	if i//n==i-o:
		l.append(i)
print(min(l),max(l))