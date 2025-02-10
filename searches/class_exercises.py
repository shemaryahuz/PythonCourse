from datetime import datetime

def linear_search(arr,element):
    for i, num in enumerate(arr):
        if num == element:
            return i
    return -1

def binary_search(arr,element):
    first = 0
    last = len(arr)-1
    while first <= last:
        mid = (first + last)//2
        if arr[mid] == element:
            return mid
        elif arr[mid] > element:
            last = mid-1
        else:
            first = mid+1
    return -1

len_list = int(input("Choose the list's length: "))
nums_list = [i * (i+1) for i in range(len_list)]
print(f"The list is {nums_list}")
number = int(input("Choose number for searching: "))

print("linear search:")
time_start = datetime.now()
if linear_search(nums_list,number) != -1:
     print(f"{number} is in index {linear_search(nums_list,number)}")
else:
    print("Not found")
time_end = datetime.now()
print(f"Running time is {time_end-time_start}")
print("")
time_start = datetime.now()
print("binary_search:")
if binary_search(nums_list,number) != -1:
     print(f"{number} is in index {binary_search(nums_list,number)}")
else:
    print("Not found")
time_end = datetime.now()
print(f"Running time is {time_end-time_start}")