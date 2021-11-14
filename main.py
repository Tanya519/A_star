from search.algorithms import AStar
from search.map import Map
import numpy as np
from search.Node import Node
import contextlib
import time

def main():
    map_name = 'maps/Denver_0_512.map'

    time_list = []
    cost_list = []

    gridded_map = Map(map_name)
    astar = AStar(gridded_map)

    Node.Cut_corners = True
    start = Node(35, 10)
    end = Node(120, 504)
    start_time = time.time()
    ans, cost = astar.search(start, end)
    end_time = time.time()
    astar_time = end_time - start_time
    time_list.append(astar_time)
    cost_list.append(cost)
    print(cost)

    Grid = astar.map.picture

    path = []

    while ans.parent is not None:
        path.append(ans)
        ans = ans.parent
    path.append(ans)
    path = path[::-1]

    for i in range(0, len(path)):
        x = path[i]._x
        y = path[i]._y
        Grid[x][y] = '*'

    Grid[end.get_x()][end.get_y()] = 'E'
    Grid[start.get_x()][start.get_y()] = 'S'

    with open('path.txt', 'w') as f:
        with contextlib.redirect_stdout(f):
            for m in Grid:
                for v in m:
                    print(str(v).replace(' ', ''), end='')
                print()

    f.close()
    return Grid


if __name__ == "__main__":
    main()
