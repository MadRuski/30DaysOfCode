n=int(input())
l=''
bit=0
while n!=0:
    if bit==0:
        l+=str(abs(n%10))
        n=abs(n//10)
        bit=1
    else:
        l+=str(abs(n%-10))
        n=abs(n//-10)
        bit=0
print(l[len(l):0:-1]+l[0])
