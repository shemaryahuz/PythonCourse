#The program hase a linear complexity; O(n), because the quantity of the program's calculations depend on n

def sum_nums(n):
    """Get numbers from the user, add them to a list and sum the list's elements"""
    nums_list = []
    for i in range(n):
        num = float(input("Enter a number: "))
        nums_list.append(num)
    return sum(nums_list)
number = int(input("Enter a natural number: "))
print("The sum is", sum_nums(number))
