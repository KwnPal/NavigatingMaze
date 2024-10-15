import copy

class agent:
    def __init__(self, maze):
        self.agent_position = [0,0]
        self.maze = maze
        self.moveset={
            0: self.left,
            1: self.right,
            2: self.down,
            3: self.up
                    }
        self.mapping ={
            0: (-1, False),
            1: (-0.04, False),
            "E": (100, True)
        }
        
    def action_update(self,action):
        reward=self.moveset[action]()
        return self.mapping[reward]

    def is_wall(self, ptr, move):
        temp = self.agent_position.copy()
        temp[ptr] = move
        reward = self.maze.maze[temp[0]][temp[1]]
        if reward != 0:
            self.agent_position[ptr] = move
        return reward

    def up(self):
        ptr = 0 # defines if the agent movement 0 -> vertically 1-> horizontally
        pos = max(self.agent_position[ptr] - 1, 0) # defines the step, the agent makes
        if self.agent_position[ptr] - 1 < 0:
            return 0
        reward = self.is_wall(ptr, pos)
        return reward
            
   
    def down(self):
        ptr = 0
        pos = min(self.agent_position[ptr] + 1, self.maze.height-1)
        if self.agent_position[ptr] + 1 > self.maze.height-1 : 
            return 0
        reward = self.is_wall(ptr, pos)
        return reward
    
    def right(self):
        ptr = 1
        pos = min(self.agent_position[ptr] + 1, self.maze.width-1)
        if self.agent_position[ptr] + 1 > self.maze.width-1:
            return 0
        reward = self.is_wall(ptr, pos)
        return reward
    
    def left(self):
        ptr = 1
        pos = max(self.agent_position[ptr] - 1, 0)
        if self.agent_position[ptr] -1 <0:
            return 0
        reward = self.is_wall(ptr, pos)
        return reward
         
