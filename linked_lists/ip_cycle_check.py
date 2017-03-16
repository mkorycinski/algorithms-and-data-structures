from single_linked_list import Node
import time

# Cycle collection
a = Node(1)
b = Node(2)
c = Node(3)

a.next_node = b
b.next_node = c
c.next_node = a


# Non-cycle list
x = Node(1)
y = Node(2)
z = Node(3)

x.next_node = y
y.next_node = z


def cycle_check(node):

    seen = []
    curr_node = node

    while curr_node.next_node:
        if curr_node in seen:
            return True

        seen.append(curr_node)
        curr_node = curr_node.next_node

    return False

t = time.clock()
print(cycle_check(a))
print(cycle_check(x))
end = time.clock() - t
print(end)


def marker_solution(node):

    marker1 = node
    marker2 = node

    while marker2 != None and marker2.next_node != None:
        marker1 = marker1.next_node
        marker2 = marker2.next_node.next_node

        if marker2 == marker1:
            return True

    return False

t = time.clock()
print(marker_solution(a))
print(marker_solution(x))
end = time.clock() - t
print(end)