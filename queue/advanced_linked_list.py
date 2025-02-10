"""Advanced Linked List"""

class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

class AdvancedLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_first(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node

    def append_last(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def insert(self, index, value):
        if index == 0:
            self.insert_first(value)
        elif index == self.len_list():
            self.append_last(value)
        else:
            node = Node(value)
            cur_point = self.head
            counter = 0
            while counter < index - 1:
                cur_point = cur_point.next
                counter += 1
            node.next = cur_point.next
            cur_point.next = node

    def pop_first(self):
        if self.head:
            removed = self.head.value
            if self.head == self.tail:
                self.tail = None
            self.head = self.head.next
            return removed

    def pop_lest(self):
        removed = None
        cur_point = self.head
        if not cur_point:
            pass
        elif not cur_point.next:
            removed = self.head.value
            self.head = None
            self.tail = None
        else:
            while cur_point.next.next:
                cur_point = cur_point.next
            removed = cur_point.next.value
            self.tail = cur_point
            self.tail.next = None
        return removed

    def pop(self, index):
        if index == 0:
            return self.pop_first()
        elif index == self.len_list() - 1:
            return self.pop_lest()
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


# is_list = AdvancedLinkedList()
# is_list.insert_first(2)
# is_list.append_last(5)
# is_list.append_last(8)
# is_list.print_list() # 2 5 8
# is_list.pop_first()
# is_list.pop_lest()
# is_list.print_list() # 5
# is_list.append_last(9)
# is_list.append_last(11)
# is_list.append_last(13)
# is_list.print_list()
# print(is_list.len_list()) # 4
# print(is_list.pop(1)) # 9
# is_list.print_list()
# is_list.insert(1, 7)
# is_list.print_list() # 5 7 11 13