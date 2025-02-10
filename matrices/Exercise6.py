# Create a square matrix, fill it with random numbers, and print:
# a. The sum of its diagonals.
# b. The sum of the first and last columns.
# c. The sum of the matrix frame.

import random

square_matrix = [ [random.randint(0,9) for j in range(5)] for i in range(5)]

for row in square_matrix:
    print(row)

sum_diagonals = 0
sum_columns = 0
sum_frame = 0

for i,row in enumerate(square_matrix):
    sum_diagonals += row[i] + (row[4 - i])
    sum_columns += row[0] + row[4]
    if i == 0 or i == 4:
        sum_frame += row[0] + row[1] + row[2] + row[3] + row[4]
    else:
        sum_frame += row[0] + row[4]

print("The sum of its diagonals is:",sum_diagonals)
print("The sum of the first and last columns is:", sum_columns)
print("The sum of the matrix frame is:",sum_frame)
