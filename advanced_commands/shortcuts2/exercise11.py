from functools import reduce

def calc_digits(num):
    digits = [int(s) for s in str(num)]
    return reduce(lambda x, y: x + y, digits)

print(calc_digits(1234))




