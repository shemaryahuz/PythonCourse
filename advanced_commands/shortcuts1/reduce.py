from functools import reduce

arr = [1,2,3,4,5]
result = reduce(lambda x,y: x * y, arr)
print(result)





