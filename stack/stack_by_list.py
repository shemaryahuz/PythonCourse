class StackImplementationList:

    def __init__(self):
        self.__list = []

    def stack_is_empty(self):
        return len(self.__list) == 0

    def push(self, value):
        self.__list.append(value)

    def pop(self):
        return self.__list.pop()

    def peek(self):
        if not self.stack_is_empty():
            return self.__list[len(self.__list) - 1]