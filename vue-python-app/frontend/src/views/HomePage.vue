<template>
  <div class="container">
    <!-- Hero Section -->
    <section class="py-5 text-center">
      <div class="row py-lg-5">
        <div class="col-lg-8 col-md-10 mx-auto">
          <img src="../assets/torch-trans.png" alt="Vue logo" class="logo mb-4" width="100">
          <h1 class="fw-bold">The Feds | Project 3</h1>
          <p class="lead hero-description">
            A Python Variable Format and Scope Checker built with<br>Vue 3, Bootstrap 5.3, and a Python Flask backend.
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
        <div class="col-md-10">
          <ContentCard title="API Integration Demo" subtitle="Test the connection to the Python backend">
            <HelloWorld />
          </ContentCard>
        </div>
      </div>
    </section>
    
    <!-- Python File Uploader Section -->
    <section class="py-3">
      <div class="row justify-content-center">
        <div class="col-md-10">
          <ContentCard title="Python File Analyzer" subtitle="Upload and view Python file contents">
            <PythonFileUploader />
          </ContentCard>
        </div>
      </div>
    </section>
    
    <!-- Features Section -->
    <section class="py-5">
      <h2 class="text-center mb-4">Key Features</h2>
      <div class="row g-4">
        <div class="col-md-4">
          <ContentCard title="Vue 3 Frontend - Hosted with Netlify" image="https://picsum.photos/id/1/500/300">
            <p>Built with Vue 3 Composition API and script setup for clean, maintainable code.</p>
            <template #footer>
              <a href="https://vuejs.org/" target="_blank" class="btn btn-sm btn-outline-primary">Learn More</a>
            </template>
          </ContentCard>
        </div>
        <div class="col-md-4">
          <ContentCard title="Python + Flask Backend - Hosted with Render" image="https://picsum.photos/id/3/500/300">
            <p>Lightweight and powerful Python Flask backend with RESTful API endpoints.</p>
            <template #footer>
              <a href="https://flask.palletsprojects.com/" target="_blank" class="btn btn-sm btn-outline-primary">Learn More</a>
            </template>
          </ContentCard>
        </div>
        <div class="col-md-4">
          <ContentCard title="Bootstrap 5.3 & SASS - Making things look good" image="https://picsum.photos/id/2/500/300">
            <p>Responsive design with Bootstrap 5.3 and custom SASS styling for a modern look and feel.</p>
            <template #footer>
              <a href="https://getbootstrap.com/" target="_blank" class="btn btn-sm btn-outline-primary">Learn More</a>
            </template>
          </ContentCard>
        </div>
      </div>
    </section>

  </div>
</template>

<script setup>
import HelloWorld from '../components/HelloWorld.vue'
import ContentCard from '../components/ContentCard.vue'
import PythonFileUploader from '../components/PythonFileUploader.vue'
</script>

<style lang="scss" scoped>
.hero-description {
  color: var(--text-secondary);
  
  .dark-theme & {
    color: var(--text-secondary);
    opacity: 0.9;
  }
}

.lead {
  font-size: 1.75rem;
}
</style>
