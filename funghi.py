#honi 2015 5.kolo 3.zad funghi.py
l=[]
for i in range(8):
	l.append(int(input()))
l.extend(l[:3])
maxi=-1
for i in range(8):
	if sum(l[i:i+4])>maxi:
		maxi=sum(l[i:i+4])
print(maxi)