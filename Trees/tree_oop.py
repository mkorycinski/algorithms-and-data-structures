class BinaryTree(object):
    """Binary tree representation"""

    def __init__(self, root_object):
        self.root = root_object
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        if not self.left_child:
            self.left_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.left_child = self.left_child
            self.left_child = t

    def insert_right(self, new_node):
        if not self.right_child:
            self.right_child = BinaryTree(new_node)

        else:
            temp = BinaryTree(new_node)
            temp.right_child = self.right_child
            self.right_child = temp

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_value(self, val):
        self.root = val

    def get_root(self):
        return self.root