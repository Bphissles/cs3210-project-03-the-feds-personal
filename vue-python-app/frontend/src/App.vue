<template>
  <AppLayout>
    <div class="container">
      <!-- Hero Section -->
      <section class="py-5 text-center">
        <div class="row py-lg-5">
          <div class="col-lg-8 col-md-10 mx-auto">
            <img src="./assets/logo.svg" alt="Vue logo" class="logo mb-4" width="100">
            <h1 class="fw-bold">Vue 3 + Python App</h1>
            <p class="lead text-muted">
              A modern web application built with Vue 3, Bootstrap 5.3, and a Python Flask backend.
              This template includes best practices for layout, components, and styling.
            </p>
            <div class="d-flex justify-content-center gap-2 mt-4">
              <a href="https://vuejs.org/" target="_blank" class="btn btn-primary">Learn Vue</a>
              <a href="https://flask.palletsprojects.com/" target="_blank" class="btn btn-outline-secondary">Learn Flask</a>
            </div>
          </div>
        </div>
      </section>
      
      <!-- API Demo Section -->
      <section class="py-3">
        <div class="row justify-content-center">
          <div class="col-md-8">
            <ContentCard title="API Integration Demo" subtitle="Test the connection to the Python backend">
              <HelloWorld />
            </ContentCard>
          </div>
        </div>
      </section>
      
      <!-- Features Section -->
      <section class="py-5">
        <h2 class="text-center mb-4">Key Features</h2>
        <div class="row g-4">
          <div class="col-md-4">
            <ContentCard title="Vue 3 Frontend" image="https://picsum.photos/id/1/500/300">
              <p>Built with Vue 3 Composition API and script setup for clean, maintainable code.</p>
              <template #footer>
                <a href="https://vuejs.org/" target="_blank" class="btn btn-sm btn-outline-primary">Learn More</a>
              </template>
            </ContentCard>
          </div>
          <div class="col-md-4">
            <ContentCard title="Bootstrap 5.3 & SASS" image="https://picsum.photos/id/2/500/300">
              <p>Responsive design with Bootstrap 5.3 and custom SASS styling for a modern look and feel.</p>
              <template #footer>
                <a href="https://getbootstrap.com/" target="_blank" class="btn btn-sm btn-outline-primary">Learn More</a>
              </template>
            </ContentCard>
          </div>
          <div class="col-md-4">
            <ContentCard title="Python Flask Backend" image="https://picsum.photos/id/3/500/300">
              <p>Lightweight Python Flask backend with RESTful API endpoints for your application needs.</p>
              <template #footer>
                <a href="https://flask.palletsprojects.com/" target="_blank" class="btn btn-sm btn-outline-primary">Learn More</a>
              </template>
            </ContentCard>
          </div>
        </div>
      </section>
      
      <!-- Alert Demo Section -->
      <section class="py-3">
        <h2 class="text-center mb-4">Alert Component Demo</h2>
        <div class="row g-3">
          <div class="col-md-6">
            <AlertMessage 
              type="success" 
              title="Success" 
              message="Operation completed successfully!"
            />
          </div>
          <div class="col-md-6">
            <AlertMessage 
              type="info" 
              title="Information" 
              message="This is an informational message."
            />
          </div>
          <div class="col-md-6">
            <AlertMessage 
              type="warning" 
              title="Warning" 
              message="Please be careful with this action."
            />
          </div>
          <div class="col-md-6">
            <AlertMessage 
              type="danger" 
              title="Error" 
              message="Something went wrong! Please try again."
            />
          </div>
        </div>
      </section>
    </div>
  </AppLayout>
</template>

<script setup>
import AppLayout from './components/AppLayout.vue'
import HelloWorld from './components/HelloWorld.vue'
import ContentCard from './components/ContentCard.vue'
import AlertMessage from './components/AlertMessage.vue'
</script>

<style lang="scss">
@import './styles/main.scss';

.logo {
  // animation: spin 10s linear infinite;
}

@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

// Add some spacing between sections
section {
  margin-bottom: 2rem;
  
  h2 {
    position: relative;
    padding-bottom: 0.5rem;
    font-weight: 600;
    
    &::after {
      content: '';
      position: absolute;
      bottom: 0;
      left: 50%;
      transform: translateX(-50%);
      width: 50px;
      height: 3px;
      background-color: var(--bs-primary);
      border-radius: 3px;
    }
  }
}
</style>
