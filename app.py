#import numpy as np
import pandas as pd
from flask import Flask, jsonify, request, render_template
import pickle

# Load pickled model
model = pickle.load(open('model.pkl','rb'))

# Name flask app
app = Flask(__name__)

# routes
## Create a route that receives JSON inputs, uses the trained model to make a prediction, and returns that prediction in a JSON format, which can be accessed through the API endpoint.
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    result = model.predict(final_features)
    output = round(result[0], 2)

    # get data
    #data = request.get_json(force=True)

    # convert data into dataframe
    #data.update((x, [y]) for x, y in data.items())
    ## you need to convert the JSON data that you get from the request to a data structure that the model can use to make a prediction.
    ## Here a pandas dataframe object
    #data_df = pd.DataFrame.from_dict(data)

    # predictions
    #result = model.predict(data_df)

    # send back to browser
    #output = {'results': int(result[0])}

    # return data
    #return jsonify(results=output)
    return render_template('index.html', prediction_text='Passenger survived (1 - Yes, 0 - No): {}'.format(output))

@app.route('/results',methods=['POST'])
def results():

    # get data
    data = request.get_json(force=True)
    result = model.predict([np.array(list(data.values()))])

    # return data
    #return jsonify(results=output)

    output = result[0]
    return jsonify(output)

if __name__ == '__main__':
    app.run(port = 7070, debug=True)

