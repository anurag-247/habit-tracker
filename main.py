import requests
from datetime import datetime

USERNAME = "anurag304"
TOKEN = "*********"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

pixela_endpoint = "https://pixe.la/v1/users"

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_spec = {
    "id": "graph1",
    "name": "Cycling graph",
    "unit": "km",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# response = requests.post(url=graph_endpoint, json=graph_spec, headers=headers)
# print(response.text)
today = datetime(year=2024, month=8, day=6)
date = today.strftime("%Y%m%d")

pixel_spec = {
    "date": date,
    "quantity": "5"
}

pixel_endpoint = f"{graph_endpoint}/graph1"

# print(date)
# response = requests.post(url=pixel_endpoint, json=pixel_spec, headers=headers)
# print(response.text)

pixel_update = f"{pixel_endpoint}/{date}"
update_params = {
    "quantity": "2"
}
# response = requests.put(url=pixel_update, json=update_params, headers=headers)
# print(response.text)

response = requests.delete(url=pixel_update, headers=headers)
print(response.text)
