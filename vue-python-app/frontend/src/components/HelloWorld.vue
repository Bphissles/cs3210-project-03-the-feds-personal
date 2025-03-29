<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { config } from '../config'

const message = ref('')
const loading = ref(false)
const error = ref(null)

const fetchMessage = async () => {
  loading.value = true
  error.value = null
  
  try {
    // Use the full API URL from config
    const response = await axios.get(`${config.apiBaseUrl}/hello`)
    message.value = response.data.message
  } catch (err) {
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
  // Use the full API URL from config
  const apiUrl = `${config.apiBaseUrl}/hello`
  navigator.clipboard.writeText(apiUrl)
    .then(() => {
      console.log('Endpoint copied to clipboard')
    })
    .catch(err => {
      console.error('Failed to copy:', err)
    })
}
</script>

<template>
  <div class="api-demo">
    <h3 class="tech-heading mb-3">API Connection Demo</h3>
    <p class="mb-4 description">
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
        <i class="bi bi-exclamation-triangle-fill me-2 flex-shrink-0"></i>
        <div>
          <strong class="tech-text">Error:</strong> {{ error }}
        </div>
      </div>
      <div v-else-if="message" class="alert alert-success d-flex align-items-center" role="alert">
        <i class="bi bi-check-circle-fill me-2 flex-shrink-0"></i>
        <div>
          <strong class="tech-text">Success!</strong> Received message: <span class="message-text">"{{ message }}"</span>
        </div>
      </div>
      <div v-else class="alert alert-info d-flex align-items-center" role="alert">
        <i class="bi bi-info-circle-fill me-2 flex-shrink-0"></i>
        <div>
          <strong class="tech-text">Info:</strong> No data yet. Click the button below to fetch data from the API.
        </div>
      </div>
    </div>
    
    <div class="d-flex gap-2">
      <button @click="fetchMessage" class="btn btn-primary tech-btn" :disabled="loading">
        <i class="bi bi-cloud-download me-1"></i>
        {{ loading ? 'Fetching...' : 'Fetch from API' }}
      </button>
      <button @click="resetMessage" class="btn btn-outline-secondary tech-btn" :disabled="loading || !message && !error">
        <i class="bi bi-arrow-counterclockwise me-1"></i>
        Reset
      </button>
    </div>
    
    <div class="mt-4 pt-3 border-top endpoint-details">
      <h6 class="text-muted mb-2 tech-subheading">API Endpoint Details:</h6>
      <div class="d-flex align-items-center endpoint-code-block">
        <code class="p-2 rounded flex-grow-1">GET http://localhost:5000/api/hello</code>
        <button class="btn btn-sm btn-outline-primary ms-2 tech-btn-sm" @click="copyEndpoint" title="Copy to clipboard">
          <i class="bi bi-clipboard"></i>
        </button>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.api-demo {
  .tech-heading {
    font-family: 'JetBrains Mono', monospace;
    font-weight: 700;
    letter-spacing: -0.5px;
    color: var(--text-primary);
    margin-bottom: 1.25rem;
  }
  
  .tech-subheading {
    font-family: 'JetBrains Mono', monospace;
    font-weight: 600;
    font-size: 0.9rem;
    letter-spacing: 0.5px;
    text-transform: uppercase;
  }
  
  .tech-text {
    font-family: 'JetBrains Mono', monospace;
    font-weight: 600;
  }
  
  .description {
    font-family: 'Roboto', sans-serif;
    line-height: 1.6;
    font-size: 1rem;
  }
  
  .message-text {
    font-family: 'JetBrains Mono', monospace;
    font-weight: 500;
    background-color: var(--bg-tertiary);
    padding: 0.2rem 0.4rem;
    border-radius: 0.25rem;
    color: var(--accent-cyan);
    
    .dark-theme & {
      color: var(--accent-cyan);
      background-color: rgba(var(--bs-info-rgb), 0.2);
      border: 1px solid rgba(var(--bs-info-rgb), 0.3);
    }
  }
  
  .api-response {
    min-height: 80px;
    font-family: 'Roboto', sans-serif;
    
    .alert {
      border-radius: 0.5rem;
      border: 1px solid var(--border-color);
      box-shadow: 0 2px 4px var(--shadow-color);
    }
  }
  
  .tech-btn {
    font-family: 'JetBrains Mono', monospace;
    font-weight: 500;
    letter-spacing: 0.5px;
    padding: 0.5rem 1.25rem;
    border-radius: 0.4rem;
    transition: all 0.3s ease;
    
    &:not(:disabled):hover {
      transform: translateY(-2px);
      box-shadow: 0 4px 8px var(--shadow-color);
    }
  }
  
  .tech-btn-sm {
    font-family: 'JetBrains Mono', monospace;
    font-weight: 500;
    transition: all 0.2s ease;
    
    &:hover {
      transform: translateY(-1px);
    }
  }
  
  .endpoint-details {
    .tech-subheading {
      opacity: 0.7;
    }
  }
  
  .endpoint-code-block {
    background-color: var(--bg-secondary);
    border-radius: 0.5rem;
    padding: 0.5rem;
    border: 1px solid var(--border-color);
  }
  
  code {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.9rem;
    word-break: break-all;
    padding: 0.75rem;
    border-radius: 0.4rem;
    background-color: var(--bg-tertiary);
    color: var(--accent-cyan);
  }
}
</style>
