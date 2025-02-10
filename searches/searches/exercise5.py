

def binary_search(arr,x):
    n = len(arr)
    is_in = False
    low = 0
    high = n - 1
    for i in range(n):
        mid = (low + high)//2
        if arr[mid] == x:
            is_in = True
            break
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return is_in

array = [1, 3, 5, 7, 9]
num = 1
print(binary_search(array,num))