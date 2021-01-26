#zad 8.raz 2 sa skolskog 2018.
b=int(input())
lb=[]
suma=0
l=[['','','','','','','',''],
   ['','','','','','','',''],
   ['','','','','','','',''],
   ['','','','','','','',''],
   ['','','','','','','',''],
   ['','','','','','','',''],
   ['','','','','','','',''],
   ['','','','','','','','']]
for i in range(b):
	x,y=map(int,input().split())
	l[x-1][y-1]='b'
	lb.append([x-2,y])
c=int(input())
for i in range(c):
	x,y=map(int,input().split())
	l[x-1][y-1]='c'
'''
for i in range(8):
	print(l[i])
'''
for i in range(b):
	if l[lb[i][0]] [lb[i][1]-2]=='c':
		l[lb[i][0]] [lb[i][1]-2]=''
		suma+=1
	if l[lb[i][0]] [lb[i][1]]=='c':
		l[lb[i][0]] [lb[i][1]]=''
		suma+=1
print(suma)