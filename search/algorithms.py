import heapq
import math

from search.Node import Node


class AStar():

    def __init__(self, gridded_map):
        self.map = gridded_map
        self.OPEN = []
        self.CLOSED = {}

    def h_value(self, node):
        delta_x = node.get_x() - self.end.get_x()
        delta_y = node.get_y() - self.end.get_y()

        return math.sqrt((delta_x)**2 + (delta_y)**2)

    def search(self, start, end):

        self.OPEN = []
        self.CLOSED = {}
        self.end = end
        node_expanded = 0

        heapq.heappush(self.OPEN, start)

        while len(self.OPEN) > 0:
            node = heapq.heappop(self.OPEN)
            node_expanded += 1

            self.CLOSED[node.state_hash()] = node

            if node == self.end:
                cost_node = node.get_f()
                return node, cost_node

            # print(repr(node))
            for neighbour in self.map.successors(node):
                # print(node._x, node._y)
                if neighbour.state_hash() in self.CLOSED:
                    continue

                if neighbour in self.OPEN:
                    neighbour_index = self.OPEN[self.OPEN.index(neighbour)]
                    if neighbour.get_g() < neighbour_index.get_g():
                        neighbour_index.set_g(neighbour.get_g())
                        neighbour_index.set_f(neighbour.get_g() + self.h_value(neighbour_index))
                        heapq.heapify(self.OPEN)

                else:
                    neighbour.set_f(neighbour.get_g() + self.h_value(neighbour))
                    neighbour.parent = node
                    # print(neighbour)
                    heapq.heappush(self.OPEN, neighbour)

        return -1, 0
