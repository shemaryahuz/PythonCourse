# Return the smallest number in a given array
# The complexity is linear; O(n), because it depend on the array's length

# def min_num(arr):
#     is_min = arr[0]
#     for i in arr:
#         if i < is_min:
#             is_min = i
#     return is_min
#
# is_arr = [9,8,7,9,6,5,7,4,9,3,2,5,7,5,3]
#
# print(f"The minimum number in the array is {min_num(is_arr)}.")

#add actions counter
def min_num(arr):
    global counter
    is_min = arr[0]
    counter += 1
    for i in arr:
        if i < is_min:
            is_min = i
            counter += 1
        counter += 1
    return is_min


is_arr = [9,8,7,9,6,5,7,4,9,3,2,5,7,5,3]

counter = 0
print(f"The minimum number in the array is {min_num(is_arr)}.")
print(f"The amount of actions is {counter}")

