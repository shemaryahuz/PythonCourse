


# is_list = ["a", "b", "c"]
# def f(l):
#     try:
#         return l[4]
#
#     except IndexError:
#         pass
#
#     finally:
#         print("done")
#
# print(f(is_list))
# print("end")


# for i in range(5, -5, -1):
#
#     try:
#         print(3/i)
#
#     except ZeroDivisionError:
#         print("x --> inf")

# import sys
#
# try:
#     f = open("MyFile.txt")
#     s = f.readline()
#     i = int(s.strip())
# except OSError as err:
#     print(f"OS error: {err}")
# except ValueError:
#     print("Could not convert data to an integer.")
# except:
#     print("Unexpected error:", sys.exc_info()[0])
#     raise

# try:
#     a = int(input("Enter a positive integer: "))
#     if a <= 0:
#         raise ValueError(f"{a} is not a positive number!")
# except ValueError as val_err:
#     print(val_err)

# x = int(input("enter a number "))
# y = int(input("enter a divider "))
#
# assert y != 0, "con not divide by zero"
# print(x / y)


# # three ways to double items
# items = [2,7,3]
# # long way
# def double(arg):
#     return arg*2
# double_items = []
# for item in items:
#     double_items.append(double(item))
# print(double_items)
# # short way
# double = lambda arg: arg * 2
# print(list(map(double, items)))
# # the shorts way
# print(list(map(lambda arg: arg * 2, items)))






# def desc(colour):
#     return lambda obj : print("The " + obj + " is " + colour)
# green = desc("green")
# green("table")
# blue = desc("blue")
# blue("chair")

# items = [2,7,3]
# y = map(lambda x: x**2, items)
# print(list(y))





# a = [i for i in range(10)]
# print(a)


# matrix = [[i * j for j in range(1, 11)] for i in range(1, 11)]
# [print(row) for row in matrix]

# dollar = {"backpack": 100, "case": 200, "bag": 20}
# shekel = {product:price*3.7 for product, price in dollar.items()}
#
# print(shekel)

# a, b = 0, 1
# def fibonacci_function():
#     global a, b
#     current = a
#     a, b = b, a + b
#     return current
# for _ in range(30):
#     print(fibonacci_function(), end= " ")

# a, b = 0, 1
# def fibonacci_function():
#     global a, b
#     current = a
#     a, b = b, a + b
#     return current
# for _ in range(10):
#     print(fibonacci_function(), end= " ")


# def fibonacci_generator():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b
#
# fib = fibonacci_generator()
# for _ in range(10):
#     print(next(fib), end= " ")