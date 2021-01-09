n=int(input())
c=[]
b1=[]
l=[]
for i in range(n):
    h,b=map(int,input().split())
    b1.append(b)
    c.append([])
    c[i]=list(map(int,input().split()))
    c[i].sort()
    


for i in range(n):
    for j in range(len(c[i])):
        if b1[i]-sum(c[i])>=0:
            l.append(len(c[i]))
            break
        if b1[i]-c[i][0]<0:
            l.append(0)
            break
        if b1[i]-sum(c[i][:j+1])<0:
            l.append(j)
            break
        
        
    print('Case #'+str(i+1)+':',l[i])
