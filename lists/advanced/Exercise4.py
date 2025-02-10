# Create a list of 200 and fill it with consecutive numbers.
# The list should be split into 2 lists:
# A. A list of all even numbers
# B. A list of all odd numbers

numbers = []
num = 200
for i in range(200):
    numbers.append(num + 1)
    num += 1

even_nums = numbers[1::2]
odd_nums = numbers[::2]

print(even_nums)
print(odd_nums)