def range_number(arr,x):
    x_ind = 0
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high)//2
        if arr[mid] < x:
            low = mid + 1
        elif arr [mid] > x:
            high = mid - 1
        else:
            while arr[mid] == x:
                mid -= 1
            left = mid
            while arr[mid + 1] == x:
                mid += 1
            right = mid + 1
            return arr[left], arr[right]


array = [1,2,3,4,5,6,8,10,10,10,11]
num = 10
print(range_number(array,num))