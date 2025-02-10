"""Stack Exercises Part 3"""

from stack_by_list import StackImplementationList

# exercise 1
# def merge_sort_stacks(stack1, stack2):
#
#     sorted_stack = StackImplementationList()
#     point1 = stack1.peek()
#     point2 = stack2.peek()
#
#
#     while not stack1.stack_is_empty() and not stack2.stack_is_empty():
#         if  point1 >= point2:
#             sorted_stack.push(stack1.pop())
#             point1 = stack1.peek()
#
#         else:
#             sorted_stack.push(stack2.pop())
#             point2 = stack2.peek()
#
#     if stack1.stack_is_empty():
#         while not stack2.stack_is_empty():
#             sorted_stack.push(stack2.pop())
#
#     else:
#         while not stack1.stack_is_empty():
#             sorted_stack.push(stack1.pop())
#
#     return sorted_stack
#
# s1 = StackImplementationList()
# s1.push(2)
# s1.push(5)
# s1.push(7)
# s2 = StackImplementationList()
# s2.push(1)
# s2.push(8)
# s2.push(9)
#
# sorted_s = merge_sort_stacks(s1, s2)
# while not sorted_s.stack_is_empty():
#     print(sorted_s.pop())


# exercise 2

# class CircularStack:
#
#     def __init__(self):
#         self.__list = []
#         self.capacity = 3
#
#     def push(self, value):
#         if len(self.__list) < self.capacity:
#             self.__list.append(value)
#         else:
#             self.__list.pop(0)
#             self.__list.append(value)
#
#     def pop(self):
#         return self.__list.pop(len(self.__list)-1)
#
#     def peek(self):
#         return self.__list[len(self.__list)-1]
#
#     def is_empty(self):
#         return len(self.__list) == 0
#
# s = CircularStack()
#
# for i in range(8, 16):
#     s.push(i)
#
# while not s.is_empty():
#     print(s.pop())


# exercise 3

def delete_duplicates(stack):

    stack2 = StackImplementationList()
    duplicates = []
    while not stack.stack_is_empty():
        continue
