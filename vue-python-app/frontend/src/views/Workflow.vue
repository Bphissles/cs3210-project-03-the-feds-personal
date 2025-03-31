<script setup></script>
<template>
  <div class="container py-5">
    <h1 class="text-center mb-5">Development Workflow</h1>
    
    <div class="row g-4">
      <!-- Setup and Configuration -->
      <div class="col-md-6">
        <div class="card h-100 border-0 shadow-sm workflow-card">
          <div class="card-body p-4">
            <div class="d-flex align-items-center mb-3">
              <div class="workflow-icon-wrapper me-3 bg-primary bg-opacity-10">
                <i class="bi bi-gear fs-3 text-primary"></i>
              </div>
              <h2 class="workflow-heading mb-0">Setup and Configuration</h2>
            </div>
            <p class="workflow-description">
              Establishing the foundation for our application by setting up the development environment and configuring the necessary tools and frameworks.
            </p>
            <ul class="list-group list-group-flush mb-3">
              <li class="list-group-item bg-transparent ps-0">
                <i class="bi bi-check-circle-fill me-2 text-success"></i>
                <strong>Initialize Vue 3 frontend</strong> with Vite for fast development
              </li>
              <li class="list-group-item bg-transparent ps-0">
                <i class="bi bi-check-circle-fill me-2 text-success"></i>
                <strong>Set up Flask backend</strong> with necessary dependencies
              </li>
              <li class="list-group-item bg-transparent ps-0">
                <i class="bi bi-check-circle-fill me-2 text-success"></i>
                <strong>Configure CORS</strong> for cross-origin resource sharing
              </li>
              <li class="list-group-item bg-transparent ps-0">
                <i class="bi bi-check-circle-fill me-2 text-success"></i>
                <strong>Establish API communication</strong> between frontend and backend
              </li>
            </ul>
            <div class="tech-stack d-flex flex-wrap gap-2 mt-4">
              <span class="badge bg-light text-dark border">Vue 3</span>
              <span class="badge bg-light text-dark border">Vite</span>
              <span class="badge bg-light text-dark border">Flask</span>
              <span class="badge bg-light text-dark border">Python</span>
              <span class="badge bg-light text-dark border">CORS</span>
              <span class="badge bg-light text-dark border">REST API</span>
            </div>
          </div>
        </div>
      </div>
      
      <!-- Frontend Development -->
      <div class="col-md-6">
        <div class="card h-100 border-0 shadow-sm workflow-card">
          <div class="card-body p-4">
            <div class="d-flex align-items-center mb-3">
              <div class="workflow-icon-wrapper me-3 bg-info bg-opacity-10">
                <i class="bi bi-layout-text-window fs-3 text-info"></i>
              </div>
              <h2 class="workflow-heading mb-0">Frontend Development</h2>
            </div>
            <p class="workflow-description">
              Building the user interface components and implementing the client-side functionality for a seamless user experience.
            </p>
            <ul class="list-group list-group-flush mb-3">
              <li class="list-group-item bg-transparent ps-0">
                <i class="bi bi-check-circle-fill me-2 text-success"></i>
                <strong>Create responsive UI components</strong> for all device sizes
              </li>
              <li class="list-group-item bg-transparent ps-0">
                <i class="bi bi-check-circle-fill me-2 text-success"></i>
                <strong>Implement file upload functionality</strong> with drag-and-drop support
              </li>
              <li class="list-group-item bg-transparent ps-0">
                <i class="bi bi-check-circle-fill me-2 text-success"></i>
                <strong>Design code preview</strong> with syntax highlighting
              </li>
              <li class="list-group-item bg-transparent ps-0">
                <i class="bi bi-check-circle-fill me-2 text-success"></i>
                <strong>Build results display interface</strong> for analysis output
              </li>
            </ul>
            <div class="tech-stack d-flex flex-wrap gap-2 mt-4">
              <span class="badge bg-light text-dark border">Bootstrap 5</span>
              <span class="badge bg-light text-dark border">SASS</span>
              <span class="badge bg-light text-dark border">Vue Router</span>
              <span class="badge bg-light text-dark border">Axios</span>
              <span class="badge bg-light text-dark border">Prism.js</span>
            </div>
          </div>
        </div>
      </div>
      
      <!-- Backend Development -->
      <div class="col-md-6">
        <div class="card h-100 border-0 shadow-sm workflow-card">
          <div class="card-body p-4">
            <div class="d-flex align-items-center mb-3">
              <div class="workflow-icon-wrapper me-3 bg-success bg-opacity-10">
                <i class="bi bi-code-square fs-3 text-success"></i>
              </div>
              <h2 class="workflow-heading mb-0">Backend Development</h2>
            </div>
            <p class="workflow-description">
              Implementing the server-side logic for parsing Python code, analyzing variable scopes, and validating naming conventions.
            </p>
            <ul class="list-group list-group-flush mb-3">
              <li class="list-group-item bg-transparent ps-0">
                <i class="bi bi-check-circle-fill me-2 text-success"></i>
                <strong>Implement AST parsing</strong> for Python files
              </li>
              <li class="list-group-item bg-transparent ps-0">
                <i class="bi bi-check-circle-fill me-2 text-success"></i>
                <strong>Create variable scope identification</strong> logic
              </li>
              <li class="list-group-item bg-transparent ps-0">
                <i class="bi bi-check-circle-fill me-2 text-success"></i>
                <strong>Build naming convention validation</strong> based on PEP 8
              </li>
              <li class="list-group-item bg-transparent ps-0">
                <i class="bi bi-check-circle-fill me-2 text-success"></i>
                <strong>Develop RESTful API endpoints</strong> for frontend communication
              </li>
            </ul>
            <div class="tech-stack d-flex flex-wrap gap-2 mt-4">
              <span class="badge bg-light text-dark border">Python AST</span>
              <span class="badge bg-light text-dark border">Flask</span>
              <span class="badge bg-light text-dark border">RESTful API</span>
              <span class="badge bg-light text-dark border">JSON</span>
            </div>
          </div>
        </div>
      </div>
      
      <!-- Deployment -->
      <div class="col-md-6">
        <div class="card h-100 border-0 shadow-sm workflow-card">
          <div class="card-body p-4">
            <div class="d-flex align-items-center mb-3">
              <div class="workflow-icon-wrapper me-3 bg-danger bg-opacity-10">
                <i class="bi bi-cloud-upload fs-3 text-danger"></i>
              </div>
              <h2 class="workflow-heading mb-0">Deployment</h2>
            </div>
            <p class="workflow-description">
              Making the application available to users by deploying it to cloud platforms and configuring it for production use.
            </p>
            <ul class="list-group list-group-flush mb-3">
              <li class="list-group-item bg-transparent ps-0">
                <i class="bi bi-check-circle-fill me-2 text-success"></i>
                <strong>Deploy frontend</strong> to Netlify
              </li>
              <li class="list-group-item bg-transparent ps-0">
                <i class="bi bi-check-circle-fill me-2 text-success"></i>
                <strong>Deploy backend</strong> to Render
              </li>
              <li class="list-group-item bg-transparent ps-0">
                <i class="bi bi-check-circle-fill me-2 text-success"></i>
                <strong>Configure environment variables</strong> for production
              </li>
              <li class="list-group-item bg-transparent ps-0">
                <i class="bi bi-check-circle-fill me-2 text-success"></i>
                <strong>Set up continuous deployment</strong> for automated updates
              </li>
            </ul>
            <div class="tech-stack d-flex flex-wrap gap-2 mt-4">
              <span class="badge bg-light text-dark border">Netlify</span>
              <span class="badge bg-light text-dark border">Render</span>
              <span class="badge bg-light text-dark border">CI/CD</span>
              <span class="badge bg-light text-dark border">Environment Variables</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>