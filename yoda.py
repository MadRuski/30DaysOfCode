#honi kolo.4 2016 3.zad
pbroj=list(str(input()))
dbroj=list(str(input()))
jej1=''
jej2=''

if len(pbroj)>len(dbroj):
	dbroj.insert(0,'0'*abs(len(pbroj)-len(dbroj)))

if len(pbroj)<len(dbroj):
	pbroj.insert(0,'0'*abs(len(pbroj)-len(dbroj)))
	

for i in range(len(dbroj)):
	if int(pbroj[i])>int(dbroj[i]):
		jej1+=pbroj[i]
	if int(pbroj[i])<int(dbroj[i]):
		jej2+=dbroj[i]
	if int(pbroj[i])==int(dbroj[i]):
		jej2+=dbroj[i]
		jej1+=pbroj[i]

if jej1=='':
	print('YODA')
elif jej1!='':
	print(int(jej1))

if jej2=='':
	print('YODA')
elif jej2!='':
	print(int(jej2))
