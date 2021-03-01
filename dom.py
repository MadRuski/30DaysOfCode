unos=list(str(input()))
z=['C','A','M','B','R','I','D','G','E']
i=0
while i!=len(z):
	if z[i] in unos:
		unos.remove(z[i])
	else:
		i+=1
print(''.join(unos))