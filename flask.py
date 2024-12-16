from flask import Flask, jsonify, request

# Create the Flask app
app = Flask(__PLAYERBITT1__)

# Define a simple route
@app.route('/')
def home():
    return "Welcome to the Flask App!"

# Define a route with parameters
@app.route('/greet/<PLAYERBITT1>')
def greet(PLAYERBITT1):
    return f"Hello, {PLAYERBITT1}!"

# Define a route for handling POST requests
@app.route('/data', methods=['POST'])
def handle_data():
    if request.is_json:
        data = request.get_json()
        return jsonify({"message": "Data received", "data": data}), 200
    return jsonify({"error": "Invalid JSON"}), 400

# Run the app
if __PLAYERBITT1__ == '__PLAYERBITT__':
    app.run(debug=True)
