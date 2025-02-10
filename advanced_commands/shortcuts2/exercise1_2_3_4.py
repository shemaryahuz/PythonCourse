"""Code Understanding"""

"""exercise 1"""

# numbers = [1, -2, 3, -4, 5]
# positive = list(filter(lambda x: x > 0, numbers))
# result = list(map(lambda  x: x * 2, positive))
# print(result)

# output: [2, 6, 10]

"""exercise 2"""

# words = ["apple", "banana", "cherry"]
# lengths = list(map(lambda x:len(x),words))
# filtered = list(filter(lambda x: x > 5, lengths))
# print(filtered)

# output: [6, 6]

"""exercise 3"""

# data = [("John", 25), ("Anna", 22), ("Mike", 28)]
# result = sorted(data, key= lambda x: x[1])
# print(result)

# the code's purpose is to get a list of the people sorted by the ages
# output: [("Anna", 22), ("John", 25), ("Mike", 28)]

"""exercise 4"""

# matrix = [[1, 2], [3, 4], [5, 6]]
# flattened = [item for sublist in matrix for item in sublist]
# squared = list(map(lambda x: x ** 2, flattened))
# print(squared)

# output: [1, 4, 9, 16, 25, 36]

