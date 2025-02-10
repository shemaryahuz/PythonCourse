
def long_subarray(is_list,n):
    """Return the longest subarray in a list where the sum of the elements is positive"""
    for i in range(1, n):
        for j in range(i):
            sub_arr = is_list[j:n - i + 1 + j]
            if sum(sub_arr) > 0:
                return sub_arr
    return []

check_list = [2,3,-40,-150,5,-8,8,-20,4,100]
length = len(check_list)
print(long_subarray(check_list, length))

