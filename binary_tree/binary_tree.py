import queue
from inspect import stack


class BinaryNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, value):
        node = BinaryNode(value)
        if not self.root:
            self.root = node
        else:
            pointer = self.root
            prev = None
            while pointer:
                prev = pointer
                if pointer.value <= value:
                    pointer = pointer.right
                else:
                    pointer = pointer.left
            if prev.value <= value:
                prev.right = node
            else:
                prev.left = node

    def _rec_insert(self, root, value):
        if root.value <= value:
            if not root.right:
                root.right = BinaryNode(value)
            else:
                self._rec_insert(root.right, value)
        else:
            if not root.left:
                root.left = BinaryNode(value)
            else:
                self._rec_insert(root.left, value)

    def rec_insert(self, value):
        if not self.root:
            self.root = BinaryNode(value)
        else:
            self._rec_insert(self.root, value)

    def find(self, value):
        if not self.root:
            return False
        else:
            pointer = self.root
            while pointer:
                if pointer.value == value:
                    return True
                elif pointer.value <= value:
                    pointer = pointer.right
                else:
                    pointer = pointer.left
            return False

    def _rec_find(self, root, value):
        if not root:
            return False
        if root.value == value:
            return True
        if root.value < value:
            return self._rec_find(root.right, value)
        return self._rec_find(root.left, value)

    def rec_find(self, value):
        return self._rec_find(self.root, value)

    def max(self):
        if not self.root:
            return "the tree is empty"
        pointer = self.root
        while pointer.right:
            pointer = pointer.right
        return pointer.value

    def min(self):
        if not self.root:
            return "the tree is empty"
        pointer = self.root
        while pointer.left:
            pointer = pointer.left
        return pointer.value

    def _rec_sum_left(self, root):
        if not root:
            return 0
        return root.value + self._rec_sum_left(root.left)

    def sum_left(self):
        return self._rec_sum_left(self.root)

    def _rec_sum(self, root):
        if not root:
            return 0
        return root.value + self._rec_sum(root.left) + self._rec_sum(root.right)

    def sum(self):
        return self._rec_sum(self.root)

    def delete(self, value):
        if not self.root:
            return "the tree is empty"

        pointer = self.root
        prev = None
        # find the value node
        while pointer and pointer.value != value:
            prev = pointer
            if pointer.value <= value:
                pointer = pointer.right
            else:
                pointer = pointer.left

        if not pointer:
            return "value does not exist"

        # if the node has no children
        if not pointer.right and not pointer.left:
            if not prev:                                                  ## it is the root
                self.root = None
            elif prev.value <= value:
                prev.right = None
            else:
                prev.left = None
        # if the node has one child
        elif not pointer.right or not pointer.left:
            if not prev:
                if not pointer.right:
                    self.root = pointer.left
                else:
                    self.root = pointer.right

            elif prev.value <= value:
                if pointer.right:
                    prev.right = pointer.right
                else:
                    prev.right = pointer.left
            else:
                if pointer.right:
                    prev.left = pointer.right
                else:
                    prev.left = pointer.left
        # if the node has two children
        else:
            target = pointer
            pointer = pointer.left
            if not pointer.right:
                target.value = pointer.value
                target.left = pointer.left
            else:
                while pointer.right:
                    prev = pointer
                    pointer = pointer.right

                target.value = pointer.value
                prev.right = pointer.left

    def _rec_print_ascending(self, root):
        if not root:
            return
        self._rec_print_ascending(root.left)
        print(root.value, end= " ")
        self._rec_print_ascending(root.right)
        if root == self.root:
            print()

    def _rec_print_descending(self, root):
        if not root:
            return
        self._rec_print_descending(root.right)
        print(root.value, end=" ")
        self._rec_print_descending(root.left)
        if root == self.root:
            print()

    def print_in_order(self, reverse = False):
        if not self.root:
            print(None)
        if not reverse:
            self._rec_print_ascending(self.root)
        else:
            self._rec_print_descending(self.root)



# b_tree = BinarySearchTree()

# b_tree.rec_insert(4)
# b_tree.rec_insert(2)
# b_tree.rec_insert(1)
# b_tree.rec_insert(3)
# b_tree.rec_insert(6)
# b_tree.rec_insert(5)
# b_tree.rec_insert(7)
#
# print(b_tree.delete(4))
# b_tree.print_in_order()
# print(b_tree.sum())
# print(b_tree.sum_left())


