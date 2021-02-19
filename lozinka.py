n=int(input())
rijeci=[]
r=[]
for i in range(n):
	unos=str(input())
	rijeci.append(unos)
	if unos[len(unos)::-1] in rijeci:
		r=[len(unos),unos[len(unos)//2]]
print(r[0],r[1])