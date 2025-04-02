<script setup>
defineProps({
  title: {
    type: String,
    default: ''
  },
  subtitle: {
    type: String,
    default: ''
  },
  image: {
    type: String,
    default: ''
  },
  headerClass: {
    type: String,
    default: ''
  },
  wellTitle: {
    type: String,
    default: ''
  },
  wellSubtitle: {
    type: String,
    default: ''
  }
})
</script>

<template>
  <div class="card content-card h-100">
    <div v-if="image" class="card-img-top-wrapper">
      <img :src="image" class="card-img-top" :alt="title">
    </div>
    <div v-if="title || subtitle" :class="['card-header', headerClass]">
      <h5 v-if="title" class="card-title mb-0">{{ title }}</h5>
      <h6 v-if="subtitle" class="card-subtitle mt-1 card-subtitle-text">{{ subtitle }}</h6>
    </div>
    <div class="card-body">
      <div v-if="wellTitle || wellSubtitle" class="well">
        <h3 v-if="wellTitle" class="tech-heading mb-3 mt-0">{{ wellTitle }}</h3>
        <p v-if="wellSubtitle" class="mb-4 description">{{ wellSubtitle }}</p>
      </div>
      <slot></slot>
    </div>
    <div v-if="$slots.footer" class="card-footer">
      <slot name="footer"></slot>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.content-card {
  transition: transform 0.3s ease, box-shadow 0.3s ease, background-color 0.3s ease;
  border: 1px solid var(--border-color);
  border-radius: 0.5rem;
  overflow: hidden;
  box-shadow: 0 4px 6px var(--shadow-color);
  background-color: var(--bg-primary);
  
  &:hover {
    // transform: translateY(-5px);
    box-shadow: 0 8px 15px var(--shadow-color);
  }
  
  .card-img-top-wrapper {
    overflow: hidden;
    position: relative;
    
    &:after {
      content: '';
      position: absolute;
      bottom: 0;
      left: 0;
      width: 100%;
      height: 30%;
      background: linear-gradient(to top, rgba(0,0,0,0.3), rgba(0,0,0,0));
      opacity: 0;
      transition: opacity 0.3s ease;
    }
    
    &:hover:after {
      opacity: 1;
    }
    
    img {
      transition: transform 0.5s ease;
      height: 180px;
      object-fit: cover;
      width: 100%;
      
      &:hover {
        transform: scale(1.05);
      }
    }
  }
  
  .card-header {
    background-color: var(--bg-secondary);
    border-bottom: 1px solid var(--border-color);
    padding: 1.25rem 1.25rem 0.75rem;
    
    .card-title {
      font-family: 'JetBrains Mono', monospace;
      font-weight: 600;
      letter-spacing: -0.5px;
      font-size: 1.25rem;
      color: var(--text-primary);
    }
    
    .card-subtitle {
      font-family: 'Roboto', sans-serif;
      font-size: 0.9rem;
      letter-spacing: 0.2px;
      color: var(--text-secondary);
      
      &.card-subtitle-text {
        .dark-theme & {
          color: var(--text-secondary);
          opacity: 0.85;
        }
      }
    }
  }
  
  .card-body {
    font-family: 'Roboto', sans-serif;
    line-height: 1.6;
    color: var(--text-primary);
    
    p {
      margin-bottom: 1rem;
    }
    
    h1, h2, h3, h4, h5, h6 {
      font-family: 'JetBrains Mono', monospace;
      font-weight: 600;
      margin-top: 1.5rem;
      margin-bottom: 1rem;
    }
  }
  
  .card-footer {
    background-color: var(--bg-secondary);
    border-top: 1px solid var(--border-color);
    font-family: 'Roboto', sans-serif;
    color: var(--text-secondary);
    
    // Card-specific button styles can go here if needed
  }
}
</style>
