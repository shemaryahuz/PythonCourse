#print multiplication table for 1 to 10
#The program hase a constant complexity; O(1), because the quantity of the program's calculations is always 10^2

is_array = []
for i in range(1,11):
    is_row = []
    for j in range(1,11):
        is_row.append(i * j)
    is_array.append(is_row)

for row in is_array:
    print(row)


