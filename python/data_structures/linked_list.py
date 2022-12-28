class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        self.val = Node(value)
        self.val.next = self.head
        self.head = self.val

    def includes(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return True
        current = current.next
        return False

    def __str__(self):
        current = self.head
        string = ""
        while current is not None:
            string += "{ " + str(current.value) + " } -> "
            current = current.next
        return string + "NULL"


class TargetError:
    pass
