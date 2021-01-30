#zadatak 1. sa zupanijskog 2018. 8.raz
t=str(input())
v=[]
m=[]
t=t.split('#')
suma=0

for i in t:
	if 'DOBRILA' in i:
		v.append(10)
		m.append(i.strip('DOBRILA'))
	if 'JELACIC' in i:
		v.append(20)
		m.append(i.strip('JELACIC'))
	if 'GUNDULIC' in i:
		v.append(50)
		m.append(i.strip('GUNDULIC'))
	if 'MAZURANIC' in i:
		v.append(100)
		m.append(i.strip('RADIC'))
	if 'RADIC' in i:
		v.append(200)
		m.append(i.strip('RADIC'))
	if 'MARULIC' in i:
		v.append(500)
		m.append(i.strip('MARULIC'))
	if 'STARCEVIC' in i:
		v.append(1000)
		m.append(i.strip('STARCEVIC'))

for i in range(len(v)):
	if m[i]=='':
		m[i]=1
	if m[i]!='':
		suma+=int(m[i])*v[i]
print(suma)
