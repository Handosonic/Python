
def duud():
	print("z")	

j = 1
for i in range(100):
	print('i: ',i)
	if(i is j):
		for i in range(j):
			duud()
		j += 1
