def print_couples(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1 , n):
                print (arr[i], arr[j])


array = ["apple","banana","tomato"]
print_couples(array)