n=int(input())
suma=0
jakov=list(map(int,input().split()))
jakov=(jakov[0]*60)+jakov[1]
for i in range(n):
    u=list(map(int,input().split()))
    u=(u[0]*60)+u[1]
    if u>jakov:
        suma+=1
print(suma)
        
