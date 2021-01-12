od=str(input())
do=str(input())
alph=[65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90]
l2=[]

l=[]
l.append(alph.index(ord(od[0])+1)*1000)
l[0]=l[0]+int(od.strip(od[0]))

l.append(alph.index(ord(do[0])+1)*1000)
l[1]=l[1]+int(do.strip(do[0]))

razlika=(l[1]-l[0])+1
#print(razlika)

s=int(input())
for i in range(s):
    #l2.append([])
    n=str(input())
    l2=alph.index(ord(n[0])+1)*1000
    l2=l2+int(n.strip(n[0]))
    if l2>=l[0] and l2<=l[1]:
        razlika=razlika-1
    l2=0
print(razlika)

