n=int(input())
m=int(input())
agenti=[[0 for j in range(m)] for i in range(n)]
agenti.insert(0,[0 for j in range(n)])


count=0
for i in range(m):
    u=str(input())
    u=u.split(' ')
    
    if u[0]=='A':
        for j in u[2:]:
            agenti[int(j)][i]=1
            agenti[0][int(j)-1]+=1
        count+=1

    elif u[0]=='B':
        maxi=0
        point=[]
        for j in u[2:]:
            if agenti[0][int(j)-1]>maxi:
                maxi=agenti[0][int(j)-1]
                point=agenti[int(j)].copy()
        if len(point)!=0:
            for j in u[2:]:
                agenti[int(j)]=point.copy()
                agenti[0][int(j)-1]=maxi

if max(agenti[0])>count:
    print('0')
else:
    for i in range(n):
        if agenti[0][i] == max(agenti[0]):
            print(i+1)

print(max(agenti[0]),count)
