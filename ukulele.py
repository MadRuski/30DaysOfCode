#zad sa zupanijskog 2017g 3 razredi
l=[]
for i in range(4):
	l.append(list(str(input())))
for i in range(len(l[i])):
	for j in range(4):
		if l[j][i]=='0':
			print(j+1)
			break
