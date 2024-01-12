
import requests
# from github import Github, Auth

# github username
username = "frank-xw"
# url to request
url = f"https://api.github.com/users/{username}"
# make the request and return the json
user_data = requests.get(url)

user_data.json()
