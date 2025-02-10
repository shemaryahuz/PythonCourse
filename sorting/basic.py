"""Question 1"""

# def sort(arr):
#     for i in range(len(arr)):
#         min_idx = i
#         for j in range(i + 1, len(arr)):
#             if arr[j] < arr[min_idx]:
#                 min_idx = j
#         arr[i], arr[min_idx] = arr[min_idx], arr[i]
#     return arr
#
# if __name__ == "__main__":
#     array = [64, 25, 12, 22, 11]
#     print("Unsorted array:", array)
#     sorted_array = sort(array)
#     print("Sorted array:", sorted_array)
#
# """
# output:
# Unsorted array: [64, 25, 12, 22, 11]
# Sorted array: [11, 12, 22, 25, 64]
# """


"""Question 2"""
def revers_sort(arr):
    n = len(arr)
    for i in range(n-1):
        max_inx = i
        for j in range(i+1,n):
            if arr[j] > arr[max_inx]:
                max_inx = j
        arr[i],arr[max_inx] = arr[max_inx],arr[i]

def revers_sort_b(arr):
    n = len(arr)
    is_sorted = True
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if arr[j] < arr[j+1]:
                is_sorted = False
                arr[j], arr[j+1] = arr[j+1], arr[j]
        if is_sorted:
            break

array = [33,24,13,12,10,25]
revers_sort(array)
print(array)

array0 = [33,24,45,12,10,25]
revers_sort_b(array0)
print(array0)


"""Question 3"""
# def sort_str(str):
#     new_str = str.lower()
#     arr = list(new_str)
#     n = len(new_str)
#     for i in range(n - 1):
#         first_ind = i
#         for j in range(i+1, n):
#             if arr[j] < arr[first_ind]:
#                 first_ind = j
#         arr[i], arr[first_ind] = arr[first_ind], arr[i]
#     new_str = "".join(arr)
#     return new_str
#
# print(sort_str("fedcbaFEDCBDA"))




