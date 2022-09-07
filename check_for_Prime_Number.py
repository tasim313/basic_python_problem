number = int(input("How many name you will check: "))

for i in range(number):
    text = input("enter a your name :")
    value = int(input("enter a your number :"))
    ascii_values = []
    for character in text:
        ascii_values.append(ord(character))
    new_list = []
    for i in ascii_values:
        new_list.append(i)
     

num =new_list[0]+value

flag = False

if num > 1:
    
    
    for i in range(2, num):
        if (num) % i == 0:
            flag = True
            break

if flag:
    print("YES")
else:
    print("No")