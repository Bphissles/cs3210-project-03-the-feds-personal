"""
Scope Identifier Module

This module analyzes Python code to identify variables and their scopes.
It classifies variables as either local (function scope) or global (script-wide scope).
"""

import ast
from typing import Dict, List, Any

class ScopeType:
    """Constants for different scope types"""
    GLOBAL = 'global'
    LOCAL = 'local'

class ScopeVisitor(ast.NodeVisitor):
    """
    AST visitor that identifies variables and their scopes in Python code.
    
    This visitor classifies variables as either local (function scope) or 
    global (script-wide scope), and detects global variables declared inside 
    functions using the global keyword.
    """
    
    def __init__(self):
        # Dictionary to store variable information: {name: {'scope': scope_type, 'line': line_number}}
        self.variables = {}
        
        # Track if we're currently in a function
        self.in_function = False
        
        # Track global declarations inside functions
        self.global_declarations = set()
    
    def visit_FunctionDef(self, node):
        """Visit a function definition"""
        # Add function name as a global variable
        self.variables[node.name] = {
            'name': node.name,
            'scope': ScopeType.GLOBAL,
            'line': node.lineno
        }
        
        # Set flag that we're entering a function
        old_in_function = self.in_function
        self.in_function = True
        
        # Visit function body
        for stmt in node.body:
            self.visit(stmt)
            
        # Add function parameters as local variables
        for arg in node.args.args:
            if arg.arg not in self.global_declarations:
                self.variables[arg.arg] = {
                    'name': arg.arg,
                    'scope': ScopeType.LOCAL,
                    'line': getattr(arg, 'lineno', node.lineno)
                }
        
        # Restore previous function state
        self.in_function = old_in_function
    
    def visit_Assign(self, node):
        """Visit an assignment"""
        # Process targets (variables being assigned to)
        for target in node.targets:
            if isinstance(target, ast.Name):
                # Simple assignment to a variable
                name = target.id
                
                # Skip if already processed as global declaration
                if self.in_function and name in self.global_declarations:
                    if name not in self.variables:
                        self.variables[name] = {
                            'name': name,
                            'scope': ScopeType.GLOBAL,
                            'line': target.lineno
                        }
                elif name not in self.variables:
                    # Determine scope based on context
                    scope = ScopeType.LOCAL if self.in_function else ScopeType.GLOBAL
                    self.variables[name] = {
                        'name': name,
                        'scope': scope,
                        'line': target.lineno
                    }
            
            # Handle tuple unpacking assignments
            elif isinstance(target, ast.Tuple) or isinstance(target, ast.List):
                for elt in target.elts:
                    if isinstance(elt, ast.Name):
                        name = elt.id
                        if self.in_function and name in self.global_declarations:
                            if name not in self.variables:
                                self.variables[name] = {
                                    'name': name,
                                    'scope': ScopeType.GLOBAL,
                                    'line': elt.lineno
                                }
                        elif name not in self.variables:
                            scope = ScopeType.LOCAL if self.in_function else ScopeType.GLOBAL
                            self.variables[name] = {
                                'name': name,
                                'scope': scope,
                                'line': elt.lineno
                            }
        
        # Visit the value expression
        self.visit(node.value)
    
    def visit_Global(self, node):
        """Visit a global statement"""
        # Record global declarations
        for name in node.names:
            self.global_declarations.add(name)
            self.variables[name] = {
                'name': name,
                'scope': ScopeType.GLOBAL,
                'line': node.lineno
            }

def identify_scopes(code: str) -> Dict[str, Any]:
    """
    Identify variables and their scopes in Python code.
    
    Args:
        code (str): Python code to analyze
        
    Returns:
        Dict[str, Any]: Dictionary containing variable scope information:
            - success: Boolean indicating if analysis was successful
            - variables: List of dictionaries with variable name, scope, and line number
            - error: Error message if analysis failed
    """
    try:
        # Parse the code into an AST
        tree = ast.parse(code)
        
        # Visit the AST to identify variables and scopes
        visitor = ScopeVisitor()
        visitor.visit(tree)
        
        # Convert variables dictionary to a list for the response
        variables_list = list(visitor.variables.values())
        
        return {
            'success': True,
            'variables': variables_list
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
            'error': f"Error analyzing code: {str(e)}"
        }