from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/collect', methods=['POST'])
def collect():
    """
    API endpoint to collect input data and display it in the terminal.
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

        # Log individual features
        print("Received Features:")
        for i, feature in enumerate(features):
            print(f"  Feature {i + 1}: {feature}")

        # Send a success response
        return jsonify({'message': 'Data received successfully', 'features': features}), 200

    except Exception as e:
        # Log and return any errors
        error_msg = f"An error occurred: {str(e)}"
        print(error_msg)
        return jsonify({'error': error_msg}), 500


if __name__ == '__main__':
    app.run(debug=True)
