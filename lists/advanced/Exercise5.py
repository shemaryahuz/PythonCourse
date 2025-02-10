# Create a list of random integers.
# Then ask the user for a number, and print whether the number is in the list.
# If so, print the position of the number, the number after it (if any), and
# the number before it (if any).

import random


numbers = []
for i in range(20):
    numbers.append(random.randint(0,1000))
print(numbers)


user_num = int(input("Please enter an integer number:"))
index_num_user = 0
if user_num in numbers:
    print(user_num,"is in the list")
    print("The index of", user_num, "in the list is", numbers.index(user_num))
    index_num_user = numbers.index(user_num)
    if index_num_user == 0:
        print("The number after", user_num, "in the list is", numbers[index_num_user + 1])
    elif index_num_user == 19:
        print("The number before", user_num, "in the list is", numbers[index_num_user - 1])
    else:
        print("The number before", user_num, "in the list is", numbers[index_num_user - 1])
        print("The number after", user_num, "in the list is", numbers[index_num_user + 1])
else:
    print(user_num,"is not in the list")