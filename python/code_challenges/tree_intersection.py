from data_structures.binary_tree import BinaryTree
from data_structures.hashtable import Hashtable


def tree_intersection(tree1, tree2):
    def walk(root, is_first_tree):
        if is_first_tree:
            diction.set(root.value, 1)
        if diction.has(root.value) and not is_first_tree:
            result.append(root.value)
        if root.left:
            walk(root.left, is_first_tree)
        if root.right:
            walk(root.right, is_first_tree)
    diction, result = Hashtable(), []
    if tree1.root:
        walk(tree1.root, True)
    if tree2.root:
        walk(tree2.root, False)
    return set(result)
