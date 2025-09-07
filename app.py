from flask import Flask, request, jsonify, render_template_string
import mlflow
import mlflow.sklearn
import numpy as np

app = Flask(__name__)

# Set MLflow tracking URI
mlflow.set_tracking_uri("http://mlflow:5000")
print(f"MLflow tracking URI set to: {mlflow.get_tracking_uri()}")

# Debug: List all registered models
try:
    models = mlflow.search_registered_models()
    print("Registered models:")
    for model in models:
        print(f"- Name: {model.name}, Latest Version: {model.latest_versions[0].version if model.latest_versions else 'None'}")
except Exception as e:
    print(f"Error listing models: {e}")

# Load the model (assuming it's logged as "iris_model")
try:
    model = mlflow.sklearn.load_model("models:/iris_model/latest")
    print("Model loaded successfully")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

@app.route('/')
def home():
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Iris Prediction</title>
    </head>
    <body>
        <h1>Iris Flower Prediction</h1>
        <form id="predictionForm">
            <label>Sepal Length:</label><input type="number" step="0.1" id="sepal_length" required><br>
            <label>Sepal Width:</label><input type="number" step="0.1" id="sepal_width" required><br>
            <label>Petal Length:</label><input type="number" step="0.1" id="petal_length" required><br>
            <label>Petal Width:</label><input type="number" step="0.1" id="petal_width" required><br>
            <button type="submit">Predict</button>
        </form>
        <div id="result"></div>
        <script>
            document.getElementById('predictionForm').addEventListener('submit', async function(e) {
                e.preventDefault();
                const data = {
                    sepal_length: parseFloat(document.getElementById('sepal_length').value),
                    sepal_width: parseFloat(document.getElementById('sepal_width').value),
                    petal_length: parseFloat(document.getElementById('petal_length').value),
                    petal_width: parseFloat(document.getElementById('petal_width').value)
                };
                const response = await fetch('/predict', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify(data)
                });
                const result = await response.json();
                document.getElementById('result').innerHTML = '<h2>Prediction: ' + result.prediction + '</h2>';
            });
        </script>
    </body>
    </html>
    """
    return render_template_string(html)

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({'error': 'Model not loaded'}), 500
    data = request.json
    features = np.array([[data['sepal_length'], data['sepal_width'], data['petal_length'], data['petal_width']]])
    prediction = model.predict(features)[0]
    species = ['setosa', 'versicolor', 'virginica'][prediction]
    return jsonify({'prediction': species})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)