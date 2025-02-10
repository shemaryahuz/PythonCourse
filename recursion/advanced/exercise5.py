
def rec_selection_sort(arr):
    if len(arr) <= 1:
        return arr
    num = arr[0]
    is_max = True
    sorted_arr = rec_selection_sort(arr[1:])
    for i in range(len(sorted_arr)):
        if num < sorted_arr[i]:
            is_max = False
            sorted_arr.insert(i,num)
            break
    if is_max:
        sorted_arr.append(num)
    return sorted_arr

array = [23,4,18]
print(rec_selection_sort(array))