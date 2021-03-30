b2=['A','B','C']
b3=['D','E','F']
b4=['G','H','I']
b5=['J','K','L']
b6=['M','N','O']
b7=['P','Q','R','S']
b8=['T','U','V']
b9=['W','X','Y','Z']
zbroj=0
u=str(input())
for i in range(len(u)):
	if u[i] in b2:
		zbroj+=3
	elif u[i] in b3:
		zbroj+=4
	elif u[i] in b4:
		zbroj+=5
	elif u[i] in b5:
		zbroj+=6
	elif u[i] in b6:
		zbroj+=7
	elif u[i] in b7:
		zbroj+=8
	elif u[i] in b8:
		zbroj+=9
	elif u[i] in b9:
		zbroj+=10
print(zbroj)