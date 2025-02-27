from flask import Flask, request, jsonify
import joblib
import numpy as np
import sys

app = Flask(__name__)

# Load the saved model
try:
    model = joblib.load('xgboost_model_v1.pkl')
    print("Model loaded successfully.")
except FileNotFoundError:
    print("Error: Model file 'xgboost_model_v1.pkl' not found. Ensure the file exists in the same directory.")
    model = None

@app.route('/predict', methods=['POST'])
def predict():
    """
    API endpoint to collect input data, process it, and return the model prediction.
    """
    try:
        # Get JSON data from the request
        data = request.get_json()
        print("POST request received.")
        print("Received data:", data)  # Log received data

        # Validate the input
        if not data or 'features' not in data:
            error_msg = 'Invalid input: Missing "features" key in the request.'
            print(error_msg)
            return jsonify({'error': error_msg}), 400

        features = data['features']

        # Ensure features is a list and contains valid values
        if not isinstance(features, list):
            error_msg = '"features" must be a list of numeric values.'
            print(error_msg)
            return jsonify({'error': error_msg}), 400

        # Validate feature length
        expected_length = model.n_features_in_ if model else None
        if model and len(features) != expected_length:
            error_msg = f'Expected {expected_length} features, got {len(features)}.'
            print(error_msg)
            return jsonify({'error': error_msg}), 400

        # Convert features to NumPy array
        try:
            test_features = np.array(features, dtype=float).reshape(1, -1)
            print("Processed features for prediction:", test_features)  # Log processed features
        except ValueError as e:
            error_msg = f'Error converting features to numeric array: {str(e)}'
            print(error_msg)
            return jsonify({'error': error_msg}), 400

        # Make prediction
        prediction = model.predict(test_features)
        prediction_value = float(prediction[0])  # Convert to float for better precision
        print(f"Prediction: {prediction_value}")  # Log prediction

        # Send the prediction result to the frontend
        return jsonify({'prediction': prediction_value})

    except Exception as e:
        # Log and return any errors
        error_msg = f"An error occurred: {str(e)}"
        print(error_msg)
        return jsonify({'error': error_msg}), 500


if __name__ == '__main__':
    if model is None:
        print("Flask app cannot start because the model is not loaded.")
        sys.exit(1)  # Stop execution if model is not loaded
    else:
        app.run(debug=True)
