"""Extract nth to the last element"""


class Node(object):
    def __init__(self, value):
        self.value = value
        self.next_node = None


#mark1 is left and mark2 is right pointer
def nth_to_last(n, node):
    mark1 = node
    mark2 = node

    for _ in range(n-1):
        if not mark2.next_node:
            raise LookupError('Error: n is larger than the linked list')
        mark2 = mark2.next_node

    while mark2.next_node:
        mark1 = mark1.next_node
        mark2 = mark2.next_node

    return mark1


if __name__ == '__main__':
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    e = Node(5)

    a.next_node = b
    b.next_node = c
    c.next_node = d
    d.next_node = e

    print(nth_to_last(2, a).value)
