class Single(object):

    def __init__(self, value):
        self.value = value
        self.next_node = None


class Double(object):
    def __init__(self, value):
        self.value = value
        self.next_node = None
        self.prev_node = None


if __name__ == '__main__':

    a = Double(1)
    b = Double(2)
    c = Double(3)
    d = Double(4)

    a.next_node = b
    b.prev_node = a
    b.next_node = c
    c.prev_node = b
    c.next_node = d
    d.prev_node = c

    print(d.prev_node.value)
    print(c.next_node.value)
