"""Course summary"""

"""Search functions"""

def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1

def binary_search(lst, target):
    low = 0
    high = len(lst)-1
    while low <= high:
        mid = (low + high)//2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            low = mid+1
        else:
            high = mid-1
    return -1



"""Sort functions"""

def selection_sort(lst):
    for i in range(len(lst)-1):
        for j in range(i+1, len(lst)):
            if lst[j] < lst[i]:
                lst[i], lst[j] = lst[j], lst[i]

def buble_sort(lst):
    for i in range(len(lst)):
        is_sorted = True
        for j in range(0, len(lst)-1-i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                is_sorted = False
        if is_sorted:
            break

def merge(a, b):
    c = []
    point_a = 0
    point_b = 0
    while point_a < len(a) and point_b < len(b):
        if a[point_a] <= b[point_b]:
            c.append(a[point_a])
            point_a += 1
        else:
            c.append(b[point_b])
            point_b += 1
    if point_a == len(a):
        c += b[point_b:len(b)]
    else:
        c += a[point_a:len(a)]
    return c

def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    left = lst[:len(lst)//2]
    right = lst[len(lst)//2:]
    return merge(merge_sort(left),merge_sort(right))



"""Recursive functions"""

def sum_arithmetic_series(n):
    if n == 1:
        return 1
    return n + sum_arithmetic_series(n-1)

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n - 2)

def hanoi_towers():
    ...



"""Linked list"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def len_list(self):
        counter = 0
        pointer = self.head
        while pointer:
            counter += 1
            pointer = pointer.next
        return counter

    def insert(self, val, index = 0):
        node = Node(val)
        if self.head is None:
            self.head = node
            self.tail = node
        elif index == 0:
            node.next = self.head
            self.head = node
        else:
            counter = 0
            pointer = self.head
            while counter != index-1:
                pointer = pointer.next
                counter += 1
            node.next = pointer.next
            pointer.next = node

    def append(self, val):
        node = Node(val)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def pop(self, index):
        if index == 0:
            deleted = self.head.val
            self.head = self.head.next
            last = self.len_list() - 1
            if last == 0:
                self.tail = self.head
            return deleted
        counter = 0
        pointer = self.head
        while counter != index-1:
            pointer = pointer.next
            counter += 1
        deleted = pointer.next.val
        pointer.next = pointer.next.next
        return deleted

    def get_val(self, index):
        if index == 0:
            return self.head.val
        counter = 0
        pointer = self.head
        while counter != index:
            pointer = pointer.next
            counter += 1
        return pointer.val

    def print_list(self):
        if self.head is None:
            print(None)
        else:
            pointer = self.head
            while pointer:
                print(pointer.val, end=" ")
                pointer = pointer.next
            print()



"""Stack"""
class StackLinkedList:
    def __init__(self):
        self._lst = LinkedList()
    def is_empty(self):
        return self._lst.len_list() == 0
    def push(self, val):
        self._lst.insert(val)
    def pop(self):
        return self._lst.pop(0)
    def peek(self):
        return self._lst.get_val(0)



"""Queue"""
class QueueLinkedList:
    def __init__(self):
        self._lst = LinkedList()
    def is_empty(self):
        return self._lst.len_list() == 0
    def enqueue_val(self, val):
        self._lst.append(val)
    def dequeue_last(self):
        return self._lst.pop(0)
    def head(self):
        return self._lst.get_val(0)



"""Binary search tree"""

class BinaryNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None
    def _recursive_insert(self, root, val):
        ...
    def insert(self, val):
        ...
    def _recursive_find(self, root, val):
        ...
    def find(self, val):
        ...
    def delete(self, val):
        ...
    def recursive_print(self, reverse):
        ...
    def print_in_order(self, reverse = False):
        ...
