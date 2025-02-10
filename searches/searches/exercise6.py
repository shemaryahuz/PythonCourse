def small_and_large(arr):
    if len(arr) > 0:
        return arr[0], arr[-1]

array = [2,4,6,8,10]
print(type(small_and_large(array)))
print(f"The small and large numbers in the array are {small_and_large(array)}")