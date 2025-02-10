def last_zero(arr):
    n = len(arr)
    first = 0
    last = n - 1
    while first <= last:
        mid = (first + last)//2
        if arr[mid] == 0 and arr[mid + 1] == 1:
            return mid
        elif arr[mid] == 0:
            first = mid + 1
        else:
            last = mid - 1


binary_array = [0,0,0,0,0,0,1,1,1,1]
print(f"The last zero in the array is at index {last_zero(binary_array)}")