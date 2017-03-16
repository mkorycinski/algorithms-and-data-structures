def preorder(tree):
    if tree:
        print(tree.get_root())
        preorder(tree.get_left_child())
        preorder(tree.get_right_child())


def postorder(tree):
    if tree:
        preorder(tree.get_left_child())
        print(tree.get_root())
        preorder(tree.get_right_child())


def inorder(tree):
    if tree:
        postorder(tree.get_left_child())
        postorder(tree.get_right_child())
        print(tree.get_root())
