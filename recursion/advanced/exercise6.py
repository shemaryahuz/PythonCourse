


def rec_bubble_sort(arr):
    if len(arr) <= 1:
        return arr
    max_ind = 0
    for i in range(1,len(arr)):
        if arr[i] < arr[max_ind]:
            arr[i],arr[max_ind] = arr[max_ind],arr[i]
        max_ind = i
    is_max = arr.pop()
    rec_bubble_sort(arr)
    arr.append(is_max)
    return arr

array = [6,1,3,9,4]
print(rec_bubble_sort(array))