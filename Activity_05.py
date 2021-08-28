num = input("Enter 5 numbers")
number_string_list = num.split(' ')
sum = 0
for i in number_string_list:
	sum = sum + int(i)
print(sum)
