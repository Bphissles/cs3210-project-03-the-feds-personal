<template>
  <div class="toast-container position-fixed bottom-0 end-0 p-3">
    <div 
      class="toast show" 
      role="alert" 
      aria-live="assertive" 
      aria-atomic="true"
      v-if="visible"
    >
      <div class="toast-header">
        <strong class="me-auto">{{ title }}</strong>
        <button 
          type="button" 
          class="btn-close" 
          @click="hideToast" 
          aria-label="Close"
        ></button>
      </div>
      <div class="toast-body">
        {{ message }}
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue';

const props = defineProps({
  show: {
    type: Boolean,
    default: false
  },
  title: {
    type: String,
    default: 'Notification'
  },
  message: {
    type: String,
    default: ''
  },
  duration: {
    type: Number,
    default: 3000
  }
});

const visible = ref(props.show);
const emit = defineEmits(['close']);

const hideToast = () => {
  visible.value = false;
  emit('close');
};

// Auto-hide toast after duration
watch(() => props.show, (newValue) => {
  visible.value = newValue;
  if (newValue && props.duration > 0) {
    setTimeout(() => {
      hideToast();
    }, props.duration);
  }
});
</script>

<style lang="scss" scoped>
.toast {
  background-color: var(--bg-primary);
  border: 1px solid var(--border-color);
  box-shadow: 0 0.25rem 0.75rem rgba(0, 0, 0, 0.1);
  
  .toast-header {
    background-color: var(--bg-secondary);
    color: var(--text-primary);
    border-bottom: 1px solid var(--border-color);
  }
  
  .toast-body {
    color: var(--text-primary);
  }
  
  .dark-theme & {
    .btn-close {
      filter: invert(1) grayscale(100%) brightness(200%);
    }
  }
}
</style>
