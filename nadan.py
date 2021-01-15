#HONI 2018/2020. 1.KOLO 3.ZAD nadan.py
k=int(input())
n=int(input())
suma=0
for i in range(1,n+1):
    
    if i==n:
        print(k-suma)
    else:
        suma+=i
        print(i)
    
        
