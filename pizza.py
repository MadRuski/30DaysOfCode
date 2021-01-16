o=list(map(int,input().split()))
o.pop(0)
p=int(input())
suma=0
for i in range(p):
    r=list(map(int,input().split()))
    r.pop(0)
    suma=suma+1
    for i in range(len(r)):
        if r[i] in o:
            suma-=1
            break
print(suma)
    
