from search.map import Map
from search.Node import Node
from search.algorithms import AStar
import random
import time

EPS = 0.01
N = 100

def read_scen(path):
    tasks = []
    with open('scen/' + path + '.map.scen') as taskFile:
        lines = taskFile.readlines()[1:]
    for line in lines:
        coord = line.split()
        tasks.append({'y_start': int(coord[-5]), 'x_start': int(coord[-4]), 'y_end': int(
            coord[-3]), 'x_end': int(coord[-2]), 'cost': float(coord[-1])})
    return random.sample(tasks, N)




file_names = ['Moscow_1_512', 'Berlin_0_256', 'London_2_1024', 'Denver_0_512']

tasks_file = {}
for file in file_names:
    tasks_file[file] = read_scen(file)

k = 0
time_list = []
cost_list = []
for map in file_names:
    gridded_map = Map('maps/' + map + '.map')
    astar = AStar(gridded_map)

    Node.Cut_corners = True

    tasks = tasks_file[map]
    for task in tasks:
        try:
            start = Node(task['x_start'], task['y_start'])
            end = Node(task['x_end'], task['y_end'])
            start_time = time.time()
            ans, cost = astar.search(start, end)
            end_time = time.time()
            astar_time = end_time - start_time
            time_list.append(astar_time)
            cost_list.append(cost)

            assert(abs(cost - task['cost']) <  EPS)

        except Exception as e:
            k += 1 
            print("Cost Error", map )
            print(e)

print(f'successful tests: {4*N-k}')
print(f'failed tests: {k}')

   