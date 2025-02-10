
def find_doubles(arr):
    n = len(arr)
    doubles_list = []
    for i in range(n):
        for j in range(i + 1, n):
            if arr[j] == arr[i]:
                doubles_list.append(arr[i])
                break
    return  doubles_list

array = [3,4,5,1,6,9,4,6]
print(f"The double numbers in the list are {find_doubles(array)}")

