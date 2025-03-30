# Project Outline: Python Variable Format and Scope Checker

## Project Overview

This project implements a Python static analysis tool that reads Python scripts and verifies whether variables follow correct naming conventions while identifying their scope (global or local).

## Architecture

### Frontend (Vue 3 + Bootstrap 5.3)
- **Technology Stack**: Vue 3, Bootstrap 5.3, SASS, Axios
- **Key Components**:
  - File upload interface for Python files
  - Code preview with syntax highlighting
  - Analysis results display
  - Responsive design for presentation screens

### Backend (Python Flask)
- **Technology Stack**: Python, Flask, AST module
- **Key Components**:
  - RESTful API endpoints
  - Python code parsing using AST
  - Variable scope identification
  - Naming convention enforcement

### Deployment
- **Frontend**: Deployed on Netlify
- **Backend**: Deployed on Render

## Core Functionality

### 1. Python Code Parsing
- Uses Python's built-in Abstract Syntax Tree (AST) module to analyze scripts
- Extracts variable assignments, function parameters, and global declarations
- Provides a clean JSON response with parsed information

### 2. Variable Scope Identification
- Classifies each variable as local (function scope) or global (script-wide scope)
- Detects global variables declared inside functions using the `global` keyword
- Maps variables to their respective scopes and locations in the code

### 3. Naming Convention Enforcement
- Ensures variable names follow PEP 8 guidelines:
  - Variable names: lowercase with underscores (snake_case)
  - Constants: UPPERCASE_WITH_UNDERSCORES
  - Class names: PascalCase
  - Function names: lowercase with underscores (snake_case)
- Flags variable names that violate these conventions

### 4. Error Reporting & Output
- Generates a structured report listing:
  - All variables, their name, scope (global/local), and line number
  - Naming convention violations with suggested corrections
- Displays results in a user-friendly format in the web interface

## User Interface

### Home Page
- Project introduction and overview
- Links to key features and resources
- Navigation to analysis tools

### Python File Analyzer
- File upload component with drag-and-drop support
- Validation for Python (.py) files only
- Code preview with syntax highlighting
- Analysis results display

### API Integration
- Backend connection demonstration
- API endpoint details
- Response visualization

## Development Workflow

### 1. Setup and Configuration
- Initialize Vue 3 frontend with Vite
- Set up Flask backend with necessary dependencies
- Configure cross-origin resource sharing (CORS)
- Establish API communication between frontend and backend

### 2. Frontend Development
- Create responsive UI components
- Implement file upload functionality
- Design code preview with syntax highlighting
- Build results display interface

### 3. Backend Development
- Implement AST parsing for Python files
- Create variable scope identification logic
- Build naming convention validation
- Develop RESTful API endpoints

### 4. Deployment
- Deploy frontend to Netlify
- Deploy backend to Render
- Configure environment variables for production

## Example Analysis

### Sample Python Code:
```python
MAX_COUNT = 100  # Global constant

def my_function():
    x = 5  # Local variable
    global_var = 10  # Incorrect global declaration (not using 'global')

def another_function():
    global MAX_COUNT  # Using global variable
    tempVar = 20  # Incorrect naming (CamelCase instead of snake_case)
```

### Expected Analysis Output:
```
Variable Name Analysis:
------------------------------------------------------
Variable        | Scope   | Line  | Issue
------------------------------------------------------
MAX_COUNT       | Global  | 1     | Should be UPPERCASE (Correct)
x               | Local   | 4     | Naming OK
global_var      | Local   | 5     | Warning: Global-like name but not declared global
MAX_COUNT       | Global  | 8     | Correct global usage
tempVar         | Local   | 9     | Naming Violation: Use snake_case (suggestion: temp_var)
------------------------------------------------------
```

## Future Enhancements

1. Support for analyzing entire Python projects (multiple files)
2. More detailed code quality metrics
3. Integration with popular code editors as a plugin
4. Support for additional programming languages
5. Export functionality for analysis results (JSON, CSV, PDF)
