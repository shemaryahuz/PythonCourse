#Print all elements in the first half of a given list
#The complexity is linear; O(n), because it depend on n
is_list = [1,2,3,4,4,5,7,7,8,4]

for element in is_list[:len(is_list)//2]:
    print(element)