"""Question 1"""


# def sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     return arr
#
# if __name__ == "__main__":
#     array = [64, 25, 12, 22, 11]
#     print("Unsorted array:", array)
#     sorted_array = sort(array)
#     print("Sorted array:", sorted_array)
# """
# explanation:
# iteration i = 0:
#     iteration j = 0:
#         arr[0] = 25
#         arr[1] = 64
#
#     iteration j = 1:
#         arr[1] = 12
#         arr[2] = 64
#
#     iteration j = 2:
#         arr[2] = 22
#         arr[3] = 64
#
#     iteration j = 3:
#         arr[3] = 11
#         arr[4] = 64
#
# iteration i = 1:
#
#     iteration j = 0:
#         arr[0] = 12
#         arr[1] = 25
#
#     iteration j = 1:
#         arr[1] = 22
#         arr[2] = 25
#
#     iteration j = 2:
#         arr[2] = 11
#         arr[3] = 25
#
#     iteration j = 3:
#
#
# iteration i = 2:
#
#     iteration j = 0:
#
#     iteration j = 1:
#         arr[1] = 11
#         arr[2] = 22
#
#     iteration j = 2:
#
#
# iteration i = 3:
#
#     iteration j = 0:
#         arr[0] = 11
#         arr[1] = 12
#
#     iteration j = 1:
#
# iteration i = 4:
#     iteration j = 0:
#
# output:
# Unsorted array: [64, 25, 12, 22, 11]
# Sorted array: [11, 12, 22, 25, 64]
# """


"""Question 2"""
# """
# The bubble sort improvement does not change the runtime complexity of the code by orders of magnitude,
# because it improves cases where the array is partially sorted,
# and complexity by orders of magnitude is measured by the worst case.
# """


"""Question 3"""
# def sort_and_search(arr,x):
#     n = len(arr)
#     for i in range(n):
#         is_sorted = True
#         for j in range(n - i - 1):
#             if arr[j] < arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#                 is_sorted = False
#         if is_sorted:
#             break
#     print(f"Sorted array: {arr}")
#     high = 0
#     low = n - 1
#     while high <= low:
#         mid = (high + low)//2
#         if arr[mid] == x:
#             return True
#         elif arr[mid] > x:
#             high = mid + 1
#         else:
#             low = mid - 1
#     return False
# array = [2,4,55,44,33,22,11]
# num = 5
# is_in = sort_and_search(array,num)
# if is_in:
#     print(f"{num} is in the array")
# else:
#     print(f"{num} is not in the array")
#
# """
# The runtime complexity of the code is o(n**2), because the sorting step requires (n*n)//2 iterations, even though the search step is o(log n).
# The function is inefficient because it requires going through the entire array to sort it, and if so, binary search does not save runtime.
# """


"""Question 4"""
def sort_arrays_a(a,b):
    new_arr = a + b
    for i in range(len(new_arr)):
        is_sorted = True
        for j in range(len(new_arr) - 1 - i):
            if new_arr[j] > new_arr[j + 1]:
                new_arr[j], new_arr[j + 1] = new_arr[j + 1], new_arr[j]
                is_sorted = False
        if is_sorted:
            break
    return new_arr

def sort_arrays_b(a,b):
    n = len(a)
    m = len(b)
    ind_a = 0
    ind_b = 0
    new_arr = []
    for i in range(n + m):
        if ind_a == n:
            new_arr += b[ind_b:]
            ind_b += 1
        elif ind_b == m:
            new_arr += a[ind_a:]
            ind_a += 1
        else:
            if a[ind_a] < b[ind_b]:
                new_arr.append(a[ind_a])
                ind_a += 1
            else:
                new_arr.append(b[ind_b])
                ind_b += 1
    return new_arr

arr1 = [1,3,5,7,9]
arr2 = [2,4,6,8,10]
print("buble_sort...")
print(sort_arrays_a(arr1,arr2))
print("merge sort...")
print(sort_arrays_b(arr1,arr2))




"""Question 5"""

# def sorted_str(matrix):
#     str_arr = []
#     for row in matrix:
#         for char in row:
#             str_arr.append(char)
#     n = len(str_arr)
#     for i in range(n - 1):
#         is_sorted = True
#         for j in range(n - i - 1):
#             if str_arr[j] > str_arr[j + 1]:
#                 is_sorted = False
#                 str_arr[j], str_arr[j + 1] = str_arr[j + 1], str_arr[j]
#         if is_sorted:
#             break
#     str = "".join(str_arr)
#     return str
#
# is_matrix = [["b","f","a"],["c","e","g"],["d","h","i"]]
# print(sorted_str(is_matrix))






