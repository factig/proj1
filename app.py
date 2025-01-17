import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/') #index or landing page of website
def home():
    return render_template('index.html')
# 127.0.0.1:8080/predict
@app.route('/predict',methods=['POST']) #post method is used to send parameters in http request
def predict():
    '''
    For rendering results on HTML GUI'''
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    print("Features are ", final_features, " No of features =", len(final_features))
    prediction = model.predict(final_features)
    output = round(prediction[0], 2)
    # output =10
    return render_template('index.html', 
    	prediction_text='Predicted install {}'
        .format(output))

import random

if __name__ == '__main__':
    # Generate a random port number between 5000 and 9999
    random_port = random.randint(5000, 9999)
    app.run(host="0.0.0.0", port=random_port)
#if __name__ == "__main__":
 #   app.run(host="0.0.0.0",port=8501) # EC2 on AWS
    # app.run(host="127.0.0.1",port=9000) # local machine
