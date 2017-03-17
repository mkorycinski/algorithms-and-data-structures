import unittest

class HashTable(object):

    def __init__(self, t_size):
        self.size = t_size
        self.slots = [None] * self.size

        self.data = [None] * self.size

    def put(self, key, data):

        hash_val = self.hash_func(key, len(self.slots))

        if not self.slots[hash_val]:
            self.slots[hash_val] = key
            self.data[hash_val] = data

        else:
            if self.slots[hash_val] == key:
                self.data[hash_val] = data

            else:
                next_slot = self.rehash(hash_val)

                while self.slots[next_slot] and self.slots[next_slot] != key:
                    next_slot = self.rehash(next_slot)

                if not self.slots[next_slot]:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data
                else:
                    self.data[next_slot] = data

    def hash_func(self, key):
        return key % self.size

    def rehash(self, hash_val):
        return ((hash_val)+1) % self.size

    def get(self, key):

        start_slot = self.hash_func(key)
        data = None
        stop = False
        found = False
        position = start_slot

        while self.slots[position] and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]

            else:
                position = self.rehash(position)
                if position == start_slot:
                    stop = True

        return data

    def __getitem__(self, item):
        return self.get(item)

    def __setitem__(self, key, value):
        self.put(key=key, data=data)


class TestHashes(unittest.TestCase):

    def setUp(self):
        self.h = HashTable(5)

        self.h[1] = 'one'
        self.h[2] = 'two'
        self.h[3] = 'three'