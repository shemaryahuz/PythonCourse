#print elements of array
#The program hase a linear complexity; O(n), because the quantity of the program's commands is 2 * len(array)
def print_elements(array):
    for element in array:
        print(element)

is_list = ["apple","banana","tomato"]
print_elements(is_list)