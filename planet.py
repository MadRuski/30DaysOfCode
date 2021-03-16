dani=int(input())
bp=int(input())
dani2=int(input())
dani=dani*24
suma=0
l=[1408,5832,24,25,10,11,17,16]
for i in l:
	if dani//i>dani2:
		suma+=1
print(dani//l[bp-1])
print(suma)