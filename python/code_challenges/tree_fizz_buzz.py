from data_structures.binary_tree import BinaryTree
from data_structures.kary_tree import KaryTree, Node


def fizz_buzz_tree(tree):
    try:
        # new_tree = tree
        new_node = Node(tree.root.value)
        new_node.children = tree.root.children.copy()
        new_tree = KaryTree(new_node)

        def fizz_buzz(root):
            if not root:
                return None
            if root.value % 3 == 0 and root.value % 5 == 0:
                root.value = "FizzBuzz"
            elif root.value % 3 == 0:
                root.value = "Fizz"
            elif root.value % 5 == 0:
                root.value = "Buzz"
            else:
                root.value = str(root.value)
            for child in root.children:
                fizz_buzz(child)
            return root

        new_tree.root = fizz_buzz(new_tree.root)

        return new_tree
    except:
        return KaryTree()


