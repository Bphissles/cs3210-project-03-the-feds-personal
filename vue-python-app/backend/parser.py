"""
Python AST Parser Module

This module uses Python's Abstract Syntax Tree (AST) to parse Python files
and return the AST data structure for further analysis.
"""

import ast
from typing import Dict, Any


def parse_python_code(code: str) -> Dict[str, Any]:
    """
    Parse Python code using AST and return the parsed structure.
    
    Args:
        code (str): Python code to parse
        
    Returns:
        Dict[str, Any]: Dictionary containing the parsed AST data
    """
    try:
        # Parse the code into an AST
        tree = ast.parse(code)
        
        # Convert the AST to a string representation
        ast_dump = ast.dump(tree)
        
        return {
            'success': True,
            'parsed_data': ast_dump
        }
    except SyntaxError as e:
        return {
            'success': False,
            'error': f"Syntax error: {str(e)}",
            'line': e.lineno,
            'offset': e.offset
        }
    except Exception as e:
        return {
            'success': False,
            'error': f"Error parsing code: {str(e)}"
        }