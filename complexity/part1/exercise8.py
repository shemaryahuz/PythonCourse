#Print all even numbers from a given list
#The complexity is linear; O(n), because it depend on the list's length
arr = [5,6,7,87,98,34,2,76,4,9]

for num in arr:
    if num % 2 == 0:
        print(num)