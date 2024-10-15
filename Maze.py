import os
import time

class maze:
    def __init__(self, width, height, id, maze):
        self.id= id
        self.maze = maze
        self.width = width
        self.height = height

    def print_maze(self):
        # os.system("cls")
        print("-" + self.width * "---")
        for i in self.maze:
            formatted_row = [f'{str(cell):>2}' for cell in i]
            print("|"+' '.join(formatted_row)+"|")
        print("-" + self.width * "---")
        
    