<script setup></script>
<template>
  <div class="container py-5">
    <h1 class="text-center mb-5">User Interface</h1>
    
    <div class="row g-4">
      <!-- Home Page -->
      <div class="col-md-4">
        <div class="card h-100 border-0 shadow-sm ui-card">
          <div class="card-body p-4">
            <div class="d-flex align-items-center mb-3">
              <div class="ui-icon-wrapper me-3 bg-primary bg-opacity-10">
                <i class="bi bi-house-door fs-3 text-primary"></i>
              </div>
              <h2 class="ui-heading mb-0">Home Page</h2>
            </div>
            <p class="ui-description">
              The welcoming entry point to our application, providing an overview and easy navigation.
            </p>
            <ul class="list-group list-group-flush mb-3">
              <li class="list-group-item bg-transparent ps-0">
                <i class="bi bi-info-circle me-2 text-primary"></i>
                <strong>Project Introduction</strong> with clear overview
              </li>
              <li class="list-group-item bg-transparent ps-0">
                <i class="bi bi-link-45deg me-2 text-primary"></i>
                <strong>Feature Links</strong> to key application areas
              </li>
              <li class="list-group-item bg-transparent ps-0">
                <i class="bi bi-signpost-split me-2 text-primary"></i>
                <strong>Navigation Menu</strong> for intuitive access
              </li>
            </ul>
          </div>
        </div>
      </div>
      
      <!-- Python File Analyzer -->
      <div class="col-md-4">
        <div class="card h-100 border-0 shadow-sm ui-card">
          <div class="card-body p-4">
            <div class="d-flex align-items-center mb-3">
              <div class="ui-icon-wrapper me-3 bg-success bg-opacity-10">
                <i class="bi bi-file-earmark-code fs-3 text-success"></i>
              </div>
              <h2 class="ui-heading mb-0">File Analyzer</h2>
            </div>
            <p class="ui-description">
              The core analysis interface where users can upload and analyze Python code.
            </p>
            <ul class="list-group list-group-flush mb-3">
              <li class="list-group-item bg-transparent ps-0">
                <i class="bi bi-upload me-2 text-success"></i>
                <strong>Drag-and-Drop</strong> file upload component
              </li>
              <li class="list-group-item bg-transparent ps-0">
                <i class="bi bi-check-circle me-2 text-success"></i>
                <strong>File Validation</strong> for Python (.py) files
              </li>
              <li class="list-group-item bg-transparent ps-0">
                <i class="bi bi-code-slash me-2 text-success"></i>
                <strong>Code Preview</strong> with syntax highlighting
              </li>
              <li class="list-group-item bg-transparent ps-0">
                <i class="bi bi-clipboard-data me-2 text-success"></i>
                <strong>Results Display</strong> with detailed analysis
              </li>
            </ul>
          </div>
        </div>
      </div>
      
      <!-- API Integration -->
      <div class="col-md-4">
        <div class="card h-100 border-0 shadow-sm ui-card">
          <div class="card-body p-4">
            <div class="d-flex align-items-center mb-3">
              <div class="ui-icon-wrapper me-3 bg-info bg-opacity-10">
                <i class="bi bi-hdd-network fs-3 text-info"></i>
              </div>
              <h2 class="ui-heading mb-0">API Integration</h2>
            </div>
            <p class="ui-description">
              The connection between frontend and backend, showcasing the API architecture.
            </p>
            <ul class="list-group list-group-flush mb-3">
              <li class="list-group-item bg-transparent ps-0">
                <i class="bi bi-arrow-left-right me-2 text-info"></i>
                <strong>Backend Connection</strong> demonstration
              </li>
              <li class="list-group-item bg-transparent ps-0">
                <i class="bi bi-diagram-3 me-2 text-info"></i>
                <strong>API Endpoints</strong> with detailed documentation
              </li>
              <li class="list-group-item bg-transparent ps-0">
                <i class="bi bi-braces me-2 text-info"></i>
                <strong>JSON Responses</strong> with structured data
              </li>
              <li class="list-group-item bg-transparent ps-0">
                <i class="bi bi-graph-up me-2 text-info"></i>
                <strong>Response Visualization</strong> with interactive elements
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
    
  </div>
</template>