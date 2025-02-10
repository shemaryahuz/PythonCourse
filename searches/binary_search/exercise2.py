def find_first_positive(arr):
    low = 0
    high = len(arr)
    while low <= high:
        mid = (low + high)//2
        if arr[mid] < 0:
            low = mid + 1
        else:
            if arr[mid - 1] < 0:
                return mid
            else:
                high = mid -1

array = [-5,-4,-3,-2,-1,0,2,4,6]
print(f"The first positive number is at index {find_first_positive(array)}")
