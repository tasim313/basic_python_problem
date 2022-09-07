

# Bubble Sort 


arr = [7, 3, 9, 2, 0, 4, 8, 1, 6,5]


def bubbleSort(sequence):
	n = len (sequence)
	for i in range(n -1):
		for j in range(n -1 -i):
			if sequence[j] > sequence[j +1]:
				temp = sequence[j]
				sequence[j]=sequence[j+1]
				sequence[j+1] = temp
	return sequence


print(bubbleSort(arr))





























# arr = [7, 3, 9, 2, 0,100, 4, 8, 1, 6,5]

# def bubbleSort(sequence):
# 	n = len(sequence)
# 	for i in range (n - 1):
# 		for j in range(n -1 -i):
# 			if sequence[j] > sequence[j+1]:
# 			   temp = sequence[j]
# 			   sequence[j] = sequence[j+1]
# 			   sequence[j+1] = temp
# 	return sequence

# print(bubbleSort(arr))
