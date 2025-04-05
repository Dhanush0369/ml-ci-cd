from flask import Flask, request, jsonify
import joblib
import os

app = Flask(__name__)
model_version = os.getenv("MODEL_VERSION")
if model_version is None:
    raise ValueError("MODEL_VERSION environment variable not set!")

model = joblib.load(f'models/{model_version}/iris_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json['features']
    prediction = model.predict([data]).tolist()
    return jsonify({
        "prediction": prediction[0],
        "model_version": model_version
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
