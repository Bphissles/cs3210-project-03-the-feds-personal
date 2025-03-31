<script setup>
import ThemeToggle from './ThemeToggle.vue';
import { useRoute } from 'vue-router';

const route = useRoute();
</script>

<template>
  <nav class="navbar navbar-expand-lg">
    <div class="container">
      <a class="navbar-brand d-flex align-items-center" href="#">
        <img src="../assets/torch-trans.png" alt="Vue Logo" width="30" height="30" class="me-2">
        <span class="brand-text">The Feds</span>
      </a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" 
              aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav me-auto">
          <li class="nav-item">
            <router-link class="nav-link" :class="{ active: route.path === '/' }" to="/">
              <i class="bi bi-house-door me-1"></i> Home
            </router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" :class="{ active: route.path === '/architecture' }" to="/architecture">
              <i class="bi bi-diagram-3 me-1"></i> Architecture
            </router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" :class="{ active: route.path === '/functionality' }" to="/functionality">
              <i class="bi bi-gear-fill me-1"></i> Functionality
            </router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" :class="{ active: route.path === '/ui' }" to="/ui">
              <i class="bi bi-layout-text-window me-1"></i> UI
            </router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" :class="{ active: route.path === '/workflow' }" to="/workflow">
              <i class="bi bi-kanban me-1"></i> Workflow
            </router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" :class="{ active: route.path === '/components' }" to="/components">
              <i class="bi bi-grid-3x3-gap me-1"></i> Components
            </router-link>
          </li>
        </ul>
        <div class="d-flex align-items-center">
          <ThemeToggle class="me-3" />
        </div>
      </div>
    </div>
  </nav>
</template>

<style lang="scss" scoped>
.navbar {
  box-shadow: 0 2px 4px var(--shadow-color);
  
  .navbar-brand {
    font-weight: 600;
    
    .brand-text {
      font-family: 'JetBrains Mono', monospace;
      font-size: 1.2rem;
      letter-spacing: -0.5px;
    }
    
    img {
      transition: transform 0.3s ease;
    }
    
    &:hover img {
      transform: rotate(20deg);
    }
  }
  
  .nav-link {
    font-family: 'JetBrains Mono', monospace;
    font-weight: 500;
    font-size: 0.9rem;
    letter-spacing: 0.5px;
    transition: all 0.2s ease;
    padding: 0.5rem 1rem;
    border-radius: 4px;
    margin: 0 0.2rem;
    
    &:hover {
      transform: translateY(-2px);
      background-color: var(--bg-tertiary);
    }
    
    &.active {
      background-color: var(--bg-tertiary);
      color: var(--primary);
      font-weight: 600;
    }
    
    i {
      font-size: 1rem;
    }
  }
  
  .btn {
    font-family: 'JetBrains Mono', monospace;
    font-weight: 500;
    letter-spacing: 0.5px;
    transition: all 0.2s ease;
    padding: 0.5rem 1.25rem;
    border-radius: 4px;
    
    &:hover {
      transform: translateY(-2px);
      box-shadow: 0 2px 4px var(--shadow-color);
    }
  }
}
</style>
