
# x = [1, 2, 3, 4]
# y = ['a', 'b', 'c', 'd']
# zipped = zip(x, y)
# print(list(zipped))


# # solution without zip:
# def sort_a_by_b(a, b):
#     zipped = [(b[i], a[i]) for i in range(len(a))]
#     zipped.sort()
#     return [couple[1] for couple in zipped]

# # solution with zip
# def sort_a_by_b(a, b):
#     zipped = list(zip(b, a))
#     zipped.sort()
#     return [couple[1] for couple in zipped]

# array1 = [3, 5, 2, 7, 8]
# array2 = [9, 1, 5, 7, 0]
# sorted_1 = sort_a_by_b(array1, array2)
# print(sorted_1)








