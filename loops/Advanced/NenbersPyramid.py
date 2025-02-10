# Ask the user for a number and print him a pyramid consisting of the numbers from 1 to the number he chose.

num = int(input("Please enter a number:"))
for i in range(1,num + 1):
    print(" " * (num - i) ,(str(i) + " ") * i)
