# Get a list of numbers and two numbers to test.
# Print whether the two numbers appear one after the other in the list

nums_list = list(input("Enter a list of numbers: "))
num1 = input("Enter number 1: ")
num2 = input("Enter number 2: ")

n = len(nums_list)
in_list = False
for i in range(n-1):
   if nums_list[i:i+2] == [num1,num2]:
        print(f"The numbers are in sequence in the list at indexes [{i},{i+1}]")
        in_list = True
        break
if not in_list:
    print("The numbers are not in sequence in the list")