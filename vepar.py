n=int(input())
l=[]
r1=1
r2=1
for i in range(n):
    l=list(map(int,input().split()))
    for j in range(l[0],l[1]+1):
        r1=r1*j
    for j in range(l[2],l[3]+1):
        r2=r2*j
    
    if r2%r1==0:
        print('DA')
    else:
        print('NE')
        
    
