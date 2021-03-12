import requests

response = requests.get(url="http://localhost:5024/animals/head/snake")

print(response.status_code)
print(response.json())
print(response.headers)
