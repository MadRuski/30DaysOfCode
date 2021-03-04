n=str(input())
l=''
bit=0
while len(n)!=0:
    if bit!=1:
        l+=n[len(n)-1]
        n=n[:len(n)-1]
        bit=1
    else:
        l+=str(abs(int(n[len(n)-1])%-10))
        n=str(abs(int(n)//-10))
        bit=0

print(l[len(l):0:-1]+l[0])
