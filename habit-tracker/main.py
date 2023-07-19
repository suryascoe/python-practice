import requests
from datetime import datetime as dt

USERNAME = "surya96"
TOKEN = "q1w2e#R4Y6T*7Uy^(uI(0"
GRAPHID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# Creating User Account.
# response = requests.post(url=pixela_endpoint, json=user_params)
# response.raise_for_status()
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPHID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# Graph Creation
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"

today = dt.now()
today = today.strftime("%Y%m%d")

post_config = {
    "date": today,
    "quantity": input("How many Km did you cycled today. ")
}

# Post a new value to you pixela
response = requests.post(url=pixel_endpoint, json=post_config, headers=headers)
print(response.text)


update_endpoint = f"{pixel_endpoint}/{today}"
put_config = {
    "quantity": "14.46"
}

# Update any particular Date data.
# response = requests.put(url=update_endpoint, json=put_config, headers=headers)
# print(response.text)

delete_endpoint = f"{pixel_endpoint}/{today}"

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
