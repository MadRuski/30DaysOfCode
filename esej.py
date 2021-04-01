a,b=map(int,input().split(' '))
ab=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
rec=''
c=0
g=c
for i in range(b):
	while True:
		if g>=len(ab):
			rec+=ab[(g//26)%25]
			g=g-(g//26)*26

		else:
			rec+=ab[g]
			break
	c+=1
	g=c
	rec+=' '
print(rec)
