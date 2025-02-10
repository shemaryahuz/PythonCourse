def rec_sum_digits(num):
    if num < 10:
        return num
    return rec_sum_digits(num // 10) + num % 10

print(rec_sum_digits(451))

