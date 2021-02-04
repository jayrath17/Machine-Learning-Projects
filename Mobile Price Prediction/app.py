from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('random_forest_regression_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    #Fuel_Type_Diesel=0
    if request.method == 'POST':
        No_Year = int(request.form['No_Year'])
        RAM_GB=float(request.form['RAM_GB'])
        ROM_GB=int(request.form['ROM_GB'])
        
        No_Year=2020-No_Year
        
        prediction=model.predict([[No_Year,RAM_GB,ROM_GB]])
        output=round(prediction[0],2)
        if output<0:
            return render_template('index.html',prediction_texts="Specifications Are Invalid")
        else:
            return render_template('index.html',prediction_text="Price of your Mobile will be around: Rs{}".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

