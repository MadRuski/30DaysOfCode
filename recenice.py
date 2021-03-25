n=int(input())
l=[]
c=-1
for i in range(n):
	a=str(input())
	c+=len(a)
	l.append(a)
c1=c
d=''
jed=['','jedan', 'dva', 'tri', 'cetiri', 'pet', 'sest', 'sedam', 'osam','devet', 'deset','jedanaest', 'dvanaest', 'trinaest', 'cetrnaest', 'petnaest','sesnaest', 'sedamnaest', 'osamnaest', 'devetnaest']
des=['dvadeset','trideset', 'cetrdeset', 'pedeset', 'sezdeset', 'sedamdeset', 'osamdeset', 'devedeset']
sto=['sto', 'dvjesto','tristo', 'cetiristo', 'petsto', 'sesto', 'sedamsto', 'osamsto','devetsto']

while True:
	if c1<20:
		d=jed[c1]

	elif c1>=20 and c1<100:
		d=des[c1//10-2]+jed[c1%10]

	elif c1>=100:
		d=sto[c1//100-1]

		if c1%100<20:
			d+=jed[c1%100]

		elif c1%100>=20:
			d+=des[(c1%100)//10-2]+jed[(c1%100)%10]

	if len(d)+c==c1:
		break

	else:
		c1+=1
		
l[l.index('$')]=d
print(' '.join(l))