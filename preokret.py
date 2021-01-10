n=int(input())
t1=0
t2=0
iz=1
key1=True
key2=True
p1=0
p2=0
bit1=0
bit2=0
razlika=[]
for i in range(n):
    z=int(input())
    if z==1:
        t1+=1
        key1=True
        if t2>t1:
            bit1=1
        if key1==True and bit1==1:
            p1+=1
        if key2==True and t2>t1:
            razlika.append(p2)
            p2=0
            key2=False
            bit2=0
        
        
        
        
        
        
    if z==2:
        t2+=1
        key2=True
        if t2<t1:
            bit2=1
        if key2==True and bit2==1:
            p2+=1
        if key1==True and t1>t2:
            razlika.append(p1)
            p1=0
            key1=False
            bit1=0
        
        
        
        
        
    if t1==t2:
        iz+=1
    if i==n-1:
        if t1>t2:
            razlika.append(p1)
        if t2>t1:
            razlika.append(p2)
    #print(p1,p2)
print(t1,t2)
print(iz)
print(razlika)