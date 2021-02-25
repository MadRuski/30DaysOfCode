dan,mjesec,godina=map(int,input().split())
sdan=dan
smjesec=mjesec
sgodina=godina
def normal(dan,mjesec,godina):
	m30=[6,4,9,11]
	#print(dan,mjesec,godina)
	if dan==31 and mjesec in m30:
		dan=1
		mjesec+=1
		

	elif dan==32 and mjesec!=2 and mjesec!=12:
		dan=1
		mjesec+=1
		

	elif mjesec==2 and dan==29 and godina%4!=0:
		dan=1
		mjesec=3
		

	elif mjesec==2 and dan==30:
		if godina%100!=0 or godina%400==0:
			dan=1
			mjesec=3
			
	elif mjesec==12 and dan==32:
		mjesec=1
		dan=1
		godina+=1
		
	return dan,mjesec,godina;

def sat(dan,mjesec,godina):
	if mjesec==12 and dan==32:
		mjesec=1
		dan=1
		godina+=1
	elif dan==32:
		dan=1
		mjesec+=1
		
	return dan,mjesec,godina;

tocno1=0

while True:
	dan,mjesec,godina=normal(dan,mjesec,godina)
	sdan,smjesec,sgodina=sat(sdan,smjesec,sgodina)
	#print(dan,mjesec,godina,'            ',sdan,smjesec,sgodina)
	if sdan!=dan and tocno1==0:
		print(dan,mjesec,godina)
		tocno1=1
	if tocno1 and sdan==dan:
		print(dan,mjesec,godina)
		break
	dan+=1
	sdan+=1
