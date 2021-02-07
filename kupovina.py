#1.zad sa skolskog 2013
t=["pon", "uto", "sri", "cet", "pet","sub", "ned"]
ex=[]
nikola=0
lucija=0


dan=str(input())
n=int(input())
for i in range(n):
	ex.append(int(input()))

trenutacni_dan=t.index(dan)
j=1

while j<31:
	if j in ex:
		lucija+=1

	elif trenutacni_dan==6 or trenutacni_dan==5:
		nikola+=1

	elif j%2==1:
		lucija+=1
	elif j%2==0:
		nikola+=1

	if trenutacni_dan==6:
		trenutacni_dan=0
	elif trenutacni_dan!=6:
		trenutacni_dan+=1
	
	j+=1
print(nikola, lucija)
