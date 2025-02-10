"""Exercises part 3"""


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def append(self, value):
        node = Node(value)
        if self.head == None:
            self.head = node
        else:
            pointer = self.head
            while pointer.next != None:
                pointer = pointer.next
            pointer.next = node

    def print_list(self):
        if self.head == None:
            print(None)
        else:
            pointer = self.head
            while pointer != None:
                print(pointer.data, end= " -> ")
                pointer = pointer.next
            print(None)

    # exercise1
    def sum_values(self):
        if self.head == None:
            return 0

        is_sum = 0
        pointer = self.head
        while pointer != None:
            is_sum += pointer.data
            pointer = pointer.next
        return is_sum

    # exercise 2
    def split_nums_and_strs(self):

        if self.head == None:
            return  None

        nums_list = LinkedList()
        strs_list = LinkedList()
        pointer = self.head
        while pointer != None:
            if type(pointer.data) != str:
                nums_list.append(pointer.data)
            else:
                strs_list.append(pointer.data)

            pointer = pointer.next

        return nums_list, strs_list

    # exercise 3
    def merge_lists(self, other):

        if self.head == None:
            self.head = other.head
            return self

        elif other.head == None:
            other.head = self.head
            return other

        else:
            pointer = self.head
            while pointer.next != None:
                pointer = pointer.next
            pointer.next = other.head

        return self

    # exercise 4
    def is_sorted(self):

        if self.head == None:
            return None

        elif self.head.next == None:
            return  True

        else:
            cur_min = self.head.data
            pointer = self.head.next

            while pointer != None:
                if pointer.data < cur_min:
                    return False
                cur_min = pointer.data
                pointer = pointer.next

            return True

    # exercise 5
    def delete_value(self, value):

        if self.head != None:
            pointer = self.head
            if pointer.data == value:
                self.head = self.head.next
            while pointer.next != None:
                if pointer.next.data == value:
                    pointer.next = pointer.next.next
                if pointer.next == None:
                    break
                pointer = pointer.next

    # exercise 6
    def non_duplicate_elements(self):
        if self.head == None or self.head.next == None:
            return self
        current = self.head.data
        pointer = self.head.next
        new_list = LinkedList()
        while pointer != None:
            continue



"""testing for exercise 1"""
# linked_list = LinkedList
# linked_list.append(5)
# linked_list.append(6)
# linked_list.append(9)
# print(linked_list.sum_values()) # 20


"""testing for exercise 2"""
# linked_list = LinkedList()
# linked_list.append(1)
# linked_list.append("a")
# linked_list.append(2)
# linked_list.append("b")
# linked_list.append(3)
# linked_list.append("c")
# linked_list.print_list() # 1 -> a -> 2 -> b -> 3 -> c -> None
# linked_list.split_nums_and_strs()[0].print_list() # 1 -> 2 -> 3 -> None
# linked_list.split_nums_and_strs()[1].print_list() # a -> b -> c -> None


"""testing for exercise 3"""
# linked_list1 = LinkedList()
# linked_list2 = LinkedList()
# linked_list1.merge_lists(linked_list2).print_list() # None
# linked_list2.append(1)
# linked_list2.append(2)
# linked_list1.merge_lists(linked_list2).print_list() # 1 -> 2 -> None
# linked_list2.merge_lists(linked_list1).print_list() # 1 -> 2 -> None
# linked_list1.append(3)
# linked_list1.append(4)
# linked_list2.merge_lists(linked_list1).print_list() # 1 -> 2 -> 3 -> 4 -> None
# linked_list1.merge_lists(linked_list2).print_list() # 3 -> 4 -> 1 -> 2 -> None


"""testing for exercise 4"""

# linked_list1 = LinkedList()
# print(f"linked list 1 is sorted? {linked_list1.is_sorted()}") # None
# linked_list1.append(1)
# print(f"linked list 1 is sorted? {linked_list1.is_sorted()}") # True
# linked_list1.append(2)
# linked_list1.append(3)
# linked_list1.append(4)
# print(f"linked list 1 is sorted? {linked_list1.is_sorted()}") # True
# linked_list2 = LinkedList()
# linked_list2.append(4)
# linked_list2.append(3)
# linked_list2.append(2)
# linked_list2.append(1)
# print(f"linked list 2 is sorted? {linked_list2.is_sorted()}") # False


"""testing for exercise 5"""
# linked_list2 = LinkedList()
# linked_list2.append(4)
# linked_list2.append(3)
# linked_list2.append(4)
# linked_list2.append(2)
# linked_list2.delete_value(4)
# linked_list2.print_list() # 3 -> 2 -> None
# linked_list2.delete_value(2)
# linked_list2.print_list() # 3 -> None


"""testing for exercise 6"""

