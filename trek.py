od=int(input())
do=int(input())
inp=[od,do]
if od<=7 and do<=7:
	a=((max(inp)-min(inp))%5)*10
	if a==40:
		a=30
	if a==0:
		a=20
	print(a)
elif od>7 and do>7:
	a=((max(inp)-min(inp))%5)*30
	if a==120:
		a=90
	if a==0:
		a=60
	b=(((max(inp)-7)-(min(inp)-7))%5)*10
	if b==40:
		b=30
	if b==0:
		b=20
	b+=40
	print(max(a,b))
elif od>7 or do>7:
	b=(((max(inp)-7)-min(inp))%5)*10
	if b==40:
		b=30
	if b==0:
		b=20
	b+=20
	print(b)