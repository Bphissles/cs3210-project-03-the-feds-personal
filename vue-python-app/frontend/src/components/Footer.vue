<script setup>
import { ref } from 'vue';
import ToastNotification from './ToastNotification.vue';

// Get current year for the copyright
const currentYear = new Date().getFullYear();

// Toast state
const showToast = ref(false);
const toastMessage = ref('');
const toastTitle = ref('');

const showNotification = (message) => {
  toastMessage.value = message;
  toastTitle.value = 'Information';
  showToast.value = true;
};

const handleLinkClick = (e,message) => {
  e.preventDefault();
  showNotification(message);
};
</script>

<template>
  <footer class="footer mt-auto py-4">
    <div class="container">
      <div class="row">
        <div class="col-md-4 mb-3 mb-md-0">
          <h5 class="text-primary tech-title"><span class="text-secondary">The Feds</span> Project 3</h5>
          <p class="footer-text">A Python Variable Format and Scope Checker with Vue 3 and Python Flask.</p>
          <div class="d-flex gap-2">
            <a href="https://github.com/Bphissles/cs3210-project-03-the-feds-personal" class="btn btn-sm btn-outline-primary rounded-circle" target="_blank" rel="noopener noreferrer">
              <i class="bi bi-github"></i>
            </a>
            <a href="https://www.reddit.com/r/ChatGPT/comments/1jmifu0/best_ai_generated_video/" class="btn btn-sm btn-outline-primary rounded-circle" target="_blank" rel="noopener noreferrer">
              <i class="bi bi-twitter-x"></i>
            </a>
            <a href="https://www.linkedin.com/in/benjaminhislop/" class="btn btn-sm btn-outline-primary rounded-circle" target="_blank" rel="noopener noreferrer">
              <i class="bi bi-linkedin"></i>
            </a>
          </div>
        </div>
        <div class="col-md-2 mb-3 mb-md-0">
          <h6 class="tech-heading">Resources</h6>
          <ul class="list-unstyled tech-list">
            <li><a href="https://vuejs.org/" class="text-decoration-none footer-link" target="_blank" rel="noopener noreferrer"><i class="bi bi-box-arrow-up-right me-1 small"></i>Vue.js</a></li>
            <li><a href="https://getbootstrap.com/" class="text-decoration-none footer-link" target="_blank" rel="noopener noreferrer"><i class="bi bi-box-arrow-up-right me-1 small"></i>Bootstrap</a></li>
            <li><a href="https://flask.palletsprojects.com/" class="text-decoration-none footer-link" target="_blank" rel="noopener noreferrer"><i class="bi bi-box-arrow-up-right me-1 small"></i>Flask</a></li>
          </ul>
        </div>
        <div class="col-md-2 mb-3 mb-md-0">
          <h6 class="tech-heading">More Resources</h6>
          <ul class="list-unstyled tech-list">
            <li><a href="https://netlify.com/" class="text-decoration-none footer-link" target="_blank" rel="noopener noreferrer"><i class="bi bi-box-arrow-up-right me-1 small"></i>Netlify</a></li>
            <li><a href="https://render.com/" class="text-decoration-none footer-link" target="_blank" rel="noopener noreferrer"><i class="bi bi-box-arrow-up-right me-1 small"></i>Render</a></li>
          </ul>
        </div>
        <div class="col-md-4">
          <h6 class="tech-heading">Subscribe</h6>
          <p class="footer-text">Stay updated with our latest features and news.</p>
          <div class="input-group">
            <input type="email" class="form-control tech-input" placeholder="Email address">
            <button class="btn btn-primary tech-btn" type="button"  @click="handleLinkClick($event,'We don\'t actually want to talk with you')">
              <i class="bi bi-envelope-check me-1"></i> Subscribe
            </button>
          </div>
        </div>
      </div>
      <hr class="my-4">
      <div class="d-flex flex-column flex-md-row justify-content-between align-items-center">
        <p class="footer-text mb-md-0 copyright">© {{ currentYear }} <span class="tech-text">The Feds</span>. All rights reserved.</p>
        <div class="d-flex gap-3">
          <a href="#" class="text-decoration-none small tech-link" @click="handleLinkClick($event,'What would this even be?')">Privacy Policy</a>
          <a href="#" class="text-decoration-none small tech-link" @click="handleLinkClick($event,'Be patient, it will be here soon')">Terms of Service</a>
          <a href="#" class="text-decoration-none small tech-link" @click="handleLinkClick($event,'There is no contact, and I want it that way')">Contact</a>
        </div>
      </div>
    </div>
  </footer>


  <ToastNotification
    :show="showToast"
    :message="toastMessage"
    :title="toastTitle"
    @close="showToast = false"
  />
</template>

<style lang="scss" scoped>
.footer {
  border-top: 1px solid var(--border-color);
  background-color: var(--bg-secondary);
  
  .tech-title {
    font-family: 'JetBrains Mono', monospace;
    font-weight: 700;
    letter-spacing: -0.5px;
    margin-bottom: 1rem;
  }
  
  .tech-heading {
    font-family: 'JetBrains Mono', monospace;
    font-weight: 600;
    margin-bottom: 1rem;
    letter-spacing: 0.5px;
    text-transform: uppercase;
    font-size: 0.9rem;
  }
  
  .tech-text {
    font-family: 'JetBrains Mono', monospace;
    font-weight: 600;
  }
  
  .tech-list {
    li {
      margin-bottom: 0.5rem;
      
      a {
        font-family: 'Roboto', sans-serif;
        transition: all 0.2s ease;
        display: inline-flex;
        align-items: center;
        
        i {
          opacity: 0.6;
          font-size: 0.8rem;
        }
        
        &:hover {
          color: var(--bs-primary) !important;
          transform: translateX(3px);
          
          i {
            opacity: 1;
          }
        }
      }
    }
  }
  
  .footer-text {
    color: var(--text-secondary);
    
    .dark-theme & {
      color: var(--text-secondary);
      opacity: 0.9;
    }
  }
  
  .footer-link {
    color: var(--text-secondary);
    
    .dark-theme & {
      color: var(--text-secondary);
      opacity: 0.9;
    }
  }
  
  .tech-link {
    font-family: 'Roboto', sans-serif;
    transition: all 0.2s ease;
    position: relative;
    color: var(--text-secondary);
    
    .dark-theme & {
      color: var(--text-secondary);
      opacity: 0.9;
    }
    
    &:after {
      content: '';
      position: absolute;
      width: 0;
      height: 1px;
      bottom: -2px;
      left: 0;
      background-color: var(--bs-primary);
      transition: width 0.3s ease;
    }
    
    &:hover {
      color: var(--bs-primary) !important;
      
      &:after {
        width: 100%;
      }
    }
  }
  
  .tech-input {
    font-family: 'Roboto', sans-serif;
  }
  
  .tech-btn {
    font-family: 'JetBrains Mono', monospace;
    font-weight: 500;
    letter-spacing: 0.5px;
  }
  
  .copyright {
    font-family: 'Roboto', sans-serif;
    font-size: 0.9rem;
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
