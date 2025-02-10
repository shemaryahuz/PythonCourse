def is_largest_greater_than_length(arr):
    n = len(arr)
    greater = False
    for num in arr:
        if num > n:
            greater = True
    return greater


def check_majority_2d_array(matrix):
    n = len(matrix)
    greats = 0
    for row in matrix:
        if is_largest_greater_than_length(row):
            greats += 1
    most_rows = greats > n // 2
    return most_rows

print(check_majority_2d_array([[5, 1], [10], [3, 2, 1], [1, 1, 1]]))

def find_min_index(arr):
    min_ind = 0
    for i in range(1, len(arr)):
        if arr[i] < arr[min_ind]:
            min_ind = i
    return min_ind


def select_sort(unsorted_arr, sorted_arr=[]):
    if len(unsorted_arr) <= 1:
        return unsorted_arr
    minimum = find_min_index(unsorted_arr)
    cur_min = unsorted_arr.pop(minimum)
    sorted_arr = select_sort(unsorted_arr)
    sorted_arr.insert(0,cur_min)
    return sorted_arr

print(select_sort([5, 2, 6, 1]))
