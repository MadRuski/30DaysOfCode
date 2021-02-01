#honi 2014/2015 kolo 1. 3.zadatak
n=int(input())
b=list(map(int,input().split()))
l=[]
suma=0
for i in range(1,n+1):
	f=i*b[i-1]
	l.append(f-suma)
	suma+=f-suma
for i in range(n):
	if i != n-1:
		print(l[i], end=' ')
	else:
		print(l[i])