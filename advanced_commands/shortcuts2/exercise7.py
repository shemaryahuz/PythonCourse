

def order_by_len(arr):

    ordered = {}
    for str in arr:
        ordered[len(str)] = [s for s in arr if len(s) == len(str)]
    return ordered

array = ["a", "ab", "aba", "b", "bc", "bcb"]
print(order_by_len(array))





