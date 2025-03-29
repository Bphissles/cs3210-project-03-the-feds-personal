<script setup>
import { ref, computed, onMounted } from 'vue'

const props = defineProps({
  type: {
    type: String,
    default: 'info',
    validator: (value) => ['success', 'danger', 'warning', 'info', 'primary', 'secondary'].includes(value)
  },
  title: {
    type: String,
    default: ''
  },
  message: {
    type: String,
    required: true
  },
  icon: {
    type: Boolean,
    default: true
  },
  dismissible: {
    type: Boolean,
    default: true
  },
  autoDismiss: {
    type: Boolean,
    default: false
  },
  dismissDelay: {
    type: Number,
    default: 5000
  }
})

// Reactive state
const show = ref(true)

// Computed properties
const iconClass = computed(() => {
  const iconMap = {
    success: 'bi-check-circle-fill',
    danger: 'bi-exclamation-triangle-fill',
    warning: 'bi-exclamation-circle-fill',
    info: 'bi-info-circle-fill',
    primary: 'bi-bell-fill',
    secondary: 'bi-gear-fill'
  }
  return iconMap[props.type] || 'bi-info-circle-fill'
})

// Methods
const dismiss = () => {
  show.value = false
}

// Lifecycle hooks
onMounted(() => {
  if (props.autoDismiss) {
    setTimeout(() => {
      dismiss()
    }, props.dismissDelay)
  }
})

// Expose methods to parent components
defineExpose({
  dismiss
})
</script>

<template>
  <div v-if="show" :class="['alert', `alert-${type}`, 'alert-dismissible', 'fade', 'show', 'tech-alert']" role="alert">
    <div class="d-flex align-items-center">
      <div v-if="icon" class="alert-icon me-2 flex-shrink-0">
        <i :class="['bi', iconClass]"></i>
      </div>
      <div>
        <strong v-if="title" class="alert-title">{{ title }}</strong>
        <span v-if="title && message" class="separator"> — </span>
        <span class="alert-message">{{ message }}</span>
      </div>
    </div>
    <button v-if="dismissible" type="button" class="btn-close" @click="dismiss" aria-label="Close"></button>
  </div>
</template>

<style lang="scss" scoped>
.tech-alert {
  position: relative;
  border: 1px solid var(--border-color);
  border-left: 4px solid;
  border-radius: 0.5rem;
  box-shadow: 0 4px 10px var(--shadow-color);
  padding: 1rem 1.25rem;
  transition: all 0.3s ease;
  color: var(--text-primary);
  
  &:hover {
    box-shadow: 0 6px 12px var(--shadow-color);
  }
  
  // Alert variants with improved contrast for dark mode
  &.alert-success {
    border-left-color: var(--bs-success);
    background-color: rgba(var(--bs-success-rgb), 0.15);
    
    .alert-icon {
      color: var(--bs-success);
    }
    
    .dark-theme & {
      background-color: rgba(var(--bs-success-rgb), 0.25);
      border-color: rgba(var(--bs-success-rgb), 0.5);
    }
  }
  
  &.alert-danger {
    border-left-color: var(--bs-danger);
    background-color: rgba(var(--bs-danger-rgb), 0.15);
    
    .alert-icon {
      color: var(--bs-danger);
    }
    
    .dark-theme & {
      background-color: rgba(var(--bs-danger-rgb), 0.25);
      border-color: rgba(var(--bs-danger-rgb), 0.5);
    }
  }
  
  &.alert-warning {
    border-left-color: var(--bs-warning);
    background-color: rgba(var(--bs-warning-rgb), 0.15);
    
    .alert-icon {
      color: var(--bs-warning);
    }
    
    .dark-theme & {
      background-color: rgba(var(--bs-warning-rgb), 0.25);
      border-color: rgba(var(--bs-warning-rgb), 0.5);
    }
  }
  
  &.alert-info {
    border-left-color: var(--bs-info);
    background-color: rgba(var(--bs-info-rgb), 0.15);
    
    .alert-icon {
      color: var(--bs-info);
    }
    
    .dark-theme & {
      background-color: rgba(var(--bs-info-rgb), 0.25);
      border-color: rgba(var(--bs-info-rgb), 0.5);
    }
  }
  
  &.alert-primary {
    border-left-color: var(--bs-primary);
    background-color: rgba(var(--bs-primary-rgb), 0.15);
    
    .alert-icon {
      color: var(--bs-primary);
    }
    
    .dark-theme & {
      background-color: rgba(var(--bs-primary-rgb), 0.25);
      border-color: rgba(var(--bs-primary-rgb), 0.5);
    }
  }
  
  &.alert-secondary {
    border-left-color: var(--bs-secondary);
    background-color: rgba(var(--bs-secondary-rgb), 0.15);
    
    .alert-icon {
      color: var(--bs-secondary);
    }
    
    .dark-theme & {
      background-color: rgba(var(--bs-secondary-rgb), 0.25);
      border-color: rgba(var(--bs-secondary-rgb), 0.5);
    }
  }
  
  .alert-icon {
    font-size: 1.25rem;
    opacity: 0.8;
  }
  
  .alert-title {
    font-family: 'JetBrains Mono', monospace;
    font-weight: 600;
    letter-spacing: -0.5px;
    color: var(--text-primary);
  }
  
  .separator {
    opacity: 0.6;
    margin: 0 0.25rem;
  }
  
  .alert-message {
    font-family: 'Roboto', sans-serif;
    font-weight: 400;
    color: var(--text-primary);
  }
  
  .btn-close {
    opacity: 0.5;
    transition: all 0.2s ease;
    
    &:hover {
      opacity: 1;
      transform: rotate(90deg);
    }
  }
}
</style>
