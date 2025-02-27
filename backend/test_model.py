from flask import Flask, request, jsonify
import joblib
import numpy as np

# Load the saved model
try:
    model = joblib.load('xgboost_model_v1.pkl')
    print("Model loaded successfully.")
except FileNotFoundError:
    print("Error: Model file 'xgboost_model_v1.pkl' not found. Ensure the file exists in the same directory.")
    exit()

# Test input features
# Replace these values with sample inputs
test_features = [20, 1.5, 45, 3, 1]  # Example: [diameter, thickness, angle, distance, mandrel]

# Ensure the input matches the expected format
try:
    test_features = np.array(test_features, dtype=float).reshape(1, -1)  # Reshape for prediction
except ValueError as e:
    print(f"Error in input formatting: {e}")
    exit()

# Predict
try:
    prediction = model.predict(test_features)
    print(f"Prediction for input {test_features.tolist()}: {int(prediction[0])}")
except Exception as e:
    print(f"Error during prediction: {e}")
