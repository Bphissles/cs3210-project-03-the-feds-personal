from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
# Enable CORS for all routes
CORS(app)

@app.route('/api/hello', methods=['GET'])
def hello_world():
    """
    Simple API endpoint that returns a Hello World message
    """
    return jsonify({"message": "Hello World"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
