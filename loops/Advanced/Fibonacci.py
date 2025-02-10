#Ask the user for a number.
#Print numbers in the Fibonacci series starting from 1 so that the number of terms in the series is the number he entered.
#Print the series in one line.

num = int(input("Please enter a natural number:"))

pre_num1 = 1
pre_num2 = 0
for i in range(num):
    temp = pre_num1 + pre_num2
    print(temp, end= " ")
    pre_num1 = pre_num2
    pre_num2 = temp
