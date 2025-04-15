"""
Naming Conventions Module

This module analyzes variable names from the scope identifier results
and checks if they follow PEP 8 naming conventions.
"""

import re
from typing import Dict, Any

class NamingConventionType:
    """Constants for different naming convention types"""
    LOWERCASE_WITH_UNDERSCORES = 'lowercase_with_underscores'  # For variables and functions
    UPPERCASE_WITH_UNDERSCORES = 'UPPERCASE_WITH_UNDERSCORES'  # For constants
    PASCAL_CASE = 'PascalCase'  # For classes

class NamingConventionViolation:
    """Class to represent a naming convention violation"""
    def __init__(self, name: str, expected_convention: str, line: int):
        self.name = name
        self.expected_convention = expected_convention
        self.line = line
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization"""
        return {
            'name': self.name,
            'expected_convention': self.expected_convention,
            'line': self.line
        }

def is_lowercase_with_underscores(name: str) -> bool:
    """Check if a name follows lowercase_with_underscores convention"""
    pattern = r'^[a-z][a-z0-9_]*$'
    return bool(re.match(pattern, name))

def is_uppercase_with_underscores(name: str) -> bool:
    """Check if a name follows UPPERCASE_WITH_UNDERSCORES convention"""
    pattern = r'^[A-Z][A-Z0-9_]*$'
    return bool(re.match(pattern, name))

def is_pascal_case(name: str) -> bool:
    """Check if a name follows PascalCase convention"""
    pattern = r'^[A-Z][a-zA-Z0-9]*$'
    return bool(re.match(pattern, name))

def is_likely_constant(name: str) -> bool:
    """Determine if a name is likely a constant based on naming"""
    return is_uppercase_with_underscores(name)

def is_likely_class(name: str) -> bool:
    """Determine if a name is likely a class based on naming"""
    return is_pascal_case(name)

def to_lowercase_with_underscores(name: str) -> str:
    """Convert a name to lowercase_with_underscores (snake_case)"""
    # Handle camelCase or PascalCase
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    s2 = re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
    # Replace any non-alphanumeric characters with underscores
    return re.sub(r'[^a-z0-9_]', '_', s2)

def to_uppercase_with_underscores(name: str) -> str:
    """Convert a name to UPPERCASE_WITH_UNDERSCORES"""
    return to_lowercase_with_underscores(name).upper()

def to_pascal_case(name: str) -> str:
    """Convert a name to PascalCase"""
    # First convert to snake_case
    snake_case = to_lowercase_with_underscores(name)
    # Then convert to PascalCase
    return ''.join(word.capitalize() for word in snake_case.split('_'))

def check_naming_conventions(scope_result: Dict[str, Any]) -> Dict[str, Any]:
    """
    Check if variable names follow PEP 8 naming conventions.
    
    Args:
        scope_result (Dict[str, Any]): Result from the scope identifier
        
    Returns:
        Dict[str, Any]: Dictionary containing naming convention results:
            - success: Boolean indicating if check was successful
            - variables: List of variables with scope, line, naming issue, and status
            - error: Error message if check failed
    """
    try:
        if not scope_result.get('success', False):
            return {
                'success': False,
                'error': 'Scope identification failed'
            }
        
        variables = scope_result.get('variables', [])
        result_variables = []
        
        for variable in variables:
            name = variable.get('name')
            line = variable.get('line')
            scope_type = variable.get('scope', '').capitalize()  # Convert 'global' to 'Global', etc.
            
            # Skip if name or line is missing
            if not name or not line:
                continue
            
            # Initialize variable data with default values
            var_data = {
                'variable': name,
                'scope': scope_type,
                'line': line,
                'issue': '',
                'status': ''
            }
            
            # Check if the name follows the appropriate convention
            if is_likely_class(name):
                # Class names should be PascalCase
                if not is_pascal_case(name):
                    var_data['issue'] = f"Naming Violation: Use PascalCase (suggestion: {to_pascal_case(name)})"
                    var_data['status'] = 'error'
                else:
                    var_data['issue'] = "Naming OK"
                    var_data['status'] = 'success'
            elif is_likely_constant(name):
                # Constants should be UPPERCASE_WITH_UNDERSCORES
                if not is_uppercase_with_underscores(name):
                    var_data['issue'] = f"Naming Violation: Use UPPERCASE_WITH_UNDERSCORES (suggestion: {to_uppercase_with_underscores(name)})"
                    var_data['status'] = 'error'
                else:
                    var_data['issue'] = "Naming OK"
                    var_data['status'] = 'success'
            else:
                # Variables and functions should be lowercase_with_underscores
                if not is_lowercase_with_underscores(name):
                    var_data['issue'] = f"Naming Violation: Use snake_case (suggestion: {to_lowercase_with_underscores(name)})"
                    var_data['status'] = 'error'
                else:
                    var_data['issue'] = "Naming OK"
                    var_data['status'] = 'success'
            
            # Check for global-like names in local scope
            if scope_type == 'Local' and name.startswith('global_'):
                var_data['issue'] = "Warning: Global-like name but not declared global"
                var_data['status'] = 'warning'
            
            # Add to result variables
            result_variables.append(var_data)
        
        return {
            'success': True,
            'variables': result_variables
        }
    except Exception as e:
        return {
            'success': False,
            'error': f"Error checking naming conventions: {str(e)}"
        }