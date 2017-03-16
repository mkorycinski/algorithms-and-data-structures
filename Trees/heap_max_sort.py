class BinaryMax(object):

    def __init__(self):
        self.heap_list = [0]
        self.heap_size = 0

    def sift_up(self, i):
        while (i // 2) - 1 > 0:
            if self.heap_list[i] > self.heap_list[(i // 2) - 1]:
                tmp_element = self.heap_list[(i // 2) - 1]
                self.heap_list[(i // 2) - 1] = self.heap_list[i]
                self.heap_list[i] = tmp_element

            i //= 2

    def insert_node(self, node):

        self.heap_list.append(node)
        self.heap_size += 1
        self.sift_up(self.heap_size)

    def del_max_val(self):

        val = self.heap_list[1]

        self.heap_list[1] = self.heap_list[self.heap_size]
        self.heap_list.pop()
        self.heap_size -= 1
        self.sift_down(1)

        return val

    def get_max_child(self, i):

        if 2 * i + 1 > self.heap_size:
            return 2 * i

        else:
            if self.heap_list[2 * i] > self.heap_list[2 * i + 1]:
                return 2 * i

            else:
                return 2 * i + 1

    def sift_down(self, i):
        while i * 2 < self.heap_size:

            max_child = self.get_max_child(i)

            if self.heap_list[i] < self.heap_list[max_child]:
                tmp = self.heap_list[i]
                self.heap_list[i] = self.heap_list[max_child]
                self.heap_list[max_child] = tmp
            i = max_child

    def build_heap(self, alist):

        self.heap_size = len(alist)

        i = self.heap_size // 2
        self.heap_list = [0] + alist[:]

        while i > 0:
            self.sift_down(i)
            i -= 1


def sort_stuff(alist):

    m = BinaryMax()

    m.build_heap(alist)
    print(m.heap_list)

    s = []
    while m.heap_size > 0:
        s.append(m.del_max_val())

    return s


if __name__ == '__main__':
    print(sort_stuff(list(str(26317237091230))))
