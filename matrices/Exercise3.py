#Print, using a for loop, a 10 by 10 matrix of consecutive numbers from 1 to 100.


#
# for i in range(10):
#     for j in range(1,11):
#         print(i * 10 + j , end = " ")
#     print("")

hundred = []
for i in range(10):
    ten = []
    for j in range(1,11):
         ten.append(i * 10 + j)
    hundred.append(ten)

for ten in hundred:
    print(ten)


