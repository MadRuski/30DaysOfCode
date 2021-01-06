#HONI 2019/2020 2.kolo 2.zadatak radio.py
n,o=map(int,input().split())
for i in range(n):
    a,b=map(int,input().split())
    razlika=a-b
    o=o-razlika
print(o)