from search.Node import Node

import math


class Map:

    def __init__(self, file_name):
        self.file_name = file_name
        self.map_file = open(self.file_name)
        self.type_map = self.map_file.readline()
        self.height = int(self.map_file.readline().split(' ')[1])
        self.width = int(self.map_file.readline().split(' ')[1])
        # self.map_lines = 0

        Node.map_width = self.width
        Node.map_height = self.height

        self.read_map()
        self.map_file.close()

    def read_map(self):
        map = open(self.file_name)
        map.readline()
        self.height = int(map.readline().split(' ')[1])
        self.width = int(map.readline().split(' ')[1])
        map.readline()
        lines = map.readlines()
        self.grid = [[0 for _ in range(self.width)]
                     for _ in range(self.height)]
        self.map_lines = [line[:-1] for line in lines]
        # self.map_lines = map_lines
        self.picture =  [['.' for _ in range(self.width)]
                     for _ in range(self.height)]
        for i in range(0, self.height):
            for j in range(0, self.width):
                if self.map_lines[i][j] == '@':
                    self.grid[i][j] = 1
                    self.picture[i][j] = '@'
        map.close()

    def is_valid_pair(self, x, y):
        if x < 0 or y < 0:
            return False
        if y >= self.width or x >= self.height:
            return False
        if self.grid[x][y] == 1:
            return False
        # if Node.Cut_corners:
        #     if self.grid[]

        return True

    def cost(self, x, y):

        if x == 0 or y == 0:
            return 1
        else:
            return math.sqrt(2)

    def successors(self, node):
        children = []
        parent = node.parent

        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                if self.is_valid_pair(node.get_x() + i, node.get_y() + j):
                    s = Node(node.get_x() + i, node.get_y() + j)
                    s.set_g(node.get_g() + self.cost(i, j))
                    children.append(s)

                    if Node.Cut_corners:
                        for k in [-1, 1]:
                            if node.get_x() + k < self.height and node.get_x() + k >= 0:
                                if self.grid[node.get_x() + k][node.get_y()] == 1:
                                    s1 = Node(node.get_x() + k, node.get_y() - 1)
                                    s2 = Node(node.get_x() + k, node.get_y() + 1)
                                    if s1 in children:
                                        children.remove(s1)
                                    if s2 in children:
                                        children.remove(s2)
                            else:
                                continue

                        for l in [-1, 1]:
                            if node.get_y() + l < self.width and node.get_y() + l >= 0:
                                if self.grid[node.get_x()][node.get_y()+l] == 1:
                                    d1 = Node(node.get_x()-1, node.get_y() + l)
                                    d2 = Node(node.get_x()+1, node.get_y() + l)
                                    if d1 in children:
                                        children.remove(d1)
                                    if d2 in children:
                                        children.remove(d2)
                            else:
                                continue

        return children
