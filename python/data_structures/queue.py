from data_structures.invalid_operation_error import InvalidOperationError


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    """
    Put docstring here
    """

    def __init__(self):
        self.front = None
        self.rear = None
        self.queue = []

    def enqueue(self, value):
        new_node = Node(value)
        self.queue.append(new_node)
        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            value = self.queue.pop(0)
            if self.is_empty():
                self.front = None
                self.rear = None
            else:
                self.front = self.queue[0]
            return value.value

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.front.value

    def is_empty(self):
        return len(self.queue) == 0
