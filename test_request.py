import requests
import json

url = 'http://localhost:5000/generate'
headers = {'Content-Type': 'application/json'}
data = {'prompt': 'Tell me a joke'}

response = requests.post(url, headers=headers, data=json.dumps(data))

print('Status code:', response.status_code)
print('Response:', response.json())
