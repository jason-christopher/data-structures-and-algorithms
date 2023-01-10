from data_structures.queue import Queue


class KaryTree:
    def __init__(self, root=None):
        self.root = root

    def breadth_first(self):
        # queue = Queue()
        #
        # collection = []
        #
        # queue.enqueue(self.root)
        #
        # while not queue.is_empty():
        #     node = queue.dequeue()
        #     collection.append(node.value)
        #     for child in node.children:
        #         queue.enqueue(child)
        #
        # return collection

        try:
            result, queue = [], [self.root]
            while queue:
                front = queue.pop(0)
                result.append(front.value)
                for child in front.children:
                    queue.append(child)
            return result
        except:
            return []


class Node:
    """K-Ary Tree Node"""

    def __init__(self, value):
        self.value = value
        self.children = []
