#zupanijsko 2020. 1 zadatak
o=int(input())
n=int(input())
s=list(map(int,input().split()))
b=0
if (sum(s)/n)+10**-7<o:
	while (sum(s)/n)+10**-7<o:
		s[s.index(min(s))]=5
		b+=1
		#print(s)

elif (sum(s)/n)+10**-7>o:
	while (sum(s)/n)+10**-7>o:
		s[s.index(max(s))]=1
		b+=1
		#print(s)
		
print('\n'+str(b))