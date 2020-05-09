import requests
import json

heroku_url = https://predictivapp.herokuapp.com/results
send_request = requests.post(heroku_url,json={'Pclass': 3, 'Age': 2, 'SibSp': 1, 'Fare': 50})

print(send_request.json())