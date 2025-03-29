<script setup>

</script>

<template>
  <footer class="footer mt-auto py-4 bg-light">
    <div class="container">
      <div class="row">
        <div class="col-md-4 mb-3 mb-md-0">
          <h5 class="text-primary">Vue Python App</h5>
          <p class="text-muted">A modern web application with Vue 3 and Python Flask.</p>
          <div class="d-flex gap-2">
            <a href="#" class="btn btn-sm btn-outline-primary rounded-circle">
              <i class="bi bi-github"></i>
            </a>
            <a href="#" class="btn btn-sm btn-outline-primary rounded-circle">
              <i class="bi bi-twitter"></i>
            </a>
            <a href="#" class="btn btn-sm btn-outline-primary rounded-circle">
              <i class="bi bi-linkedin"></i>
            </a>
          </div>
        </div>
        <div class="col-md-2 mb-3 mb-md-0">
          <h6 class="text-dark">Links</h6>
          <ul class="list-unstyled">
            <li><a href="#" class="text-decoration-none text-muted">Home</a></li>
            <li><a href="#" class="text-decoration-none text-muted">Features</a></li>
            <li><a href="#" class="text-decoration-none text-muted">About</a></li>
          </ul>
        </div>
        <div class="col-md-2 mb-3 mb-md-0">
          <h6 class="text-dark">Resources</h6>
          <ul class="list-unstyled">
            <li><a href="https://vuejs.org/" class="text-decoration-none text-muted">Vue.js</a></li>
            <li><a href="https://getbootstrap.com/" class="text-decoration-none text-muted">Bootstrap</a></li>
            <li><a href="https://flask.palletsprojects.com/" class="text-decoration-none text-muted">Flask</a></li>
          </ul>
        </div>
        <div class="col-md-4">
          <h6 class="text-dark">Subscribe</h6>
          <p class="text-muted">Stay updated with our latest features and news.</p>
          <div class="input-group">
            <input type="email" class="form-control" placeholder="Email address">
            <button class="btn btn-primary" type="button">Subscribe</button>
          </div>
        </div>
      </div>
      <hr class="my-4">
      <div class="d-flex flex-column flex-md-row justify-content-between align-items-center">
        <p class="text-muted mb-md-0">© {{ new Date().getFullYear() }} Vue Python App. All rights reserved.</p>
        <div class="d-flex gap-3">
          <a href="#" class="text-decoration-none text-muted small">Privacy Policy</a>
          <a href="#" class="text-decoration-none text-muted small">Terms of Service</a>
          <a href="#" class="text-decoration-none text-muted small">Contact</a>
        </div>
      </div>
    </div>
  </footer>
</template>

<style lang="scss" scoped>
.footer {
  border-top: 1px solid rgba(0, 0, 0, 0.1);
  
  h5, h6 {
    font-weight: 600;
    margin-bottom: 1rem;
  }
  
  ul li {
    margin-bottom: 0.5rem;
    
    a {
      transition: all 0.2s ease;
      
      &:hover {
        color: var(--bs-primary) !important;
      }
    }
  }
  
  .btn-outline-primary {
    width: 32px;
    height: 32px;
    padding: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.3s ease;
    
    &:hover {
      transform: translateY(-3px);
    }
  }
}
</style>
