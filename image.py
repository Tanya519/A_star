from main import main
from PIL import Image
import numpy as np
from search.Node import Node

grid = main()
for i in range(0, Node.map_width):
    for j in range(0, Node.map_height):
        if grid[i][j] == '.':
            grid[i][j] = [0, 0, 0]
        if grid[i][j] == '@':
            grid[i][j] = [67, 65, 78]
        if grid[i][j] == "*":
            grid[i][j] = [140, 45, 78]
        if grid[i][j] == "E":
            for k in [-1, 0, 1]:
                for l in [-1, 0, 1]:
                    grid[i+k][j+l] = [0, 255, 0]

        if grid[i][j] == 'S':
            for k in [-1, 0, 1]:
                for l in [-1, 0, 1]:
                    grid[i+k][j+l] = [250, 0, 0]

decrypted_rgb = np.array(grid)
new_image = Image.fromarray(decrypted_rgb.astype('uint8'))
new_image.save('path.png')
