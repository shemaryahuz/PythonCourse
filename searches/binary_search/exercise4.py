def find_nearest(arr,x):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low + high)//2
        if arr[mid] == x:
            return x
        elif arr[mid] < x and mid == len(arr) - 1:
            return arr[mid]
        elif arr[mid] > x and mid == 0:
            return arr[mid]
        elif arr[mid] < x:
            if arr[mid + 1] > x:
                left = x - arr[mid]
                right = arr[mid + 1] - x
                if left <= right :
                    return arr[mid]
                else:
                    return arr[mid + 1]
            else:
                low = mid + 1
        else:
            if arr[mid - 1] < x:
                left = x - arr[mid - 1]
                right = arr[mid] - x
                if  left > right:
                    return arr[mid]
                else:
                    return arr[mid - 1]
            else:
                high = mid - 1


array = [2,5,9,13,17,20]
num = 18
print(find_nearest(array,num))