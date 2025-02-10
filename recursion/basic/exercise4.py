def print_digits(num):
    if num < 10:
        print(num, end= " ")
    else:
        print_digits(num // 10)
        print(num % 10, end= " ")
print_digits(12345)