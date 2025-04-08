<script setup>
import ContentCard from '../components/ContentCard.vue'
</script>
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
            <router-link to="/architecture" class="btn btn-success">The Architecture</router-link>
            <router-link to="/tests" class="btn btn-info">The Tests</router-link>
            <router-link to="/report" class="btn btn-primary">The Report</router-link>
          </div>
        </div>
      </div>
    </section>
    
    <!-- Features Section -->
    <section class="py-5">
      <h2 class="text-center mb-4">Key Features</h2>
      <div class="row g-4">
        <div class="col-sm-12">
          <h3 class="">Backend <hr></h3>
        </div>
        <div class="col-md-6">
          <ContentCard title="Render - Deploying the Backend" image="/images/render-thumb.png">
            <p>Deploying the Python Flask backend with Render for a production-ready environment.</p>
            <template #footer>
              <a href="https://render.com/" target="_blank" class="btn btn-sm btn-outline-primary">Learn More</a>
            </template>
          </ContentCard>
        </div>
        <div class="col-md-6">
          <ContentCard title="Python + Flask Backend" image="/images/flask-thumb.png">
            <p>Lightweight and powerful Python Flask backend with RESTful API endpoints.</p>
            <template #footer>
              <a href="https://flask.palletsprojects.com/" target="_blank" class="btn btn-sm btn-outline-primary">Learn More</a>
            </template>
          </ContentCard>
        </div>
        <div class="col-sm-12 pt-4">
          <h3 class="">Frontend <hr></h3>
        </div>
        <div class="col-md-4">
          <ContentCard title="Vue 3 Frontend" image="/images/vue-thumb.png">
            <p>Built with Vue 3 Composition API and script setup for clean, maintainable code.</p>
            <template #footer>
              <a href="https://vuejs.org/" target="_blank" class="btn btn-sm btn-outline-primary">Learn More</a>
            </template>
          </ContentCard>
        </div>
        <div class="col-md-4">
          <ContentCard title="Bootstrap 5.3 & SASS" image="/images/bootstrap-thumb.png">
            <p>Responsive design with Bootstrap 5.3 and custom SASS styling for a modern look and feel.</p>
            <template #footer>
              <a href="https://getbootstrap.com/" target="_blank" class="btn btn-sm btn-outline-primary">Learn More</a>
            </template>
          </ContentCard>
        </div>
        <div class="col-md-4">
          <ContentCard title="Netlify - Deploying the Frontend" image="/images/netlify-thumb.png">
            <p>Deploying the Vue 3 frontend with Netlify for a production-ready environment.</p>
            <template #footer>
              <a href="https://netlify.com/" target="_blank" class="btn btn-sm btn-outline-primary">Learn More</a>
            </template>
          </ContentCard>
        </div>
      </div>
    </section>

  </div>
</template>