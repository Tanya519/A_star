
class Node:

    map_width = 0
    map_height = 0

    Cut_corners = True

    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._g = 0
        self._h = 0
        self._f = 0
        self.parent = None

    def set_parent(self, parent):
        self.parent = parent

    def __repr__(self):
        return '({0}, {1})'.format(self._x, self._y)

    def __lt__(self, other):
        return self._f < other._f

    def state_hash(self):
        return self._y * Node.map_width + self._x

    def __eq__(self, other):
        return self._x == other._x and self._y == other._y

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_g(self):
        return self._g

    def get_h(self):
        return self._h

    def get_f(self):
        return self._f

    def set_g(self, cost):
        self._g = cost

    def set_h(self, h):
        self._h = h

    def set_f(self, cost):
        self._f = cost
