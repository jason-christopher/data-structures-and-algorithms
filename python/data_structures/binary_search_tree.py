from data_structures.binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):
    def add(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return
        node = self.root
        while True:
            if value < node.value:
                if not node.left:
                    node.left = new_node
                    break
                node = node.left
            elif value > node.value:
                if not node.right:
                    node.right = new_node
                    break
                node = node.right
            else:
                break

    def contains(self, value):
        node = self.root
        while node:
            if value < node.value:
                node = node.left
            elif value > node.value:
                node = node.right
            else:
                return True
            return False
