r,s=list(map(int,input().split()))
l=[]
suma=0
for i in range(r):
    l.append(list(str(input())))
for i in range(1,r-1):
    for j in range(1,s-2):
        #print(l[i+1][j-1:j+3])
        if l[i][j]=="#":
            if l[i][j+1]=="#":
            	if "#" not in l[i-1][j-1:j+3] and "#" not in l[i+1][j-1:j+3]:
            		if "#" != l[i][j-1] and "#" != l[i][j+2]:
            			suma+=1
print(suma)
