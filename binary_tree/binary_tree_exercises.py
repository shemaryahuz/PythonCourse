class TreeNode:
    """class to create a node object for binary tree"""
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    """class to create a binary search tree object"""
    def __init__(self):
        self.root = None

    def _rec_insert(self, root, data):
        """recursive function to insert data to the tree"""
        # if current data <= data, go to the right
        if root.data <= data:
            # if the right field is None insert to the right
            if root.right is None:
                root.right = TreeNode(data)
            # else, call the recursive function with the right node
            else:
                self._rec_insert(root.right, data)
        # if current data > data, go to the left
        else:
            # if the left field is None insert to the left
            if root.left is None:
                root.left = TreeNode(data)
            # else, call the recursive function with the left node
            else:
                self._rec_insert(root.left, data)

    def insert(self, data):
        """insert data to the tree by using recursive function"""
        # if the tree is empty insert to the root
        if self.root is None:
            self.root = TreeNode(data)
        # else, call the recursive function with the root
        else:
            self._rec_insert(self.root, data)

    def _rec_find(self, root, data):
        """recursive function to find data in the tree"""
        # if the current node is None, return False
        if root is None:
            return False
        # if the current data == data, return True
        if root.data == data:
            return True
        # if the current data <= data, go to the right
        if root.data <= data:
            return self._rec_find(root.right, data)
        # if the current data > data, go to the left
        else:
            return self._rec_find(root.left, data)

    def find(self, data):
        """return True if the data is in the tree. else, return False"""
        # call the recursive find function
        return self._rec_find(self.root, data)

    def min(self):
        """return the minimum data in the tree"""
        pointer = self.root
        while pointer.left:
            pointer = pointer.left
        return pointer.data

    def max(self):
        """return the maximum data in the tree"""
        pointer = self.root
        while pointer.right:
            pointer = pointer.right
        return pointer.data

    def print_tree(self):
        pass

binary_tree = BinarySearchTree()
