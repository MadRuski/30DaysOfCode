unos=str(input())
l=[]
for i in unos:
	if i.isupper() is True:
		l.append(i)
print(''.join(l))