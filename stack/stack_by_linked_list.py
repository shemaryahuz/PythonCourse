from linked_list import LinkedList


class StackByLinkedList:

    def __init__(self):
        self.__linked_list = LinkedList()


    def is_empty(self):
        return self.__linked_list.len_list() == 0

    def push(self, value):
        self.__linked_list.insert_first(value)

    def pop(self):
        return self.__linked_list.remove_first()

    def peek(self):
        return self.__linked_list.get_value(0)
