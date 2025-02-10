def rec_pow(base,exp):
    if base == 0:
        return 0
    if exp == 0:
        return 1
    return rec_pow(base,exp-1) * base

print(rec_pow(1,2))