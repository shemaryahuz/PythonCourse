# Create a 4x4 matrix with any numbers.
# Then:
# A. Print the size of the matrix and the size of the first row.
# B. Print a matrix with the order reversed. Order the columns from last to first and the values in each row from last to first.
# C. Print another matrix containing only the elements in the even place in each row.
# D. Print the sum of all the elements and their average.
# E. Print the number that appears most often in the matrix.


four_matrix = [[43,2,17,4],[54,2,11,17],[9,85,11,2],[19,17,11,17]]
print("The matrix of four by four is",four_matrix)

# print("The size of the matrix is", len(four_matrix))
# print("The size of the first row is", len(four_matrix[0]))

# reverse_matrix = []
# for i in range(4):
#     row = four_matrix[i][::-1]
#     reverse_matrix.append(row)
# reverse_matrix = reverse_matrix[::-1]
# print("The reversed matrix is",reverse_matrix)

# even_matrix = []
# for i in range(4):
#     row = four_matrix[i][1::2]
#     even_matrix.append(row)
# print("The matrix of the even indexes",even_matrix)

# sum_elements = 0
# amount_elements = 0

# for i in range(4):
#     for j in range(4):
#         sum_elements += four_matrix[i][j]
#         amount_elements += 1
# print(f"The sum of all the elements in the matrix is {sum_elements} and the average is {sum_elements/amount_elements}")

matrix_list = []

for arr in four_matrix:
    matrix_list += arr

print("The matrix list is:",matrix_list)

counter_max = 0
counter = 0
common_num = 0
for num in matrix_list:
            counter = matrix_list.count(num)
            if counter > counter_max:
                counter_max = counter
                common_num = num
print("The common number is",common_num)





