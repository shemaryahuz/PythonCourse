"""Exercises part 1"""

from stack_by_list import StackImplementationList

"""exercise 1"""

# stack = StackImplementationLinkedList()
#
# stack.push(5)
# stack.push(3)
# x = stack.pop()
# stack.push(8)
# y = stack.pop()
# print(x, y) # 3 8
# print(stack.peek()) # 5
# # The stack hse only the value 5

"""exercise 2"""

# s = StackImplementationList()
# s.push("A")
# s.push("B")
# s.push("C")
# while not s.is_empty():
#     print(s.pop())
# output:
# C
# B
# A

"""exercise3"""

# def print_stack_elements(stack):
#
#     new_stack = StackImplementationList()
#     while not stack.is_empty():
#         removed = stack.pop()
#         new_stack.push(removed)
#         print(removed)
#     while not new_stack.is_empty():
#         stack.push(new_stack.pop())
#
# s = StackImplementationList()
#
# s.push("A")
# s.push("B")
# s.push("C")
#
# print_stack_elements(s)
# while not s.is_empty():
#     print(s.pop())
#
# print(s.peek())


"""exercise4"""

# def sum_stack_elements(stack):
#
#     is_sum = 0
#     new_stack = StackImplementationList()
#
#     while not stack.stack_is_empty():
#         removed = stack.pop()
#         is_sum += removed
#         new_stack.push(removed)
#
#     while not new_stack.stack_is_empty():
#         stack.push(new_stack.pop())
#
#     return is_sum
#
# s = StackImplementationList()
# s.push(2)
# s.push(3)
# s.push(5)
# print(sum_stack_elements(s))
#
# while not s.stack_is_empty():
#     print(s.pop())

"""exercise5"""

# def max_element(stack):
#
#     is_max = stack.peek()
#     new_stack = StackImplementationList()
#
#     while not stack.stack_is_empty:
#         removed = stack.pop()
#         if removed > is_max:
#             is_max = removed
#         new_stack.push(removed)
#
#     while not new_stack.stack_is_empty():
#         stack.push(new_stack.pop())
#
#     return is_max
#
# s = StackImplementationList()
# s.push(2)
# s.push(3)
# s.push(5)
# print(max_element(s))
#
# while not s.stack_is_empty():
#     print(s.pop())

"""exercise6"""

# def even_len(stack):
#
#     counter = 0
#     new_stack = StackImplementationList()
#
#     while not StackImplementationList.stack_is_empty(stack):
#         removed = stack.pop()
#         counter += 1
#         new_stack.push(removed)
#
#     while not new_stack.stack_is_empty():
#         stack.push(new_stack.pop())
#
#     return counter % 2 == 0
#
# s = StackImplementationList()
# s.push(2)
# s.push(3)
# s.push(4)
# s.push(5)
#
# print(even_len(s))
#
# while not s.stack_is_empty():
#     print(s.pop())

"""exercise7"""

# def count_num(stack, num):
#
#     counter = 0
#     new_stack = StackImplementationList()
#
#     while not stack.stack_is_empty():
#         removed = stack.pop()
#         if removed == num:
#             counter += 1
#         new_stack.push(removed)
#
#     while not new_stack.stack_is_empty():
#         stack.push(new_stack.pop())
#
#     return counter
#
# s = StackImplementationList()
# s.push(2)
# s.push(1)
# s.push(3)
# s.push(4)
#
# print(count_num(s, 5))
#
# while not s.stack_is_empty():
#     print(s.pop())




