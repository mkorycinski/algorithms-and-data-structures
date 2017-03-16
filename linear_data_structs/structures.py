class struct(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)


class Stack(struct):

    def push(self, element):
        self.items.append(element)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]



class Queue(object):

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)
        # self.items.append(item)

    def dequeue(self):
        return self.items.pop()
        # item = self.items[0]
        # self.items.remove(0)
        # return item

class Deque(object):

    def __init__(self):
        self.items = []

    def add_front(self, item):
        self.items.insert(0, item)

    def add_end(self, item):
        self.items.append(item)

    def remove_front(self):
        return self.items.pop(0)

    def remove_end(self):
        return self.items.pop()