n=int(input())
rem=list(map(int,input().split()))
l=[]
l.extend(range(1,n+1))
for i in range(len(rem)):
	l.pop(rem[i]-1)
print(l[0])