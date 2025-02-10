def find_first(arr,x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x and mid != 0:
            if arr[mid - 1] != x:
                return mid
            else:
                high = mid - 1
        elif arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def find_last(arr,x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x and mid != len(arr)-1:
            if arr[mid + 1] != x:
                return mid
            else:
                low = mid + 1
        elif arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def times_shows(arr,x):
    first = find_first(arr,x)
    last = find_last(arr,x)
    if first != -1:
        return last - first + 1
    return 0

array = [12,14]
num = 13

print(f"{num} shows {times_shows(array,num)} times in the array")