def binary_search(arr,x):
    n = len(arr)
    low = 0
    high = n - 1
    for i in range(n):
        mid = (low + high)//2
        if arr[mid] == x and mid == 0 :
            return mid
        if arr[mid] == x and arr[mid - 1] != x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

array = [5, 5, 5]
num = 5
if binary_search(array,num) == -1:
    print(f"{num} is not in the array")
else:
    print(f"{num} is in the array at index {binary_search(array,num)}")