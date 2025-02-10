# Get a list of numbers from the user and a number to test.
# Print whether the number is in the list or not.

is_list = list(input("Enter a list of numbers: "))
number = input("Enter a number for searching: ")
if number in is_list:
    print(f"{number} is in the list")
else:
    print(f"{number} is not in the list")