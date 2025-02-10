def find_repeated_num(arr):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low + high)//2
        if arr[mid] == mid and arr[mid - 1] == mid:
            return mid
        elif arr[mid] > mid:
            low = mid + 1
        else:
            high = mid - 1

array = [1, 2, 3, 4, 5]

print(find_repeated_num(array))