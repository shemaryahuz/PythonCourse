def sum_parameters(*arr):
    """function that accepts any number of numbers as parameters
    and returns their sum."""
    is_sum = 0
    for num in arr:
        is_sum += num
    return is_sum
help(sum_parameters)

print(sum_parameters(9,5,7,6,4,3,2,5,9))