print("hello")
number=5
for i in range(1,number+1):
	print()
	for j in range(1,i+1):
		print(j,end=" ")


for i in list(range(1,number)).reverse():
	print(i)
