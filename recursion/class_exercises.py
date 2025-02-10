

# def print_n_to_zero(n):
#     for i in range(n, -1, -1):
#         print(i)
#
#
# num = int(input("Enter a natural number: "))
# print_n_to_zero(num)

# def on_back(n):
#     return n - 1
#
# def print_back(n):
#     while n >= 0:
#         print(n)
#         n = on_back(n)
#
# num = int(input("Enter a natural number: "))
# print_back(num)

# def rec_print_back(n):
#     if n == 0:
#         print("no more prints")
#     else:
#         print(n)
#         rec_print_back(n - 1)
#         print(f"we are in function call {n}")
#
# num = int(input("Enter a natural number: "))
# rec_print_back(num)

# def rec_sum_one_to_n(n):
#     print(f"we are in call {n}")
#     if n == 1:
#         return 1
#     else:
#         res = rec_sum_one_to_n(n-1)+n
#         return res
#
# x = 5
# print(rec_sum_one_to_n(x))

# def rec_pow(base,exp):
#     if base == 0:
#         return 0
#     if exp == 0:
#         return 1
#     return rec_pow(base,exp-1) * base
#
# print(rec_pow(1,2))

# def reverse(num):
#     if num < 10:
#         print(num)
#     else:
#         print(num % 10, end = "")
#         reverse(num // 10)
#
# reverse(12345)







