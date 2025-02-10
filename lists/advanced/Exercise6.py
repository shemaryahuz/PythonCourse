# Ask the user for 10 integers and fill a list with the numbers they selected.
# Print the largest number in the list.

numbers = []

for i in range(10):
    num = int(input("Please enter a number:"))
    numbers.append(num)
print(numbers)

largest_num = 0

for i in range(len(numbers)):
    if numbers[i] > largest_num:
        largest_num = numbers[i]
print("The largest number is",largest_num)