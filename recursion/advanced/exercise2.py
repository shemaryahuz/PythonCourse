def rec_sum(arr):
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[0]
    return rec_sum(arr[:-1]) + arr[-1]

array = [1,4,-2,10]
print(rec_sum(array))




