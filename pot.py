n=int(input())
zbroj=0
for i in range(n):
	broj=int(input())
	zbroj+=(broj//10) ** (broj%10)
print(zbroj)