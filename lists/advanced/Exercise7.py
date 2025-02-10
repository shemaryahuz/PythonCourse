# Ask the user to enter 10 numbers into a list.
# Print whether the list is sorted in ascending order or in no specific order.
# If the numbers in the list are in ascending order, print the sum of all the elements
# in the list
# If there is no specific order, print the average of all the numbers in the list


numbers = []
sum_nums = 0
amount_nums = 0
num = int(input("Please enter a number:"))
numbers.append(num)
sum_nums += num
amount_nums += 1

temp = num
is_not_order = False

for i in range(1,10):
    num = int(input("Please enter a number:"))
    numbers.append(num)
    sum_nums += num
    amount_nums += 1
    if num != temp + 1:
        is_not_order = True
    temp = num
print(numbers)
if is_not_order:
    print("There is no specific order")
    print("The average of the numbers is", sum_nums / amount_nums)
else:
    print("There is ascending order")
    print("The sum of the numbers is", sum_nums)
