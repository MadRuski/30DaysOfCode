import decimal
x=1
y=1
while True:
	if len(str(x))+len(str(y))>32:
		print(str(x)[:15],str(y)[:15])
	else:
		print(x,y)
	print(decimal.Decimal(x) / decimal.Decimal(y))
	x+=y
	y=x-y