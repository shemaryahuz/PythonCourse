# class StackImplementationList:
#
#     def __init__(self):
#         self.__list = []
#
#     def is_empty(self):
#         return len(self.__list) == 0
#
#     def push(self, value):
#         self.__list.append(value)
#
#     def pop(self):
#         return self.__list.pop()
#
#     def peek(self):
#         if not self.is_empty():
#             return self.__list[len(self.__list) - 1]
#
#
# stack = StackImplementationList()
#
#
# stack.push(4)
# stack.push(10)
# stack.push(15)
# print(stack.pop())
# print(stack.pop())
# print(stack.is_empty())
# print(stack.pop())
# print(stack.is_empty())



#
# check if the string has a proper parentheses
# def is_str_proper(str):
#
#     parentheses_stack = StackImplementationArrayList()
#
#     for char in str:
#         if char == "(":
#             parentheses_stack.push(0)
#         elif char == ")":
#             try:
#                 parentheses_stack.pop()
#             except IndexError:
#                 return False
#
#     return len(parentheses_stack.list) == 0
#
# print(is_str_proper("(())"))






# """
# what is the output of this pseudocode?
# s1.init()     # s1 = None
# s1.push(7)    # s1 = [7]
# s1.push(9)    # s1 = [9, 7]
# s2.init()     # s2 = None
# x = s1.pop()  # s1 = [7]; x = 9
# s2.push(x)    # s2 = [9]
# s1.push(6)    # s1 = [6, 7]
# x = s2.pop()  # s2 = None; x = 9
# x = s1.pop()  # s1 = [7]; x = 6
# s1.push(8)    # s1 = [8, 7]
# """




# """
# what is the output of this pseudocode?
# s2.init()                                # s2 = None
# s1.init()                                # s1 = None
# s1.push(‘a’)                             # s1 = [a]
# s1.push(‘b’)                             # s1 = [b, a]
# s2.push(‘c’)                             # s2 = [c]
# x = s1.pop()                             # s1 = [a]; x = b
# s2.push(x)                               # s2 = [b, c]
# s1.pop()                                 # s1 = None
# if not s1.is_empty() → output: s1.peek() #
# else → output: s2.peek()                 # output: b
# """


# check if the string has a proper parentheses
# def is_str_proper(str):
#     left = 0
#     right = 0
#     opened = False
#     closed = False
#     for i in range(len(str)):
#         if not opened and str[i] == ")" and left != right:
#             return False
#         elif str[i] == "(":
#             left += 1
#             opened = True
#             closed = False
#         elif opened and str[i] == ")":
#             right += 1
#             closed = True
#             opened = False
#
#     return closed and left == right
#
# print(is_str_proper("(()())"))



# class Array(list):
#
#     def __init__(self, capacity):
#         super().__init__()
#         self.capacity = capacity
#
#     def is_full(self):
#         return len(self) == self.capacity
#
#     def append(self, value):
#         if not self.is_full():
#             super().append(value)
#
# class StackImplementationArray:
#
#     def __init__(self, capacity):
#         self.__array = Array(capacity)
#
#     def is_empty(self):
#         return len(self.__array) == 0
#
#     def push(self, value):
#         if not self.__array.is_full():
#             self.__array.append(value)
#
#     def pop(self):
#         return self.__array.pop()
#
#     def peek(self):
#         return self.__array[len(self.__array) - 1]


# limited_stack = StackImplementationArray(3)
#
# limited_stack.push(5)
# limited_stack.push(6)
# limited_stack.push(7)
#
# x = limited_stack.is_full()
# print(limited_stack.peek())
#
# print(x)

# from linked_list import LinkedList
#
#
# class StackImplementationLinkedList:
#
#     def __init__(self):
#         self.__linked_list = LinkedList()
#
#     def is_empty(self):
#         return self.__linked_list.len_list() == 0
#
#     def push(self, value):
#         self.__linked_list.insert_first(value)
#
#     def pop(self):
#         return self.__linked_list.remove_first()
#
#     def peek(self):
#         self.__linked_list.get_value(0)
#
# stack = StackImplementationLinkedList()
# stack.push(4)
# stack.push(10)
# stack.push(15)
# print(stack.pop())
# print(stack.pop())
# print(stack.is_empty())
# print(stack.pop())
# print(stack.is_empty())




# from linked_list import LinkedList
#
#
# class LimitedStackImplementationLinkedList:
#
#     def __init__(self, capacity):
#         self.__linked_list = LinkedList()
#         self.capacity = capacity
#
#     def is_empty(self):
#         return self.__linked_list.len_list() == 0
#
#     def push(self, value):
#         if self.__linked_list.len_list() < self.capacity:
#             self.__linked_list.insert_first(value)
#             return True
#         return False
#
#     def pop(self):
#         return self.__linked_list.remove_first()
#
#     def peek(self):
#         return self.__linked_list.get_value(0)

# limited_stack = LimitedStackImplementationLinkedList(3)
# print(limited_stack.is_empty()) # True
# limited_stack.push(1)
# limited_stack.push(2)
# limited_stack.push(3)
# print(limited_stack.is_empty()) # False
# pushed = limited_stack.push(4)
# print(pushed)                   # False
# print(limited_stack.peek())     # 3
# limited_stack.pop()
# pushed = limited_stack.push(4)
# print(pushed)                   # True
# print(limited_stack.peek())     # 4


