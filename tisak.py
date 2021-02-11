#1 zad zup sa 3. raz 2020.
n=int(input())
rec=[]
string=''
redak=0
for i in range(n):
	rec.append(list(map(str,input().split())))
red,duljina=map(int,input().split())
d=duljina-2

for i in range(n):

	for j in range(len(rec[i])):

		if len(rec[i][j])+1<=d:
			string+=rec[i][j]+'.'
			d-=len(rec[i][j])+1

		elif len(rec[i][j])==d:
			string+=rec[i][j]
			d=0

		if j!=len(rec[i])-1:
			if len(rec[i][j+1])>d:
				print('|'+string+'.'*d+'|')
				redak+=1
				string=''
				d=duljina-2

		if j==len(rec[i])-1:
			print('|'+string+'.'*d+'|')
			redak+=1
			string=''
			d=duljina-2
	if n>1:
		print('|'+(duljina-2)*'.'+'|')
		redak+=1

for i in range(red-redak):
	print('|'+(duljina-2)*'.'+'|')


