import requests
import json
import numpy as np

class Env:

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

    def resetEnv(self):
        response = requests.post(self.url+"/reset/"+self.uuid)
        if response.status_code == 200:
            data = np.array(response.json()["observation"],dtype=np.float32)
            return data
        else:
            print("Error Code ",response.status_code)
            print(response.text)
            
    def step(self,action):
        body = {"action" : int(action)}
        try:
            response = requests.post(self.url+"/step/"+self.uuid , body)
            done = response.json()["done"]
            info = response.json()["info"]
            observation = np.array(response.json()["observation"],dtype=np.float32)
            reward = response.json()["reward"]
            truncated = response.json()["truncated"]
            return observation,reward,done,truncated,info
        except requests.exceptions.RequestException as e:
            print("An error occurred:",e) 
            return observation,reward,done,truncated,info
            
