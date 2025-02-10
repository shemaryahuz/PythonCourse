"""Linked List Class"""



# class Node:
#
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
# class LinkedList:
#
#     def __init__(self):
#         self.head = None
#
#     def is_empty(self):
#         if self.head == None:
#             return True
#         return False
#
#     def push(self, value):
#         node = Node(value)
#         if self.head == None:
#             self.head = node
#         else:
#             node.next = self.head
#             self.head = node
#
#     def append(self, value):
#         node = Node(value)
#         if self.head == None:
#             self.head = node
#         else:
#             pointer = self.head
#             while pointer.next != None:
#                 pointer = pointer.next
#             pointer.next = node
#
#     def delete_first(self):
#         if self.head == None:
#             return None
#         else:
#             deleted = self.head.data
#             self.head = self.head.next
#             return deleted
#
#     def delete_after(self, index):
#         if index >= self.length() - 1:
#            return None
#         else:
#             pointer = self.head
#             counter = 0
#             while counter < index:
#                 pointer = pointer.next
#                 counter += 1
#             deleted = pointer.next.data
#             pointer.next = pointer.next.next
#             return deleted
#
#     def find_by_value(self, value):
#         if self.head == None:
#             return None
#         else:
#             pointer = self.head
#             counter = 0
#             while pointer != None:
#                 if pointer.data == value:
#                     return counter
#                 pointer = pointer.next
#                 counter += 1
#             return None
#
#     def find_by_index(self, index):
#         if index > self.length() - 1:
#             return None
#         elif index == 0:
#             return self.head.data
#         else:
#             pointer = self.head
#             counter = 0
#             while counter < index:
#                 pointer = pointer.next
#                 counter += 1
#             return pointer.data
#
#     def length(self):
#         pointer = self.head
#         counter = 0
#         while pointer != None:
#             pointer = pointer.next
#             counter += 1
#         return counter
#
#     def print_list(self):
#         if self.head == None:
#             print(None)
#         else:
#             pointer = self.head
#             while pointer != None:
#                 print(pointer.data, end= " -> ")
#                 pointer = pointer.next
#             print(None)

"""testing for creating link list"""
#linked_list = LinkedList()

"""testing for is_empty function"""
# print(linked_list.is_empty()) # True
# linked_list.push("a")
# print(linked_list.is_empty()) # False

"""testing for push function"""
# linked_list.push("c")
# linked_list.print_list() # c -> a -> None


"""testing for append function"""
# linked_list = LinkedList()
# linked_list.append("d")
# linked_list.print_list() # d -> None
# linked_list.append("e")
# linked_list.print_list() # d -> e -> None

"""testing for delete_first function"""
# linked_list.delete_first()
# linked_list.print_list()                 # e -> None
# is_deleted = linked_list.delete_first()
# linked_list.print_list()                 # None
# print(is_deleted)                        # e

"""testing for delete_after function"""
# is_deleted = linked_list.delete_after(0)
# print(is_deleted)                          # None
# linked_list.append("a")
# linked_list.append("b")
# linked_list.append("c")
# is_deleted = linked_list.delete_after(1)
# linked_list.print_list()                   # a -> b -> None
# print(is_deleted)                          # c


"""testing for find_by_value function"""
# founded = linked_list.find_by_value("a")
# print(founded)                            # None
# linked_list.append("a")
# linked_list.append("b")
# linked_list.append("c")
# founded = linked_list.find_by_value("c")
# print(founded)                            # 2
# founded = linked_list.find_by_value("d")
# print(founded)                            # None


"""testing for find_by_index function"""
# founded = linked_list.find_by_index(0)
# print(founded)                         # None
# linked_list.append("a")
# linked_list.append("b")
# linked_list.append("c")
# founded = linked_list.find_by_index(0)
# print(founded)                         # a
# founded = linked_list.find_by_index(3)
# print(founded)                         # None
# founded = linked_list.find_by_index(2)
# print(founded)                         # c

"""testing for length function"""
# print(linked_list.length()) # 0
# linked_list.append("a")
# linked_list.append("b")
# linked_list.append("c")
# print(linked_list.length()) # 3

"""testing for print_list function"""
# linked_list.print_list() # None
# linked_list.append("a")
# linked_list.append("b")
# linked_list.append("c")
# linked_list.print_list() # a -> b -> c -> None