# reverse a given number

def rev_num(num):
	rev = 0
	while num > 0:
		reminder = num % 10
		rev = (rev * 10) + reminder
		num = num // 10
	return rev


print(f"reverse of the given number is {rev_num(56789)}")





# reverse a number user input

s = int(input("Enter a number: "))


def rev_num(num):
	rev = 0
	while num > 0:
		reminder = num % 10
		rev = (rev * 10) + reminder
		num = num // 10
	return rev

print(f"reverse of the given number is {rev_num(s)}")

