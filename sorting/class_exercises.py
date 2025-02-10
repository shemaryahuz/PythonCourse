
# def selection_sort(arr):
#     n = len(arr)
#     for i in range(n-1):
#         index_min = i
#         for j in range(i+1,n) :
#             if arr[j] < arr[index_min]:
#                 index_min = j
#         arr[i],arr[index_min] = arr[index_min], arr[i]
#     return arr
#
# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         is_sorted = True
#         for j in range(n - 1 - i):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#                 is_sorted = False
#         if is_sorted:
#             break
#     return arr
#
# is_list = [88,55,2,34,13,9,44]
# print("Selection sort...")
# print(selection_sort(is_list))
# print("Bubble sort...")
# print(bubble_sort(is_list))

def merge_sort(a,b):
    new_arr = []
    n = len(a)
    m = len(b)
    ind_a = 0
    ind_b = 0
    while ind_a < n and ind_b < m:
        if a[ind_a] <= b[ind_b]:
            new_arr.append(a[ind_a])
            ind_a += 1
        else:
            new_arr.append(b[ind_b])
            ind_b += 1

    if ind_a == n:
        new_arr += b[ind_b:]
    else:
        new_arr += a[ind_a:]
    return new_arr

arr1 = [2,4,7,11]
arr2 = [1,3,9,13]
print("Merge sort...")
print(merge_sort(arr1,arr2))

















