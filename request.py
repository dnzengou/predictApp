import requests
import json

url = 'http://localhost:7070/results'
send_request = requests.post(url,json={'Pclass': 3, 'Age': 2, 'SibSp': 1, 'Fare': 50})

print(send_request.json())