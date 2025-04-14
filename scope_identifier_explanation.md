# Python Scope Identifier Explanation

## Overview

The Python Scope Identifier in `scopeIdentifier.py` is designed to analyze Python code and identify variables along with their scopes. It classifies variables as either local (function scope) or global (script-wide scope) and detects global variables declared inside functions using the `global` keyword.

## Components of the Scope Identifier

### 1. ScopeType Class

```python
class ScopeType:
    """Constants for different scope types"""
    GLOBAL = 'global'
    LOCAL = 'local'
```

This class defines constants for the different types of variable scopes that the module identifies.

### 2. ScopeVisitor Class

```python
class ScopeVisitor(ast.NodeVisitor):
    """
    AST visitor that identifies variables and their scopes in Python code.
    
    This visitor classifies variables as either local (function scope) or 
    global (script-wide scope), and detects global variables declared inside 
    functions using the global keyword.
    """
```

This class extends Python's built-in `ast.NodeVisitor` class to traverse an Abstract Syntax Tree (AST) and identify variable scopes. It tracks variables and their scopes as it visits different nodes in the AST.

#### Key Methods:

- **`__init__(self)`**: Initializes the visitor with:
  - A dictionary to store variable information
  - A flag to track if we're currently in a function
  - A set to track global declarations inside functions

- **`visit_FunctionDef(self, node)`**: Handles function definitions by:
  - Adding the function name as a global variable
  - Setting a flag that we're entering a function
  - Visiting the function body
  - Adding function parameters as local variables
  - Restoring the previous function state

- **`visit_Assign(self, node)`**: Processes variable assignments by:
  - Identifying variables being assigned to
  - Determining their scope based on context (local if in a function, global otherwise)
  - Handling tuple unpacking assignments
  - Respecting global declarations inside functions

- **`visit_Global(self, node)`**: Processes global statements by:
  - Recording global declarations
  - Marking variables as global in the current scope

### 3. identify_scopes Function

```python
def identify_scopes(code: str) -> Dict[str, Any]:
    """
    Identify variables and their scopes in Python code.
    """
```

This is the main function that:
1. Parses Python code into an AST
2. Creates a ScopeVisitor instance to traverse the AST
3. Collects variable scope information
4. Returns a structured result with variable names, scopes, and line numbers

## How It Works

1. The Python code is parsed into an Abstract Syntax Tree using Python's built-in `ast` module
2. The ScopeVisitor traverses the AST, visiting different types of nodes:
   - Function definitions
   - Variable assignments
   - Global statements
3. As it traverses, it builds a dictionary of variables with their scopes and line numbers
4. The final result is a list of dictionaries, each containing:
   - `name`: The variable name
   - `scope`: Either 'global' or 'local'
   - `line`: The line number where the variable is defined

## Example Output

For a simple Python code snippet:

```python
x = 10  # Global variable

def my_function(param):
    global y
    y = 20  # Global variable declared inside function
    z = 30  # Local variable
    return param + x + y + z
```

The scope identifier would produce:

```json
{
  "success": true,
  "variables": [
    {
      "name": "x",
      "scope": "global",
      "line": 1
    },
    {
      "name": "my_function",
      "scope": "global",
      "line": 3
    },
    {
      "name": "param",
      "scope": "local",
      "line": 3
    },
    {
      "name": "y",
      "scope": "global",
      "line": 5
    },
    {
      "name": "z",
      "scope": "local",
      "line": 6
    }
  ]
}
```

## Limitations

- The current implementation only handles global and local scopes, not nonlocal scopes or class scopes
- It doesn't track variable usage, only variable definitions
- It doesn't infer variable types
