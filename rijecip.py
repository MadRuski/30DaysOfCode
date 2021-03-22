a=1
b=0
n=int(input())
for i in range(n):
	b=a+b
	a=b-a
print(a,b)