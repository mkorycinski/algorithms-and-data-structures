class Node(object):

    def __init__(self, value):
        self.value = value
        self.next_node = None

# Non-cycle list
x = Node(1)
y = Node(2)
z = Node(3)
zz = Node(4)

x.next_node = y
y.next_node = z
z.next_node = zz


def reverse_llist(head):
    current = head
    previous = None
    next_node = None

    while current:
        next_node = current.next_node
        current.next_node = previous
        previous = current
        current = next_node

    return previous

reverse_llist(x)


print(zz.next_node.value)
print(z.next_node.value)
print(y.next_node.value)
print(x.next_node.value)
