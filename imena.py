n=int(input())
recenica=str(input())

recenica=recenica.split('.')
recenica=' '.join(recenica)

recenica=recenica.split('?')
recenica=' '.join(recenica)

recenica=recenica.split('!')
recenica=' '.join(recenica)

recenica=recenica.split('  ')
b=0
for i in range(len(recenica)):
	recenica[i]=recenica[i].split(' ')
	
	for j in range(len(recenica[i])):
		if len(recenica[i][j])>0:
			if recenica[i][j][0].isupper()==True:
				
				if recenica[i][j][1:].islower()==True and recenica[i][j][1:].isalpha()==True:
					b+=1
	print(b)
	b=0
