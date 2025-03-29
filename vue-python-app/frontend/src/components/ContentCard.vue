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
      <h6 v-if="subtitle" class="card-subtitle mt-1 text-muted">{{ subtitle }}</h6>
    </div>
    <div class="card-body">
      <slot></slot>
    </div>
    <div v-if="$slots.footer" class="card-footer">
      <slot name="footer"></slot>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.content-card {
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  border: none;
  border-radius: 0.5rem;
  overflow: hidden;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
  
  &:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 15px rgba(0, 0, 0, 0.1);
  }
  
  .card-img-top-wrapper {
    overflow: hidden;
    
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
    background-color: transparent;
    border-bottom: 1px solid rgba(0, 0, 0, 0.05);
    
    .card-title {
      font-weight: 600;
    }
  }
  
  .card-footer {
    background-color: transparent;
    border-top: 1px solid rgba(0, 0, 0, 0.05);
  }
}
</style>
