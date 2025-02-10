"""Linked List"""

class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def insert_first(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def insert_last(self, value):
        node = Node(value)
        cur_point = self.head
        if not cur_point:
            self.head = node
        else:
            while cur_point.next:
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
        if self.head:
            removed = self.head.value
            self.head = self.head.next
            return removed

    def remove_lest(self):
        removed = None
        cur_point = self.head
        if not cur_point:
            pass
        elif not cur_point.next:
            removed = self.head.value
            self.head = None
        else:
            while cur_point.next.next:
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
        while cur_point:
            counter += 1
            cur_point = cur_point.next
        return counter

    def print_list(self):
        cur_point = self.head
        while cur_point:
            print(cur_point.value, end=" ")
            cur_point = cur_point.next
        print()