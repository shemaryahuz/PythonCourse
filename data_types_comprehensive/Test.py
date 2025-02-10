# num1 = float(input("Enter a number:"))
# num2 = float(input("Enter a number:"))
# print("the result is:",num1 * num2)

# x = 5
# for i in range(x):
#     s = ""
#     for j in range(x - i):
#         s += str(x - i - j)
# print(s)

# d = {"x":{6 , 6}, "y":(6 , 6)}
# print(len(d["x"]) + d["y"][1])

# a = []
# b = []
# for i in range(4):
#     num = int(input("Enter a number:"))
#     a.append(num)
# for i in range(4):
#     num = int(input("Enter a number:"))
#     b.append(num)
# print(a)
# print(b)
# c = []
# for i in range(4):
#     if i % 2 == 0:
#         c.append(a[i] * b[i + 1])
#     else:
#         c.append(a[i] + b[i - 1])
# print(c)

# list_1 = []
# list_2 = []
# list_3 = []
# for i in range(4):
#     list_1.append(i)
# print(list_1)
# data = {"max":list_1[-1]}
# for i,x in enumerate(list_1):
#     list_2.append(list_1[i % 3] + x)
# list_2 = list_2[::-1]
# print(list_2)
# while len(list_2)>0:
#     x = list_2.pop() + list_2.pop()
#     list_3.append(x)
# print(list_3)
# print(data["max"]in list_3)

# a = [9,8,7,6,5,45,67,3,4,18,25]
# num = int(input("Enter a number:"))
# is_not = True
# for i in a:
#     if i > num:
#         is_not = False
#         print(i)
# if is_not:
#     print("not found")

# a = [4,6,7]
# m = []
# for i in range(len(a)):
#     if i % 2 == 0:
#         m.append(a)
#     else:
#         m.append(a[::-1])
# print(m)
# is_sum = 0
# for i,x in enumerate(m):
#     if i == 0:
#         is_sum += x[0]
#     else:
#         is_sum += x[0] + x[i]
# print(is_sum)

