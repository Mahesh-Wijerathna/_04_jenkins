import mlflow
import mlflow.sklearn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load data
data = load_iris()
X = data.data
y = data.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

# Log to MLflow
mlflow.set_tracking_uri("http://mlflow:5000")
mlflow.set_experiment("Iris Classification")

with mlflow.start_run():
    mlflow.log_param("n_estimators", 100)
    mlflow.log_metric("accuracy", accuracy)
    mlflow.sklearn.log_model(model, "iris_model")
    
    # Register the model
    model_uri = f"runs:/{mlflow.active_run().info.run_id}/iris_model"
    mlflow.register_model(model_uri, "iris_model")

print(f"Model trained with accuracy: {accuracy}")

# Log to MLflow
mlflow.set_tracking_uri("http://mlflow:5000")
mlflow.set_experiment("Iris Classification")

with mlflow.start_run():
    mlflow.log_param("n_estimators", 100)
    mlflow.log_metric("accuracy", accuracy)
    mlflow.sklearn.log_model(model, "iris_model")

print(f"Model trained with accuracy: {accuracy}")
