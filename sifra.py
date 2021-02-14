a=str(input())
kud=[]
od=[]
t=0
brojka=''
for i in range(len(a)):
	if ord(a[i])>=48 and ord(a[i])<=57:
		brojka+=a[i]
	else:
		if brojka!='':
			kud.append(brojka)
		brojka=''
if brojka!='':
		kud.append(brojka)
print(len(set(kud)))