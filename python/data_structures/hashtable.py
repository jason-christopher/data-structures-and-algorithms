from data_structures.linked_list import LinkedList


class Hashtable:
    def __init__(self, size=10):
        self.size = size
        self._buckets = [None] * size

    def set(self, key, value):
        hashed_key = self._hash(key)
        bucket = self._buckets[hashed_key]
        if not bucket:
            self._buckets[hashed_key] = LinkedList()
        self._buckets[hashed_key].insert([key, value])

    def get(self, key):
        bucket = self._buckets[self._hash(key)]
        if isinstance(bucket, LinkedList):
            current = bucket.head
            while current:
                if current.value[0] == key:
                    return current.value[1]
                current = current.next
        raise KeyError(f"Key not found: {key}")

    def has(self, key):
        bucket = self._buckets[self._hash(key)]
        if isinstance(bucket, LinkedList):
            current = bucket.head
            while current:
                if current.value[0] == key:
                    return True
                current = current.next
        return False

    def keys(self):
        keys = []
        for bucket in self._buckets:
            while isinstance(bucket, LinkedList) and bucket.head:
                keys.insert(0, bucket.head.value[0])
                bucket.head = bucket.head.next
        return keys

    def _hash(self, key):
        return hash(key) % self.size
        # hash = 0
        # for char in key:
        #     hash += ord(char)
        # return (hash * 19) % self.size
