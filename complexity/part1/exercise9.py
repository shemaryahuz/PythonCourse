#Ask the user for a list of numbers and return the maximum of them
#The complexity is linear; O(n), because it depend on the list's length
stop_condition = int(input("Enter a negative number for stop: "))
num = 0
is_max = 0
while num > stop_condition:
    num = float(input("Enter a positive number: "))
    if num > is_max:
        is_max = num
print("The maximum number of the entered numbers is", is_max)
