"""Stack exercises part 2"""
from searches.class_exercises import len_list
from sorting.basic import array


# exercise 1
class ListStack:

    def __init__(self):
        self.list = []

    def push(self, value):
        self.list.append(value)

    def pop(self):
        return self.list.pop()

    def is_empty(self):
        return self.list == 0

# exercise 2
class ArrayStack(list):
    def __init__(self):
        super().__init__()
        self.__array = []
        self.capacity = 3

    def push(self, value):
        if len(self.__array) < self.capacity:
            self.__array.append(value)
        else:
            return False

    def pop(self, index = -1):
        return self.__array.pop()

    def peek(self):
        return self.__array[-1]

    def is_empty(self):
        return self.__array == 0

    def overflow(self):
        if len(self.__array) == self.capacity:
            print("The stack is full")

# exercise 3
from linked_list import LinkedList

class LinkedListStack:

    def __init__(self):
        self.linked_list = LinkedList()

    def push(self, value):
        self.linked_list.insert_first(value)

    def pop(self, index = -1):
        return self.linked_list.remove_first()

    def peek(self):
        return self.linked_list.get_value(0)

    def is_empty(self):
        return self.linked_list.len_list() == 0

# exercise 4
class LimitedLinkedListStack(LinkedListStack):

    def __init__(self):
        super().__init__()
        self.capacity = 3

    def push(self, value):
        if self.linked_list.len_list() < self.capacity:
            super().push(value)


# exercise 5

    def overflow(self):
        if self.linked_list.len_list() == self.capacity:
            print("The stack is full")