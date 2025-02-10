arr1 = [5,4,3]
arr2 = [1,10,-5]
arr3 = [10, 30, 15, 2]
arr4 = [200, 20]
all_arr = [arr1,arr2,arr3,arr4]
# len_4 = len(all_arr) == 4
# print(len_4)
# num = int(input("Please enter a number:"))
numbers = [3,44,10,5,6]


index_num = 0
for num in numbers:
    num_in_all = False
    for i,arr in enumerate(all_arr):
        # print(num,arr)
        if num in arr:
            num_in_all = True
            j = arr.index(num)
            index_num = i,j
            print(num, "is in the array at index", index_num)
    if not num_in_all:
            print(num, "is not in the array")







