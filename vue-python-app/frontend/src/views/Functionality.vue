<script setup></script>
<template>
  <div class="container py-5">
    <h1 class="text-center mb-5">Core Functionality</h1>
    
    <div class="row g-4">
      <!-- Python Code Parsing -->
      <div class="col-md-6">
        <div class="card h-100 border-0 shadow-sm functionality-card">
          <div class="card-body p-4">
            <div class="d-flex align-items-center mb-3">
              <div class="feature-icon-wrapper me-3 bg-primary bg-opacity-10">
                <i class="bi bi-code-square fs-3 text-primary"></i>
              </div>
              <h2 class="feature-heading mb-0">Python Code Parsing</h2>
            </div>
            <p class="feature-description">
              Our application leverages Python's built-in Abstract Syntax Tree (AST) module to analyze Python scripts with precision and depth.
            </p>
            <ul class="list-group list-group-flush mb-3">
              <li class="list-group-item bg-transparent ps-0">
                <i class="bi bi-check-circle-fill me-2 text-success"></i>
                <strong>AST Analysis:</strong> Parses Python code into structured syntax trees
              </li>
              <li class="list-group-item bg-transparent ps-0">
                <i class="bi bi-check-circle-fill me-2 text-success"></i>
                <strong>Variable Extraction:</strong> Identifies all variable assignments and declarations
              </li>
              <li class="list-group-item bg-transparent ps-0">
                <i class="bi bi-check-circle-fill me-2 text-success"></i>
                <strong>Function Detection:</strong> Captures function parameters and their default values
              </li>
              <li class="list-group-item bg-transparent ps-0">
                <i class="bi bi-check-circle-fill me-2 text-success"></i>
                <strong>JSON Response:</strong> Returns structured data for frontend visualization
              </li>
            </ul>
          </div>
        </div>
      </div>
      
      <!-- Variable Scope Identification -->
      <div class="col-md-6">
        <div class="card h-100 border-0 shadow-sm functionality-card">
          <div class="card-body p-4">
            <div class="d-flex align-items-center mb-3">
              <div class="feature-icon-wrapper me-3 bg-info bg-opacity-10">
                <i class="bi bi-layers fs-3 text-info"></i>
              </div>
              <h2 class="feature-heading mb-0">Scope Identification</h2>
            </div>
            <p class="feature-description">
              Our intelligent scope analyzer precisely identifies and classifies variable scopes throughout your Python code.
            </p>
            <ul class="list-group list-group-flush mb-3">
              <li class="list-group-item bg-transparent ps-0">
                <i class="bi bi-check-circle-fill me-2 text-success"></i>
                <strong>Scope Classification:</strong> Distinguishes between global and local variables
              </li>
              <li class="list-group-item bg-transparent ps-0">
                <i class="bi bi-check-circle-fill me-2 text-success"></i>
                <strong>Global Detection:</strong> Identifies variables declared with the <code>global</code> keyword
              </li>
              <li class="list-group-item bg-transparent ps-0">
                <i class="bi bi-check-circle-fill me-2 text-success"></i>
                <strong>Scope Mapping:</strong> Links variables to their respective scopes in the code
              </li>
              <li class="list-group-item bg-transparent ps-0">
                <i class="bi bi-check-circle-fill me-2 text-success"></i>
                <strong>Location Tracking:</strong> Records line numbers for each variable reference
              </li>
            </ul>
          </div>
        </div>
      </div>
      
      <!-- Naming Convention Enforcement -->
      <div class="col-md-6">
        <div class="card h-100 border-0 shadow-sm functionality-card">
          <div class="card-body p-4">
            <div class="d-flex align-items-center mb-3">
              <div class="feature-icon-wrapper me-3 bg-warning bg-opacity-10">
                <i class="bi bi-check2-square fs-3 text-warning"></i>
              </div>
              <h2 class="feature-heading mb-0">Naming Conventions</h2>
            </div>
            <p class="feature-description">
              Our application enforces PEP 8 naming conventions, ensuring your Python code follows industry best practices.
            </p>
            <ul class="list-group list-group-flush mb-3">
              <li class="list-group-item bg-transparent ps-0">
                <i class="bi bi-check-circle-fill me-2 text-success"></i>
                <strong>PEP 8 Compliance:</strong> Validates variable names against Python standards
              </li>
              <li class="list-group-item bg-transparent ps-0">
                <i class="bi bi-check-circle-fill me-2 text-success"></i>
                <strong>Style Validation:</strong> Checks for proper snake_case in variables and functions
              </li>
              <li class="list-group-item bg-transparent ps-0">
                <i class="bi bi-check-circle-fill me-2 text-success"></i>
                <strong>Constant Detection:</strong> Verifies UPPERCASE naming for constants
              </li>
              <li class="list-group-item bg-transparent ps-0">
                <i class="bi bi-check-circle-fill me-2 text-success"></i>
                <strong>Class Naming:</strong> Ensures PascalCase for class definitions
              </li>
            </ul>
          </div>
        </div>
      </div>
      
      <!-- Error Reporting & Output -->
      <div class="col-md-6">
        <div class="card h-100 border-0 shadow-sm functionality-card">
          <div class="card-body p-4">
            <div class="d-flex align-items-center mb-3">
              <div class="feature-icon-wrapper me-3 bg-danger bg-opacity-10">
                <i class="bi bi-clipboard-data fs-3 text-danger"></i>
              </div>
              <h2 class="feature-heading mb-0">Results Dashboard</h2>
            </div>
            <p class="feature-description">
              Our intuitive dashboard presents analysis results in a clear, actionable format with detailed recommendations.
            </p>
            <ul class="list-group list-group-flush mb-3">
              <li class="list-group-item bg-transparent ps-0">
                <i class="bi bi-check-circle-fill me-2 text-success"></i>
                <strong>Structured Reports:</strong> Organized display of all variables and their properties
              </li>
              <li class="list-group-item bg-transparent ps-0">
                <i class="bi bi-check-circle-fill me-2 text-success"></i>
                <strong>Violation Flagging:</strong> Clear highlighting of naming convention issues
              </li>
              <li class="list-group-item bg-transparent ps-0">
                <i class="bi bi-check-circle-fill me-2 text-success"></i>
                <strong>Suggested Fixes:</strong> Automatic recommendations for correcting violations
              </li>
              <li class="list-group-item bg-transparent ps-0">
                <i class="bi bi-check-circle-fill me-2 text-success"></i>
                <strong>Interactive UI:</strong> User-friendly interface for reviewing results
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
