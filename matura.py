sat,minuta=map(int,input().split())
vrijeme=int(input())
u1=input().split(' ')
u2=input().split(' ')
u3=input().split(' ')
u1=int(u1[0])*60+int(u1[1])
u2=int(u2[0])*60+int(u2[1])
u3=int(u3[0])*60+int(u3[1])
v=sat*60+minuta
v2=v+vrijeme
if u1>=v+30 and u1<v2-15:
	print('DA')
else:
	print('NE')

if u2>=v+30 and u2<v2-15:
	print('DA')
else:
	print('NE')

if u3>=v+30 and u3<v2-15:
	print('DA')
else:
	print('NE')