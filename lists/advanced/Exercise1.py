# Get five integers from the user. Create a new list and insert the numbers into it.
# Replace the third element with the second element. And the element at index 3 with the fifth element.
# Print the new list.

user_list = []

for i in range(5):
    num = int(input("Please enter an integer number:"))
    user_list.append(num)
print(user_list)

user_list[1],user_list[2] = user_list[2],user_list[1]
user_list[3],user_list[4] = user_list[4],user_list[3]

print(user_list)
