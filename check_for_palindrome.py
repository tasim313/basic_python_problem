s = input ("Enter a string: ")

def palindrome(string):
	x = ""
	for i in string:
		x = i +x
	return x

if s == palindrome(s):
	print("It is a palindrome")
else:
	print("It is not a palindrome")


