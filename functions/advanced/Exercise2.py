def zero_to_n(num):
    """function that accepts a positive integer and returns the sum of the numbers from zero to the number it received."""
    is_sum = 0
    for i in range(1, num + 1):
        is_sum += i
    return is_sum

help(zero_to_n)
print(zero_to_n(4))

