# The complexity is linear; O(n), because it depend on the array's length

# def print_elements(arr):
#     """Print all elements in the first half of a given list, then in another loop all elements in the second half."""
#     print("first loop:")
#     for i in range(len(arr)//2):
#         print(arr[i])
#     print("second loop:")
#     for i in range(len(arr)//2, len(arr)):
#         print(arr[i])
#
# is_arr = [3,4,5,6,76,8,9,6,1,45,6,8,97,57,3]
# print_elements(is_arr)

#add actions counter
def print_elements(arr):
    """Print all elements in the first half of a given list, then in another loop all elements in the second half."""
    counter = 0
    print("first loop:")
    counter += 1
    for i in range(len(arr)//2):
        print(arr[i])
        counter += 2
    print("second loop:")
    counter += 1
    for i in range(len(arr)//2, len(arr)):
        print(arr[i])
        counter += 2
    print(f"The amount of actions is {counter}")
is_arr = [3,4,5,6,76,8,9,6,1,45,6,8,97,57,3]
print_elements(is_arr)