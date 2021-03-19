p1=['b', 'f', 'p', 'v']
p2=['c', 'g', 'j', 'k', 'q', 's', 'x', 'z']

sg=['$']
l=[]
n=int(input())
for i in range(n):
	ime=list(str(input()))
	ps=ime[0]
	ime[0]=ime[0].lower()
	for j in range(len(ime)):
		if ime[j] in p1 and sg[len(sg)-1]!='1':
			sg.append('1')

		elif ime[j] in p2 and sg[len(sg)-1]!='2':
			sg.append('2')

		elif ime[j] in ['d','t'] and sg[len(sg)-1]!='3':
			sg.append('3')

		elif ime[j] == 'l' and sg[len(sg)-1]!='4':
			sg.append('4')

		elif ime[j] in ['m','n'] and sg[len(sg)-1]!='5':
			sg.append('5')

		elif ime[j] == 'r' and sg[len(sg)-1]!='6':
			sg.append('6')
	if ps in ['A','E','I','O','U','Y','W','H']:
		sg[0]=ps
	else:
		sg[:2]=ps

	if len(sg)<=4:
		sg.append('0'*(4-len(sg)))
	else:
		sg=sg[:4]
	l.append(''.join(sg))
	sg=['$']
for i in l:
	print(i)