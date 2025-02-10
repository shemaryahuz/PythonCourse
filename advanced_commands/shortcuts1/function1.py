# A:
multiply = lambda  x, y: x * y
result = multiply(3, 4)
print(result)
# output: 12

# B:
numbers = [1, 2, 3, 4]
doubled = list(map(lambda x : x * 2, numbers))
print(doubled)
# output: [2, 4, 6, 8]