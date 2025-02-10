

def binary_search(arr,x):
    low_ind = 0
    high_ind = len(arr)-1
    while low_ind <= high_ind:
        mid_ind = (low_ind + high_ind)//2
        if arr[mid_ind] == x:
            return mid_ind
        elif arr[mid_ind] < x:
            low_ind = mid_ind +1
        else:
            high_ind = mid_ind -1
    return -1

array = [2,5,8,13,16,21,29,35]
num = 14
if binary_search(array,num) == -1:
    print(f"{num} is not in the array")
else:
    print(f"{num} is in the array at index {binary_search(array,num)}")