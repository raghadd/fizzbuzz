import math


for x in range(1,300):
	if x % 3:
		if x % 5:
			print(x)
		else:
			print(x, "buzz")
	else:
		print(x, "fizz")
