n=int(input())
imena=[]
l=[]

for i in range(n):
	imena.append(str(input()))

n1=int(input())
for i in range(n1):
	todo=str(input())
	if "IZBACI" in todo:
		todo=todo.strip('IZBACI ')
		imena.remove(todo)
		
	elif "SALJI" in todo:
		todo=todo.strip('SALJI ')
		todo=todo.split(' ')
		
		prvi=abs(imena.index(todo[0])-imena.index(todo[1]))
		drugi=[imena.index(todo[0]),imena.index(todo[1])]
		drugi=abs((min(drugi)+n)-max(drugi))

		if prvi<drugi:
			l.append(prvi)

		if prvi>drugi:
			l.append(drugi)

		elif prvi==drugi:
			l.append(drugi)

for i in l:
	print(i)