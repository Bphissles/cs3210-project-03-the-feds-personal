<script setup>
import '@/styles/views/architecture.scss';
</script>

<template>
  <div class="container py-5">
    <section class="mb-5">
      <h1 class="display-4 fw-bold text-center mb-4">Project Architecture</h1>
      <p class="lead text-center mb-5">
        This project implements a modern web application with a Vue 3 frontend and Python Flask backend to analyze Python variable naming conventions and scope.
      </p>
      
      <div class="row mt-5 g-4">
        <div class="col-md-6">
          <div class="card h-100 border-0 shadow-sm architecture-card">
            <div class="card-body p-4">
              <div class="d-flex align-items-center mb-3">
                <div class="tech-icon-wrapper me-3 bg-success bg-opacity-10">
                  <i class="bi bi-code-slash fs-3 text-success"></i>
                </div>
                <h2 class="tech-heading mb-0">Frontend</h2>
              </div>
              <h5 class="tech-subheading mb-3">Technology Stack</h5>
              <div class="d-flex flex-wrap gap-2 mb-4">
                <span class="badge bg-primary">Vue 3</span>
                <span class="badge bg-info text-dark">Bootstrap 5.3</span>
                <span class="badge bg-secondary">SASS</span>
                <span class="badge bg-warning text-dark">Axios</span>
              </div>
              
              <h5 class="tech-subheading mb-3">Key Components</h5>
              <ul class="list-group list-group-flush mb-4">
                <li class="list-group-item bg-transparent ps-0">
                  <i class="bi bi-upload me-2 text-success"></i>
                  <strong>Python File Uploader:</strong> Drag-and-drop interface for uploading Python source files
                </li>
                <li class="list-group-item bg-transparent ps-0">
                  <i class="bi bi-code-square me-2 text-success"></i>
                  <strong>Syntax Highlighting:</strong> Displays code with color-coded syntax for better readability
                </li>
                <li class="list-group-item bg-transparent ps-0">
                  <i class="bi bi-table me-2 text-success"></i>
                  <strong>Results Dashboard:</strong> Presents analysis findings in a structured, easy-to-read format
                </li>
                <li class="list-group-item bg-transparent ps-0">
                  <i class="bi bi-phone me-2 text-success"></i>
                  <strong>Responsive Layout:</strong> Optimized for all screen sizes from mobile to presentation displays
                </li>
              </ul>
              
              <div class="deployment-section mt-2 p-3 rounded">
                <div class="d-flex align-items-center">
                  <div class="tech-icon-wrapper me-3 bg-primary bg-opacity-25">
                    <i class="bi bi-cloud-upload fs-4 text-primary"></i>
                  </div>
                  <div>
                    <h6 class="tech-subheading mb-1 fw-bold">Deployment</h6>
                    <p class="mb-0 deployment-text">Frontend deployed on <span class="deployment-platform">Netlify</span></p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        
        <div class="col-md-6">
          <div class="card h-100 border-0 shadow-sm architecture-card">
            <div class="card-body p-4">
              <div class="d-flex align-items-center mb-3">
                <div class="tech-icon-wrapper me-3 bg-info bg-opacity-10">
                  <i class="bi bi-server fs-3 text-info"></i>
                </div>
                <h2 class="tech-heading mb-0">Backend</h2>
              </div>
              <h5 class="tech-subheading mb-3">Technology Stack</h5>
              <div class="d-flex flex-wrap gap-2 mb-4">
                <span class="badge bg-success">Python</span>
                <span class="badge bg-danger">Flask</span>
                <span class="badge bg-dark">AST Module</span>
              </div>
              
              <h5 class="tech-subheading mb-3">Key Components</h5>
              <ul class="list-group list-group-flush mb-4">
                <li class="list-group-item bg-transparent ps-0">
                  <i class="bi bi-hdd-network me-2 text-info"></i>
                  <strong>RESTful API:</strong> Secure endpoints for file upload and code analysis requests
                </li>
                <li class="list-group-item bg-transparent ps-0">
                  <i class="bi bi-diagram-3 me-2 text-info"></i>
                  <strong>AST Parser:</strong> Analyzes Python code structure using Abstract Syntax Trees
                </li>
                <li class="list-group-item bg-transparent ps-0">
                  <i class="bi bi-layers me-2 text-info"></i>
                  <strong>Scope Analyzer:</strong> Identifies variable scopes (global/local) throughout the code
                </li>
                <li class="list-group-item bg-transparent ps-0">
                  <i class="bi bi-check2-square me-2 text-info"></i>
                  <strong>Style Validator:</strong> Verifies adherence to PEP 8 naming conventions
                </li>
              </ul>
              
              <div class="deployment-section backend-deployment mt-2 p-3 rounded">
                <div class="d-flex align-items-center">
                  <div class="tech-icon-wrapper me-3 bg-info bg-opacity-25">
                    <i class="bi bi-cloud-upload fs-4 text-info"></i>
                  </div>
                  <div>
                    <h6 class="tech-subheading mb-1 fw-bold">Deployment</h6>
                    <p class="mb-0 deployment-text">Backend deployed on <span class="deployment-platform backend-platform">Render</span></p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    
    <section class="mt-5">
      <h2 class="text-center mb-4">Architecture Diagram</h2>
      <div class="card border-0 shadow-sm architecture-card">
        <div class="card-body p-4">
          <div class="architecture-diagram py-4">
            <div class="row g-4">
              <div class="col-md-5">
                <div class="card diagram-card border-primary mb-3">
                  <div class="card-header bg-primary text-white">
                    <h5 class="mb-0">Frontend (Vue 3)</h5>
                  </div>
                  <div class="card-body">
                    <ul class="list-unstyled diagram-list">
                      <li class="mb-2"><i class="bi bi-file-earmark-code me-2 text-primary"></i><strong>Vue Components</strong></li>
                      <li class="mb-2"><i class="bi bi-brush me-2 text-primary"></i><strong>Bootstrap & SASS</strong></li>
                      <li class="mb-2"><i class="bi bi-arrow-repeat me-2 text-primary"></i><strong>Axios HTTP Client</strong></li>
                      <li><i class="bi bi-file-earmark-text me-2 text-primary"></i><strong>Code Highlighting</strong></li>
                    </ul>
                  </div>
                </div>
              </div>
              
              <div class="col-md-2 d-flex align-items-center justify-content-center">
                <div class="d-flex flex-column align-items-center">
                  <div class="arrow-right mb-2"></div>
                  <div class="tech-text fw-bold">HTTP/JSON</div>
                  <div class="arrow-left mt-2"></div>
                </div>
              </div>
              
              <div class="col-md-5">
                <div class="card diagram-card border-success mb-3">
                  <div class="card-header bg-success text-white">
                    <h5 class="mb-0">Backend (Flask)</h5>
                  </div>
                  <div class="card-body">
                    <ul class="list-unstyled diagram-list">
                      <li class="mb-2"><i class="bi bi-hdd-network me-2 text-success"></i><strong>RESTful API</strong></li>
                      <li class="mb-2"><i class="bi bi-diagram-3 me-2 text-success"></i><strong>AST Parser</strong></li>
                      <li class="mb-2"><i class="bi bi-braces me-2 text-success"></i><strong>Scope Analysis</strong></li>
                      <li><i class="bi bi-check2-all me-2 text-success"></i><strong>Naming Validation</strong></li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>