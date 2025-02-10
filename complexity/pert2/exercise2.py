#Print all the elements in the list twice, one after the other
#The complexity is linear; O(n), because it depend on the list's length
str_list = [1,5,4,3,6,7,8,4,9]
for i in str_list:
    print((str(i)+" ") * 2)