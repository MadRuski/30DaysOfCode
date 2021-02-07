a=int(input())
l = [ [ "0" for i in range(a) ] for j in range(a) ]
null=0
brojac=0

for i in range(a//2):

	for j in range(null,(a-null)-1):
		brojac+=1
		l[j][i*2-i]=str(brojac)

	for j1 in range(null,(a-null)-1):
		brojac+=1
		l[(a-null)-1][j1]=str(brojac)

	for j2 in range((a-null)-1,null,-1):
		brojac+=1
		l[j2][(a-null)-1]=str(brojac)

	for j3 in range((a-null)-1,null,-1):
		brojac+=1
		l[i*2-i][j3]=str(brojac)
	null+=1
	
if a%2==1:
	l[a//2][a//2]=str(a**2)
for i in l:
	print(" ".join(i))
