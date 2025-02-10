def find_num_l(matrix,x):
    in_matrix = False
    for row in matrix:
        if x in row:
            in_matrix = True
            print(f"{x} is in the matrix at row {matrix.index(row)} column {row.index(x)}")
            break
    if not in_matrix:
        print(f"{x} is not in the matrix")

def find_num_b(matrix,x):
    n = len(matrix)
    is_not = True
    low_ind = 0
    high_ind = n - 1
    for i in range(n):
        mid_ind = (low_ind + high_ind) // 2
        if matrix[mid_ind][i] == x:
            print(f"{x} is in the matrix at row {mid_ind} column {i}")
            is_not = False
            break
        elif matrix[mid_ind][i] < x:
            low_ind = mid_ind + 1
        else:
            high_ind = mid_ind - 1
    if is_not:
        print(f"{x} is not in the matrix")



is_matrix = [[1,5,9,13],[2,6,10,14],[3,7,11,15],[4,8,12,16]]
for row in is_matrix:
    print(row)
num = 2
print("linear search...")
find_num_l(is_matrix,num)
print("binary search...")
find_num_b(is_matrix,num)



















# first_row = 0
# last_row = len(matrix) - 1
# first_element = 0
# last_element = len(matrix) - 1
# while first_row <= last_row:
#     mid_row = (first_row + last_row) // 2
#     while first_element <= last_element:
#         mid_element = (first_element + last_element) // 2
#         if matrix[mid_row][mid_element] == x:
#             print(f"{x} is in the matrix at row {mid_row} column {mid_element}")
#             break
#         elif matrix[mid_row][mid_element] < x:
#             first_element = mid_element + 1
#         else:
#             last_element = mid_element - 1
#     if matrix[mid_row][mid_element] < x:
#         first_row = mid_row + 1
#     elif matrix[mid_row][mid_element] > x:
#         last_row = mid_row - 1
# print(f"{x} is not in the matrix")

