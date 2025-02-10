# Get numbers from the user in a loop. The stop condition is the word "exit".
# Print in the menu:
# A. The amount of numbers he entered
# B. The sum of  the numbers he entered
# C. The amount of even numbers and also the amount of odd numbers
# D. The largest number and also the smallest number
# E. The average of all the numbers he entered



user_input = input("Please enter a number:")

amount = 1
sum_nums = 0
even_nums = 0
odd_nums = 0

if user_input == "exit":
    print("You can't exit, you haven't entered a number yet!")

    user_input =int(input("Please enter a number:"))

    sum_nums = int(user_input)
    if user_input == 0:
        even_nums = even_nums
        odd_nums = odd_nums
    elif user_input % 2 == 0:
        even_nums += 1
    else:
        odd_nums += 1

    large_num = user_input
    small_num = user_input

else:
    user_input = int(user_input)
    sum_nums = user_input
    if user_input == 0:
        even_nums = even_nums
        odd_nums = odd_nums
    elif user_input % 2 == 0:
        even_nums += 1
    else:
        odd_nums += 1

    large_num = user_input
    small_num = user_input

while user_input != "exit":

    user_input = input("Please enter a number or exit:")

    if user_input != "exit":
        user_input = int(user_input)
        amount += 1
        sum_nums += user_input
        if user_input == 0:
            even_nums = even_nums
            odd_nums = odd_nums
        elif user_input % 2 == 0:
           even_nums += 1
        else:
            odd_nums += 1

        if user_input > large_num:
            large_num = user_input
        elif user_input < small_num:
            small_num = user_input

print("The amount of numbers is",amount)
print("The sum of the numbers is",sum_nums)
print("The amount of even numbers is",even_nums,"and the amount of odd numbers is",odd_nums)
print("The largest number is",large_num, "and the smallest number is",small_num)
print("The average of all the numbers is",sum_nums/amount)