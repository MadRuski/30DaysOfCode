#HONI 2019/2020 4.kolo 2.zadatak amazon.py
n=int(input())
b=int(input())
p=0
suma=1
for i in range(b):
    k=int(input())
    p+=k
    if p>n:
        p=k
        suma+=1
print(suma)