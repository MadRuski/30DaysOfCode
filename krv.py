#1.zad sa zupanijskog 2015
n=int(input())
krv=list(map(str,input().split()))
l=['A0','AA', 'B0', 'BB', 'AB', '00']
suma=0
s=[]

for i in krv:
	if 'AB' in i:
		print('AB', end=' ')
	elif 'A' in i:
		print('A', end=' ')
	elif 'B' in i:
		print('B', end=' ')
	elif '0' == i[0]:
		print('0', end=' ')

for i in range(len(l)):
	for j in range(len(l)):
		for x in range(n):
			if krv[x][0] in l[i]:
				if krv[x][1] in l[j]:
					suma+=1
			elif krv[x][0] in l[j]:
				if krv[x][1] in l[i]:
					suma+=1
		s.append(suma)
		suma=0
print('\n'+str(max(s)))