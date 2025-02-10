# Ask the user for a number and create a square matrix based on the number the user entered.
# Then fill the elements in the matrix with numbers from 1 onwards until the matrix ends.


matrix_size = int(input("Enter a natural number:"))
matrix_squ = []
for i in range(matrix_size):
    line = []
    for j in range(1, matrix_size + 1):
        line.append(i * matrix_size + j)
    matrix_squ.append(line)

for line in matrix_squ:
    print(line)