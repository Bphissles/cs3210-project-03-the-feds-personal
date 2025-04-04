"""
Python AST Parser Module

This module uses Python's Abstract Syntax Tree (AST) to parse Python files
and return the AST data structure for further analysis.
"""

import ast
from typing import Dict, Any

class ASTNodeVisitor(ast.NodeVisitor):
    """
    Custom AST node visitor to convert the AST into a structured dictionary.
    This allows for easier processing by other functions.
    """
    
    def __init__(self):
        self.result = {}
        
    def generic_visit(self, node):
        """
        Visit a node and convert it to a dictionary representation.
        
        Args:
            node: The AST node to visit
            
        Returns:
            Dict: A dictionary representation of the node
        """
        node_type = type(node).__name__
        node_dict = {
            'type': node_type,
            'lineno': getattr(node, 'lineno', None),
            'col_offset': getattr(node, 'col_offset', None),
            'end_lineno': getattr(node, 'end_lineno', None),
            'end_col_offset': getattr(node, 'end_col_offset', None),
        }
        
        # Process child nodes
        for field, value in ast.iter_fields(node):
            if isinstance(value, list):
                # Handle lists of nodes (like body)
                node_dict[field] = []
                for item in value:
                    if isinstance(item, ast.AST):
                        # Recursively visit child nodes
                        child_visitor = ASTNodeVisitor()
                        child_visitor.visit(item)
                        node_dict[field].append(child_visitor.result)
                    else:
                        node_dict[field].append(item)
            elif isinstance(value, ast.AST):
                # Recursively visit child nodes
                child_visitor = ASTNodeVisitor()
                child_visitor.visit(value)
                node_dict[field] = child_visitor.result
            else:
                # Handle primitive values
                node_dict[field] = value
                
        self.result = node_dict
        
    def visit(self, node):
        """
        Visit a node and store its dictionary representation.
        
        Args:
            node: The AST node to visit
        """
        self.generic_visit(node)
        return self.result

def extract_ast_structure(tree: ast.AST) -> Dict[str, Any]:
    """
    Extract a structured representation of the AST.
    
    Args:
        tree (ast.AST): The AST to extract structure from
        
    Returns:
        Dict[str, Any]: A structured dictionary representation of the AST
    """
    visitor = ASTNodeVisitor()
    return visitor.visit(tree)

def parse_python_code(code: str) -> Dict[str, Any]:
    """
    Parse Python code using AST and return both the raw AST dump and a structured breakdown.
    
    Args:
        code (str): Python code to parse
        
    Returns:
        Dict[str, Any]: Dictionary containing the parsed AST data including:
            - success: Boolean indicating if parsing was successful
            - ast_dump: Raw string representation of the AST (for debugging)
            - ast_structure: Structured dictionary representation of the AST
            - error: Error message if parsing failed
    """
    try:
        # Parse the code into an AST
        tree = ast.parse(code)
        
        # Convert the AST to a string representation (for debugging)
        ast_dump = ast.dump(tree)
        
        # Extract a structured representation of the AST
        ast_structure = extract_ast_structure(tree)
        
        return {
            'success': True,
            'ast_dump': ast_dump,
            'ast_structure': ast_structure
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