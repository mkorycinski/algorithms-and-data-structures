"""Adjacency list implementation"""


class Vertex(object):
    def __init__(self, key):
        self.id = key
        self.connected_to = {}

    def add_neighbor(self, nbr, weight=0):
        self.connected_to[nbr] = weight

    def get_connections(self):
        return self.connected_to.keys()

    def get_id(self):
        return self.id

    def get_weight(self, nbr):
        return self.connected_to[nbr]

    def __str__(self):
        return '%s connected to: %s' % (str(self.id),
                                        str([x.id for x in self.connected_to]))


class Graph(object):
    def __init__(self):
        self.vert_list = {}
        self.num_vert = 0

    def add_vertex(self, key):
        self.num_vert += 1
        new_vertex = Vertex(key)
        self.vert_list[key] = new_vertex
        # return new_vertex

    def get_vert(self, key):
        try:
            return self.vert_list[key]
        except KeyError:
            return None

    def add_edge(self, f, t, cost=0):
        if f not in self.vert_list:
            self.add_vertex(f)

        if t not in self.vert_list:
            self.add_vertex(t)

        self.vert_list[f].add_neighbor(self.vert_list[t], cost)

    def get_vertices(self):
        return self.vert_list.keys()

    def __iter__(self):
        return iter(self.vert_list.values())

    def __contains__(self, item):
        return item in self.vert_list


g = Graph()

for i in range(6):
    g.add_vertex(i)

# print(g.vert_list)

g.add_edge(0, 1, 2)

for ver in g:
    print(ver)
    print(ver.get_connections())
    print('\n')
