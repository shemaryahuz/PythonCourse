"""Regular List"""


# is_list = [0, 1, 2, 3, 4, 5, 6, 7, 8 ,9]
#
# print(is_list)
#
# is_list.append(10)# O(1)
#
# is_list.insert(0,-1)# O(n)
#
# print(is_list)
#
# is_list.pop()# O(1)
#
# is_list.pop(0)# O(n)
#
# print(is_list)


"""Linked List"""

class Node:

    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class LinkedList:

    def __init__(self):
        self.head = None

    def insert_first(self, value):
        node = Node(value)
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def insert_last(self, value):
        node = Node(value)
        cur_point = self.head
        if cur_point == None:
            self.head = node
        else:
            while cur_point.next != None:
                cur_point = cur_point.next
            cur_point.next = node

    def insert(self, index, value):
        if index == 0:
            self.insert_first(value)
        elif index == self.len_list():
            self.insert_last(value)
        else:
            node = Node(value)
            cur_point = self.head
            counter = 0
            while counter < index - 1:
                cur_point = cur_point.next
                counter += 1
            node.next = cur_point.next
            cur_point.next = node

    def remove_first(self):
        if self.head != None:
            removed = self.head.value
            self.head = self.head.next
            return removed

    def remove_lest(self):
        removed = None
        cur_point = self.head
        if cur_point == None:
            pass
        elif cur_point.next == None:
            removed = self.head.value
            self.head = None
        else:
            while cur_point.next.next != None:
                cur_point = cur_point.next
            removed = cur_point.next.value
            cur_point.next = None
        return removed

    def remove_by_index(self, index):
        if index == 0:
            return self.remove_first()
        elif index == self.len_list() - 1:
            return self.remove_lest()
        else:
            cur_point = self.head
            counter = 0
            while counter < index - 1:
                cur_point = cur_point.next
                counter += 1
            removed = cur_point.next.value
            cur_point.next = cur_point.next.next
            cur_point.next.next = None
            return removed

    # def remove_by_value(self, value):
    #
    #     if self.head.value == value:
    #         self.head = self.head.next
    #     else:
    #         cur_point = self.head
    #         while cur_point.next != None:
    #             if cur_point.value == value:
    #                 cur_point
    #             cur_point = cur_point.next

    def get_value(self, index):
        cur_point = self.head
        counter = 0
        while counter < index:
            cur_point = cur_point.next
            counter += 1
        return cur_point.value

    def len_list(self):
        cur_point = self.head
        counter = 0
        while cur_point != None:
            counter += 1
            cur_point = cur_point.next
        return counter

    def print_list(self):
        cur_point = self.head
        while cur_point != None:
            print(cur_point.value, end=" ")
            cur_point = cur_point.next
        print()

# is_list = LinkedList()
# is_list.insert_last(4)
# is_list.insert_last(5)
# is_list.insert_last(6)
# is_list.insert_last(7)
#
# x = is_list.remove_by_index(2)
# print(x)
# is_list.print_list()