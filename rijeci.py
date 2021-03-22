poc=['A']
bit=0
n=int(input())
for i in range(n):
	#print(poc)
	for j in range(len(poc)+poc.count('B')):

		if bit==1:
				bit=0
				continue

		if poc[j]=='A':
			poc[j]='B'

		elif poc[j]=='B':
			poc.insert(j+1,'A')
			bit=1

c=poc.count('B')
print(len(poc)-c,c)