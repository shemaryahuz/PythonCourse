# Create a 5x5 square matrix and fill it with random numbers.
# Then do the following:
# A. Print the row number where the sum of the elements is the largest
# B. Print the row number where the sum of the elements is the smallest
# C. Rotate the matrix 90 degrees to the right and recalculate parts A and B.

import random

square_matrix = [ [random.randint(0,9) for j in range(5)] for i in range(5)]

for row in square_matrix:
    print(row)


# sum_max = 0
# sum_min = 45
# row_max = 0
# row_min = 0
# for i,row in enumerate(square_matrix):
#     sum_row = 0
#     for j in row:
#         sum_row += j
#     if sum_row > sum_max:
#         sum_max = sum_row
#         row_max = i + 1
#     elif sum_row < sum_min:
#         sum_min = sum_row
#         row_min = i + 1
#     print(sum_row)
#
# print("The row number where the sum of the elements is the largest is:",row_max)
# print("The row number where the sum of the elements is the smallest is:",row_min)

rotated_matrix = [ [] for i in range(5)]
rotated_copy = rotated_matrix.copy()
print(rotated_matrix)

for i,row in enumerate(rotated_copy):
    for j,row2 in enumerate(square_matrix):
         print(row)
         print(row2)
         print(i)
         print(j)
         rotated_matrix[i].insert(0 , row2[i])
         x = rotated_matrix[i]
         print(x)
for row in rotated_matrix:
    print(row)



