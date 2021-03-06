s=str(input())
l=[]
l1=['..#.','.#.#','#.'+s[0]+'.','.#.#','..#.']
brojac=1
for i in range(1,len(s)):
	if (i+1)%3==0:
		l=['..*.','.*.*','*.'+s[i]+'.','.*.*','..*.']
	if (i+1)%3!=0:
		l=['..#.','.#.#','#.'+s[i]+'.','.#.#','..#.']
	for j in range(5):
		l1.insert(brojac*(j+1)+j,l[j])
	brojac+=1
n=0
for i in range(5):
	if i==2:
		if len(s)%3==0:
			print(''.join(l1[n:n+len(s)])+'*')
		else:
			print(''.join(l1[n:n+len(s)])+'#')
	else:
		print(''.join(l1[n:n+len(s)])+'.')
	n+=len(s)