num = input("Enter 5 numbers")
num1 = num.split(' ')
sum = 0
for i in num1:
	sum = sum + int(i)
print("The sum of the numbers:",sum)
