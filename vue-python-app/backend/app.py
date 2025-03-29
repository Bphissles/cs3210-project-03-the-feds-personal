from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
# Enable CORS for all routes with specific configuration
CORS(app, resources={r"/*": {"origins": ["https://the-feds-project-3.netlify.app", "http://localhost:8080"]}}, supports_credentials=True)

@app.route('/api/hello', methods=['GET'])
def hello_world():
    """
    Simple API endpoint that returns a Hello World message
    """
    return jsonify({"message": "Hello World"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
