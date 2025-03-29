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
  <div v-if="show" :class="['alert', `alert-${type}`, 'alert-dismissible', 'fade', 'show']" role="alert">
    <div class="d-flex align-items-center">
      <div v-if="icon" class="alert-icon me-2">
        <i :class="['bi', iconClass]"></i>
      </div>
      <div>
        <strong v-if="title">{{ title }}</strong>
        <span v-if="title && message"> - </span>
        {{ message }}
      </div>
    </div>
    <button v-if="dismissible" type="button" class="btn-close" @click="dismiss" aria-label="Close"></button>
  </div>
</template>

<style lang="scss" scoped>
.alert {
  position: relative;
  border: none;
  border-left: 4px solid;
  border-radius: 0.25rem;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
  
  &.alert-success {
    border-left-color: var(--bs-success);
  }
  
  &.alert-danger {
    border-left-color: var(--bs-danger);
  }
  
  &.alert-warning {
    border-left-color: var(--bs-warning);
  }
  
  &.alert-info {
    border-left-color: var(--bs-info);
  }
  
  &.alert-primary {
    border-left-color: var(--bs-primary);
  }
  
  &.alert-secondary {
    border-left-color: var(--bs-secondary);
  }
  
  .alert-icon {
    font-size: 1.25rem;
  }
}
</style>
