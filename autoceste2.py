o=int(input())
d={}
for i in range(o):
    mjesta=(str(input()))
    n=int(input())
    for j in range(n):
        tab=[]
        tab.extend(list(map(str,input().split())))
        
        tab[1]=''.join(tab[1].split(':'))

        if int(tab[0]) not in d.keys():
            d[int(tab[0])]=[tab[1]],[mjesta]  

        else:
            d[int(tab[0])][0].append(tab[1])
            d[int(tab[0])][1].append(mjesta)

mali=min(d)
for i in sorted(d.keys()):
    if i!=mali:
        print()
    print(i, end=' ')
    
    for j in range(len(d[i][0])):
        tablica=i
        nm=min(d[i][0])
        nm2=d[i][1][d[i][0].index(nm)]
        print(nm2,end=' ')
        print(nm[:2]+':'+nm[2:4]+':'+nm[4:6],end=' ')
        z=d[i][0].index(nm)
        d[tablica][0][z]=max(d[tablica][0])+'9'
        
        if j==len(d[i][0])-1:
            del d[tablica]
            
        else:
            print('->',end=' ')
        
