from functools import reduce
def maximum(arr):
    return reduce(lambda x, y: x if x > y else y, arr)

a = [7,5,4,7,8,3,2,5]
print(maximum(a))


