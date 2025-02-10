# Ask the user for a number.
# Print the shape of an arrow, in which the longest row (ie the tip),
# consists of the number of stars entered by the user.

num = int(input("Please enter a number:"))
for i in range(1,num + 1):
    print("*" * i)
for i in range(1,num):
    print("*" * (num - i))
