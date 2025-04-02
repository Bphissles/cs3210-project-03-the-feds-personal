from flask import Flask, jsonify, request
from flask_cors import CORS
from parser import parse_python_code

app = Flask(__name__)
# Enable CORS for all routes with specific configuration
CORS(app, resources={r"/*": {"origins": ["https://the-feds-project-3.netlify.app", "http://localhost:8080"]}}, supports_credentials=True)

@app.route('/api/hello', methods=['GET'])
def hello_world():
    """
    Simple API endpoint that returns a Hello World message
    """
    return jsonify({"message": "Hello World"})

@app.route('/api/python-file', methods=['POST'])
def process_python_file():
    """
    API endpoint that accepts a Python file upload and returns its contents
    
    Expects a file with key 'file' in the form data
    Returns the file contents as a string
    """
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
        
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400
        
    if not file.filename.endswith('.py'):
        return jsonify({"error": "File must be a Python (.py) file"}), 400
    
    # Read the file contents
    file_content = file.read().decode('utf-8')
    
    return jsonify({
        "filename": file.filename,
        "content": file_content
    })

@app.route('/api/file-parser', methods=['POST'])
def analyze_python_file():
    """
    API endpoint that accepts a Python file and returns AST parsing results
    
    Expects a file with key 'file' in the form data
    Returns parsed AST data from the file for further analysis
    """
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
        
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400
        
    if not file.filename.endswith('.py'):
        return jsonify({"error": "File must be a Python (.py) file"}), 400
    
    # Read the file contents
    file_content = file.read().decode('utf-8')
    
    # Parse the Python code using our parser module
    parsing_result = parse_python_code(file_content)
    """
    New PY files can be placed here, and consume parsing_result
    or we can call them directly in the parser. Best practice is to
    call them here though. #separation-of-concerns
    """
    
    return jsonify({
        "filename": file.filename,
        "parsing_result": parsing_result
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
