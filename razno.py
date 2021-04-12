from itertools import permutations
from itertools import combinations
import math
l=[1,2,3,4]

#3 i 2 su duljine permutacije ili kombinacije
def perm(perm): #perm je lista
	perm=permutations(l)
	for i in list(perm):
		print(i)

def comb(comb): #comb je lista
	comb=combinations(l,2)
	for i in list(comb):
		print(i)
		
def faktorial(n): #n je broj
	print(math.factorial(n))\

def gcd(a,b): #a i b su brojevi
	print('Najveci zajednicki djeljitelj je',math.gcd( a, b ))

def pow(a,b,c): #a, b, c su brojevi
	print(pow(a, b)) #(a**b)
	print(pow(a, b, c)) #(a**b) % c

#comb(l)
#perm(l)
#faktorial(4)
#gcd(5,15)