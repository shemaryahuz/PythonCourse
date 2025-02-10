def rec_multiply(a,b):
    if b == 0:
        return 0
    return rec_multiply(a, b - 1) + a

print(rec_multiply(5,4))