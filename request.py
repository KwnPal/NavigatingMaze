import requests
import json 



# Checking status code
URL = "http://3.77.211.177:5005/"
ng=URL +"new_game"
reset=URL +"reset/"
response = requests.post(URL +"new_game")

with open('data.json', 'w') as json_file:
    json.dump(response.json(), json_file, indent=1)

uuid=response.json()["uuid"]
reset=reset+uuid
response2 =requests.post(reset)
print(response2.status_code)
