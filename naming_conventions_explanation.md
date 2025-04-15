# Python Naming Conventions Checker Explanation

## Overview

The Python Naming Conventions Checker in `namingConventions.py` is designed to analyze variable names from the scope identifier results and check if they follow PEP 8 naming conventions. It flags variables that violate these conventions, provides information about the expected convention, and offers suggestions for correcting the naming issues.

## Components of the Naming Conventions Checker

### 1. NamingConventionType Class

```python
class NamingConventionType:
    """Constants for different naming convention types"""
    LOWERCASE_WITH_UNDERSCORES = 'lowercase_with_underscores'  # For variables and functions
    UPPERCASE_WITH_UNDERSCORES = 'UPPERCASE_WITH_UNDERSCORES'  # For constants
    PASCAL_CASE = 'PascalCase'  # For classes
```

This class defines constants for the different naming convention types that are enforced by the module.

### 2. NamingConventionViolation Class

```python
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
```

This class defines constants for the different naming convention types that are enforced by the module.

### 3. Helper Functions

The module includes several helper functions to check if a name follows a specific convention and to convert between different naming conventions:

#### Convention Checking Functions
- **`is_lowercase_with_underscores(name)`**: Checks if a name follows the lowercase_with_underscores convention (e.g., `valid_variable_name`)
- **`is_uppercase_with_underscores(name)`**: Checks if a name follows the UPPERCASE_WITH_UNDERSCORES convention (e.g., `MAX_VALUE`)
- **`is_pascal_case(name)`**: Checks if a name follows the PascalCase convention (e.g., `MyClass`)
- **`is_likely_constant(name)`**: Determines if a name is likely a constant based on its naming
- **`is_likely_class(name)`**: Determines if a name is likely a class based on its naming

#### Convention Conversion Functions
- **`to_lowercase_with_underscores(name)`**: Converts a name to snake_case (e.g., `validVariableName` → `valid_variable_name`)
- **`to_uppercase_with_underscores(name)`**: Converts a name to UPPERCASE_WITH_UNDERSCORES (e.g., `maxValue` → `MAX_VALUE`)
- **`to_pascal_case(name)`**: Converts a name to PascalCase (e.g., `max_value` → `MaxValue`)

### 4. check_naming_conventions Function

```python
def check_naming_conventions(scope_result: Dict[str, Any]) -> Dict[str, Any]:
    """
    Check if variable names follow PEP 8 naming conventions.
    """
```

This is the main function that:
1. Takes the result from the scope identifier
2. Checks each variable name against the appropriate naming convention
3. Generates a comprehensive report for each variable including:
   - Variable name
   - Scope (Global or Local)
   - Line number
   - Issue description (with suggestions for fixing violations)
   - Status (success, warning, or error)
4. Returns a structured result with all variables and their analysis

## How It Works

1. The function receives the scope_result from the scope identifier
2. It iterates through each variable in the scope_result
3. For each variable, it determines the appropriate naming convention based on the variable's characteristics:
   - Class names should follow PascalCase
   - Constants should follow UPPERCASE_WITH_UNDERSCORES
   - Variables and functions should follow lowercase_with_underscores
4. If a variable name doesn't follow the appropriate convention, it's added to the violations list
5. The function returns a dictionary with the list of violations

## Example Output

For a Python code snippet with naming convention violations:

```python
class myClass:  # Should be MyClass (PascalCase)
    max_value = 100  # Should be MAX_VALUE (UPPERCASE_WITH_UNDERSCORES) if it's a constant
    
    def ProcessData(self):  # Should be process_data (lowercase_with_underscores)
        localVar = 42  # Should be local_var (lowercase_with_underscores)
```

The naming conventions checker would produce:

```json
{
  "success": true,
  "variables": [
    {
      "variable": "myClass",
      "scope": "Global",
      "line": 1,
      "issue": "Naming Violation: Use PascalCase (suggestion: MyClass)",
      "status": "error"
    },
    {
      "variable": "max_value",
      "scope": "Global",
      "line": 2,
      "issue": "Naming Violation: Use UPPERCASE_WITH_UNDERSCORES (suggestion: MAX_VALUE)",
      "status": "error"
    },
    {
      "variable": "ProcessData",
      "scope": "Global",
      "line": 4,
      "issue": "Naming Violation: Use snake_case (suggestion: process_data)",
      "status": "error"
    },
    {
      "variable": "localVar",
      "scope": "Local",
      "line": 5,
      "issue": "Naming Violation: Use snake_case (suggestion: local_var)",
      "status": "error"
    }
  ]
}
```

This output format is designed to be directly usable in the Report view of the application, which displays variables and their naming convention status in a table format.

## PEP 8 Naming Conventions

The module enforces the following PEP 8 naming conventions:

1. **Variable names** should be lowercase with underscores (e.g., `valid_variable_name`)
2. **Constants** should be in UPPERCASE with underscores (e.g., `MAX_VALUE`)
3. **Class names** should follow PascalCase (e.g., `MyClass`)
4. **Function names** should be lowercase with underscores (e.g., `process_data`)

These conventions help make Python code more readable and consistent across different projects.
