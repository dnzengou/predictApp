# Deploy ML model with Flask to Heroku

Click the button below to quickly clone and deploy into Heroku acount.

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

Once deployed to your Heroku instance run the following:

```bash
curl -s -XPOST 'https://<name-of-your-heroku-app>.herokuapp.com/' -d '{"Pclass":3,"Age":2,"SibSp":1,"Fare":50}' -H 'accept-content: application/json'
```

Alternatively a simple python script:

```python
import requests
import json
url = 'https://<name-of-your-heroku-app>.herokuapp.com/'
data = {"Pclass":3, "Age":2, "SibSp":1, "Fare":50}
response = requests.post(url, json.dumps(data))
print(response.json())
```

# Inspiration
## Article

 - **Article**: [Towards Data Science: Create an API to Deploy Machine Learning Models using Flask](https://towardsdatascience.com/create-an-api-to-deploy-machine-learning-models-using-flask-and-heroku-67a011800c50)
 - From [Elizabeth Ter Sahakyan](https://towardsdatascience.com/@liztersahakyan)

