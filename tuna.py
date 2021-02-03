#zadatak 3. sa honi 2016/2017 5.kolo tuna.py
n=int(input())
r=int(input())
v=0
for i in range(n):
	t=list(map(int,input().split()))
	if abs(t[0]-t[1])>r:
		nt=int(input())
		v+=nt
	else:
		v+=max(t)
print(v)
