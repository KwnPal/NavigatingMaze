import requests
import json
import numpy as np
# Use this in case of API usage
class Env_API:
    def __init__(self,url):
        self.url=url
        self.uuid = None
        self.createEnv()

    def createEnv(self):
        response = requests.post(self.url+"/new_game")
        if response.status_code == 200:
            data = response.json()
            obs = response.json()["observation_space"]
            self.uuid = data["uuid"]
            self.high = int(obs["high"])
            self.low = int(obs["low"])
            print("New env created \nuuid: "+self.uuid)
        else:
            print("Can't create new Env status code"+response.status_code)

    def reset(self):
        response = requests.post(self.url+"/reset/"+self.uuid)
        try:
            data = np.array(response.json()["observation"],dtype=np.float32)
            return data
        except requests.exceptions.RequestException:
            print("Error Code ",response.status_code)
            print(response.text)
            
    def step(self,action):
        body = {"action" : int(action)}
        try:
            response = requests.post(self.url+"/step/"+self.uuid, json=body)
            done = response.json()["done"] # If True the game resets and the agent either found the exit or something else is wrong
            info = response.json()["info"]
            observation = np.array(response.json()["observation"],dtype=np.float32)# The location of the agent in the maze
            reward = response.json()["reward"]# Reward of the step
            truncated = response.json()["truncated"] # If True the game resets (we usually create a rule like max steps or too many failed steps)
            return observation,reward,done,truncated,info
        except requests.exceptions.Timeout as e:# If there is a connection timeout the environment resets
            print("An error occurred: \n",response.status_code) 
            observation = np.zeros((2,), dtype=np.float32) 
            reward = -1.0  
            done = True  
            truncated = False 
            info = {"error": str(e)}

            return observation, reward, done, truncated, info
            
