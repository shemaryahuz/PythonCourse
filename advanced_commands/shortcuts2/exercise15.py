from functools import reduce

def sum_positives(matrix):
    positives = list(map(lambda row: list(filter(lambda x: x > 0, row)), matrix))
    return reduce(lambda x, y: x + y, reduce(lambda x, y: x + y, positives))

nums_matrix = [[2,-3,4],[1,9,6],[5,3,-7]]

print(f"The sum of all the positive numbers in the matrix is {sum_positives(nums_matrix)}")











