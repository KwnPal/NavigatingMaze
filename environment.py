import requests
import json

class Env:

    def __init__(self,url):
        self.url=url
        self.uuid = None
        self.createEnv()

    def createEnv(self):
        response = requests.post(self.url+"/new_game")
        if response.status_code == 200:
            data = response.json()
            self.uuid = data["uuid"]
            with open('data.json', 'w') as json_file:
                json.dump(response.json(), json_file, indent=1)
            print("New env created \nuuid: "+self.uuid)
        else:
            print("Can't create new Env status code"+response.status_code)


    def resetEnv(self):
        response = requests.post(self.url+"/reset/"+self.uuid)
        if response.status_code == 200:
            print("Environment has been reset")
            print(response.text)
        else:
            print("Error Code ",response.status_code)
            print(response.text)

    def step(self,action):
        body = {"action" : action}
        response = requests.post(self.url+"/step/"+self.uuid , json=body)
        if response.status_code == 200:
            print("Step has been made\n---------")
            done = response.json()["done"]
            info = response.json()["info"]
            observation = response.json()["observation"]
            reward = response.json()["reward"]
            truncated = response.json()["truncated"]
            return done, info, observation, reward, truncated 

        else:
            print("Error Code ",response.status_code,"\n"+response.text)
            return None, None, None, None , None