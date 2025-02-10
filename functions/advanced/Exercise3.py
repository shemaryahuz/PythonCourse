def sum_nums(arr):
    """function that accepts a list of numbers and returns their sum."""
    is_sum = 0
    for num in arr:
        is_sum += num
    return is_sum
help(sum_nums)
is_list = [1,2,3]
print(sum_nums(is_list))

