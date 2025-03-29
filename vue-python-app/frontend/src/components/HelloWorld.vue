<script setup>
import { ref } from 'vue'
import axios from 'axios'

const message = ref('')
const loading = ref(false)
const error = ref(null)

const fetchMessage = async () => {
  loading.value = true
  error.value = null
  
  try {
    // Use the full URL to the backend API
    const response = await axios.get('http://localhost:5000/api/hello')
    message.value = response.data.message
  } catch (err) {
    // Handle errors with detailed information
    error.value = err.message || 'Unknown error occurred while connecting to the API'
    console.error('API Error:', err)
  } finally {
    loading.value = false
  }
}

const resetMessage = () => {
  message.value = ''
  error.value = null
}

const copyEndpoint = () => {
  navigator.clipboard.writeText('http://localhost:5000/api/hello')
    .then(() => {
      // Could show a toast notification here
      console.log('Endpoint copied to clipboard')
    })
    .catch(err => {
      console.error('Failed to copy:', err)
    })
}
</script>

<template>
  <div class="api-demo">
    <p class="mb-4">
      This component demonstrates the connection between the Vue.js frontend and the Python Flask backend.
      Click the button below to fetch a message from the API endpoint.
    </p>
    
    <div class="api-response mb-4">
      <div v-if="loading" class="d-flex justify-content-center py-4">
        <div class="spinner-border text-primary" role="status">
          <span class="visually-hidden">Loading...</span>
        </div>
      </div>
      <div v-else-if="error" class="alert alert-danger d-flex align-items-center" role="alert">
        <i class="bi bi-exclamation-triangle-fill me-2"></i>
        <div>
          <strong>Error:</strong> {{ error }}
        </div>
      </div>
      <div v-else-if="message" class="alert alert-success d-flex align-items-center" role="alert">
        <i class="bi bi-check-circle-fill me-2"></i>
        <div>
          <strong>Success!</strong> Received message: "{{ message }}"
        </div>
      </div>
      <div v-else class="alert alert-info d-flex align-items-center" role="alert">
        <i class="bi bi-info-circle-fill me-2"></i>
        <div>
          No data yet. Click the button below to fetch data from the API.
        </div>
      </div>
    </div>
    
    <div class="d-flex gap-2">
      <button @click="fetchMessage" class="btn btn-primary" :disabled="loading">
        <i class="bi bi-cloud-download me-1"></i>
        {{ loading ? 'Fetching...' : 'Fetch from API' }}
      </button>
      <button @click="resetMessage" class="btn btn-outline-secondary" :disabled="loading || !message && !error">
        <i class="bi bi-arrow-counterclockwise me-1"></i>
        Reset
      </button>
    </div>
    
    <div class="mt-4 pt-3 border-top">
      <h6 class="text-muted mb-2">API Endpoint Details:</h6>
      <div class="d-flex align-items-center">
        <code class="bg-light p-2 rounded flex-grow-1">GET http://localhost:5000/api/hello</code>
        <button class="btn btn-sm btn-outline-primary ms-2" @click="copyEndpoint" title="Copy to clipboard">
          <i class="bi bi-clipboard"></i>
        </button>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.api-demo {
  .api-response {
    min-height: 80px;
  }
  
  button {
    transition: all 0.3s ease;
    
    &:not(:disabled):hover {
      transform: translateY(-2px);
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
  }
  
  code {
    font-size: 0.9rem;
    word-break: break-all;
  }
}
</style>
