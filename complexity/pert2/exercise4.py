def sum_evens(arr):
    is_sum = 0
    for num in arr:
        if num % 2 == 0:
            is_sum += num
    return is_sum

is_arr = [9,8,7,9,6,5,7,4,9,3,2,5,7,5,3]
print(f"The sum of the even numbers is {sum_evens(is_arr)}.")