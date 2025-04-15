# Flask Backend Application Explanation

## Components and Structure

### 1. Flask Application Setup

```python
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": ["https://the-feds-project-3.netlify.app", "http://localhost:8080"]}}, supports_credentials=True)
```

This section initializes the Flask application and configures Cross-Origin Resource Sharing (CORS) to allow requests from the frontend application, whether deployed or running locally.

### 2. Simple API Endpoint

```python
@app.route('/api/hello', methods=['GET'])
def hello_world():
    """
    Simple API endpoint that returns a Hello World message
    """
    return jsonify({"message": "Hello World"})
```

A basic endpoint that serves as a health check and example. It returns a simple JSON response with a "Hello World" message.

### 3. Python File Upload Endpoint

```python
@app.route('/api/python-file', methods=['POST'])
def process_python_file():
    """
    API endpoint that accepts a Python file upload and returns its contents
    """
    # File validation and processing logic
    return jsonify({
        "filename": file.filename,
        "content": file_content
    })
```

This endpoint accepts a Python file upload, validates it (ensuring it's a .py file), and returns the file's contents as a string. It's a simpler version of the file parser endpoint, primarily used for displaying raw file content.

### 4. File Parser Endpoint

```python
@app.route('/api/file-parser', methods=['POST'])
def analyze_python_file():
    """
    API endpoint that accepts a Python file and returns AST parsing results
    """
    # File validation and processing
    
    # Parse the Python code using our parser module
    parsing_result = parse_python_code(file_content)
    
    # Identify variables and their scopes
    scope_result = identify_scopes(file_content)

    # Naming Convention Audit
    naming_result = check_naming_conventions(scope_result)
    
    return jsonify({
        "filename": file.filename,
        "parsing_result": parsing_result,
        "scope_result": scope_result,
        "naming_result": naming_result
    })
```

This is the main analysis endpoint that:
1. Accepts a Python file upload
2. Validates the file (ensuring it's a .py file)
3. Reads the file contents
4. Processes the file through three analysis modules:
   - `parse_python_code`: Parses the Python code into an Abstract Syntax Tree (AST)
   - `identify_scopes`: Identifies variables and their scopes
   - `check_naming_conventions`: Checks variable names against PEP 8 naming conventions
5. Returns a comprehensive JSON response with all analysis results

### 5. Server Startup

```python
if __name__ == '__main__':
    app.run(debug=True, port=5000)
```

This section starts the Flask development server on port 5000 when the script is run directly. The debug mode is enabled for development purposes.

## Integration with Analysis Modules

The application integrates with three key analysis modules:

1. **Parser Module** (`parser.py`):
   - Parses Python code into an Abstract Syntax Tree (AST)
   - Provides a structured representation of the code's syntax
   - Enables deeper analysis of code structure

2. **Scope Identifier Module** (`scopeIdentifier.py`):
   - Identifies variables and their scopes (global or local)
   - Detects global variables declared inside functions
   - Provides line numbers for variable declarations

3. **Naming Conventions Module** (`namingConventions.py`):
   - Checks variable names against PEP 8 naming conventions
   - Identifies naming violations and provides suggestions for fixes
   - Categorizes variables by scope and naming convention status

## API Response Structure

The main file parser endpoint returns a JSON response with the following structure:

```json
{
  "filename": "example.py",
  "parsing_result": {
    "success": true,
    "ast_dump": "...",
    "ast_structure": { ... }
  },
  "scope_result": {
    "success": true,
    "variables": [ ... ]
  },
  "naming_result": {
    "success": true,
    "variables": [
      {
        "variable": "example_var",
        "scope": "Global",
        "line": 5,
        "issue": "Naming OK",
        "status": "success"
      },
      ...
    ]
  }
}
```

This comprehensive response provides all the information needed by the frontend to display detailed analysis results, including variable scopes, naming convention violations, and suggestions for improvements.

## Error Handling

The application includes robust error handling:

1. **File Validation**:
   - Checks if a file was provided in the request
   - Verifies that the file has a name
   - Ensures the file has a .py extension

2. **Processing Errors**:
   - Each analysis module includes its own error handling
   - Syntax errors in the Python code are caught and reported
   - Other exceptions during processing are caught and returned with appropriate error messages

This ensures that the API provides meaningful feedback even when processing invalid or problematic files.

## Security Considerations

The application implements several security measures:

1. **CORS Configuration**:
   - Restricts API access to specific origins
   - Prevents unauthorized cross-origin requests

2. **File Type Validation**:
   - Only accepts Python (.py) files
   - Reduces the risk of processing potentially harmful files

3. **Error Handling**:
   - Prevents detailed error information from leaking to clients
   - Returns controlled error messages

These measures help protect the application from common web vulnerabilities and ensure secure operation.
