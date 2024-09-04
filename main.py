from datetime import datetime
import os
import requests
from dotenv import load_dotenv, find_dotenv

found_env = find_dotenv(".env")
load_dotenv(found_env)

pixela_endpoint = os.getenv("PIXELA_ENDPOINT")
TOKEN = os.getenv("TOKEN")
USERNAME = os.getenv("USER")
GRAPH_ID = "graph1"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "commit",
    "type": "float",
    "color": "kuro"
}

headers = {
    "X-USER-Token": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

today = datetime.now()
today_formatted = today.strftime("%Y%m%d")

pixel_config = {
    "date": today_formatted,
    "quantity": input("How many hours did you spend coding today? "),
}

response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)

# update_endpoint = f"{pixel_endpoint}/{today_formatted}"

# response = requests.put(url=update_endpoint, json=pixel_config, headers=headers)
# print(response.text)

# delete_endpoint = f"{pixel_endpoint}/{today_formatted}"
#
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
