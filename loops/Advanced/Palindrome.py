# Ask the user for a number and print whether it is a palindrome.

num = int(input("Please enter a number:"))
copy_num = num
revers_num = 0
while num > 0:
    units = num % 10
    num = num // 10
    revers_num += units
    revers_num *= 10
revers_num /= 10
if revers_num == copy_num:
    print(copy_num,"is a palindrome")
else:
    print(copy_num,"is not a palindrome")