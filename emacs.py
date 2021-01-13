#HONI 2019/2020 5.KOLO 3.ZAD emacs.py
x,y=map(int,input().split())
l=[]
for i in range(x):
    l.append(list(str(input())))
    #print(l[i])
b=0
for i in range(x):
    for j in range(y):
        if l[i][j]=='*':
            l[i][j]=''
            for ax in range(x-i):
                if l[i+ax][j]=='.':
                        break
                for ay in range(y-j):
                    if l[i+ax][j+ay]=='*':
                        l[i+ax][j+ay]=''
                    if l[i+ax][j+ay]=='.':
                        break
            b+=1
            
print(b)          
                    
            
