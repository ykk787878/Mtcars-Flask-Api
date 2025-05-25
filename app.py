# app.py
from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

model = joblib.load("model/model.pkl")

@app.route("/")
def index():
    return "Welcome to the MTCars MPG Prediction API!"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        df = pd.DataFrame([data])
        prediction = model.predict(df)[0]
        return jsonify({"mpg_prediction": round(prediction, 2)})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8080))  
    app.run(debug=True, host="0.0.0.0", port=port)
