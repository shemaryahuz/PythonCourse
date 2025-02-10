from functools import reduce

def multiply_positives(arr):
    return reduce(lambda x, y: x * y, [x for x in arr if x > 0])

array = [-9, -2, -5, 2, -1, 2]
print(multiply_positives(array))



