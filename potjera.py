n=int(input())
ldc=8
ndc=6
lose=0
for i in range(n):
	n,l=map(str,input().split())
	if n=="t":
		ndc-=1
	if l=="t":
		ldc-=1
	if ldc==ndc:
		lose=1
if lose==1:
	print('ulovljen')
else:
	print('pobjegao')