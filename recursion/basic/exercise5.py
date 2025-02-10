def print_reverse_digits(num):
    if num < 10:
        print(num, end= " ")
    else:
        print(num % 10, end= " ")
        print_reverse_digits(num // 10)

print_reverse_digits(12345)