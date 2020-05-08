import requests
import json

#url = 'http://localhost:5000/results'
heroku_url = https://predictivapp.herokuapp.com/
send_request = requests.post(heroku_url,json={'Pclass': 3, 'Age': 2, 'SibSp': 1, 'Fare': 50})

print(send_request.json())