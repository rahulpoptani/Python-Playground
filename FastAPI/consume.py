import requests, json

response = requests.get('http://localhost:8000/user')
response = json.loads(response.text)

print(response.get('profile'))