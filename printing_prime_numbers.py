#  Prime Number

# Prime numbers are numbers that have only 2 factors: 1 and themselves. For example, the first 5 prime numbers are 2, 3, 5, 7, and 11.

lower = 100
upper = 200

for num in range(lower, upper+1):
	if num > 1:
		for i in range(2, num):
			if num % i == 0:
				break
		else:
			 print(num)	




























# lower = 100
# upper = 150

# for num in range(lower, upper+1):
# 	if num > 1:
# 		for i in range(2, num):
# 			if num % i == 0:
# 				break
# 		else:
# 			print(num)