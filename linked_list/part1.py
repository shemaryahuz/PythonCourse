"""Exercises Part 1"""


"""Exercise 1"""
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
# head = Node(1)
# second = Node(2)
# third = Node(3)
# head.next = second
# second.next = third
# # print(head.next.data)
"""
Output :
2
"""
# print(third.data)
"""
Output :
3
"""


"""Exercise 2"""
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
# node1 = Node(5)
# node2 = Node(10)
# node1 = node2
"""
The Error is at line 33, assignment of node1 for nod2.
node2 is a reference variable for the Node object
"""

"""Exercise 3"""
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
# x = Node(10)
# y = Node(20)
# x.next = y
# y.next = x
# print(x.next.next.data)

"""
Output :
10
"""



"""Exercise 4"""
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
# a = Node(1)
# b = a
# a.data = 2
# print(b.data)
# b.data = 3
# print(a.data)
"""
Output :
2
3
"""


"""Exercise 5"""
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
# head = Node("Hello")
# tail = Node("World")
# head.next = tail
# print(head.data)
# head = head.next
# print(head.data)
"""
Output :
Hello
World
"""


"""Exercise 6"""
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
# first = Node("a")
# second = Node("b")
# third = Node("c")
# first.next = second
# second.next = third
# temp = first
# while temp:
#     print(temp.data, end= "")
#     temp = temp.next

"""
Output :
abc
"""






