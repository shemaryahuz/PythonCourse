# Ask the user for numbers repeatedly until they enter 0 and create a list of the numbers.
# Remove the last item in the list and store it in a variable, then insert it from the variable to the beginning of the list.


num = 1
numbers = []
while num != 0:
    num = int(input("Please enter a number:"))
    numbers.append(num)
numbers.pop()
print(numbers)
last_num = numbers.pop()
numbers.insert(0,last_num)
print(numbers)

