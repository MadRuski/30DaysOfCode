god=int(input())
if god==2020:
	print('NE')

elif god%4==0:
	print('DA')
	razlika=god-2020
	print(razlika//4)

else:
	print('NE')