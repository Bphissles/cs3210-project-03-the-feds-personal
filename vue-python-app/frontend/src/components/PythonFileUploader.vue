<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { config } from '../config'
import hljs from 'highlight.js/lib/core'
import python from 'highlight.js/lib/languages/python'
import 'highlight.js/styles/atom-one-dark.css'

const props = defineProps({
  endpoint: {
    type: String,
    required: true
  },
  endpointUrl: {
    type: String,
    required: true
  }
})

const pythonFile = ref(null)
const fileName = ref('')
const fileContent = ref('')
const parsingResult = ref(null)
const loading = ref(false)
const error = ref(null)
const success = ref(false)
const isAdvancedParser = ref(false)

const handleFileChange = (event) => {
  const file = event.target.files[0]
  if (file && file.name.endsWith('.py')) {
    pythonFile.value = file
    fileName.value = file.name
    error.value = null
  } else if (file) {
    error.value = 'Please select a Python (.py) file'
    pythonFile.value = null
    fileName.value = ''
  }
}

const uploadFile = async () => {
  if (!pythonFile.value) {
    error.value = 'Please select a Python file first'
    return
  }

  loading.value = true
  error.value = null
  success.value = false
  parsingResult.value = null
  
  try {
    const formData = new FormData()
    formData.append('file', pythonFile.value)
    
    const response = await axios.post(`${config.apiBaseUrl}/${props.endpoint}`, formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    })
    
    // Check if this is the advanced parser response
    if (response.data.parsing_result) {
      isAdvancedParser.value = true
      parsingResult.value = response.data.parsing_result
      fileContent.value = ''
    } else {
      isAdvancedParser.value = false
      fileContent.value = response.data.content || ''
      parsingResult.value = null
    }
    
    success.value = true
  } catch (err) {
    error.value = err.message || 'Error uploading file'
    console.error('API Error:', err)
  } finally {
    loading.value = false
  }
}

const resetForm = () => {
  pythonFile.value = null
  fileName.value = ''
  fileContent.value = ''
  parsingResult.value = null
  error.value = null
  success.value = false
  isAdvancedParser.value = false
  
  // Reset the file input
  const fileInput = document.getElementById('python-file-input')
  if (fileInput) {
    fileInput.value = ''
  }
}

// Initialize highlight.js
onMounted(() => {
  // Register the Python language
  hljs.registerLanguage('python', python)
})

// Function to apply syntax highlighting
const highlightCode = (code) => {
  if (!code) return ''
  try {
    return hljs.highlight(code, { language: 'python' }).value
  } catch (e) {
    console.error('Highlighting error:', e)
    return code
  }
}
</script>

<template>
  <div class="python-file-uploader">
    <div class="file-upload-form mb-4">
      <div class="mb-3">
        <label for="python-file-input" class="form-label">Select Python File</label>
        <input 
          type="file" 
          class="form-control" 
          id="python-file-input" 
          accept=".py"
          @change="handleFileChange"
          :disabled="loading"
        >
        <div class="form-text" v-if="fileName">Selected: {{ fileName }}</div>
      </div>
      
      <div class="d-flex gap-2">
        <button 
          @click="uploadFile" 
          class="btn btn-primary tech-btn" 
          :disabled="loading || !pythonFile"
        >
          <i class="bi bi-cloud-upload me-1"></i>
          {{ loading ? 'Uploading...' : 'Upload File' }}
        </button>
        <button 
          @click="resetForm" 
          class="btn btn-outline-secondary tech-btn" 
          :disabled="loading || (!fileName && !fileContent)"
        >
          <i class="bi bi-arrow-counterclockwise me-1"></i>
          Reset
        </button>
      </div>
    </div>
    
    <div class="response-container mb-4">
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
      <div v-else-if="success" class="file-content-display">
        <div class="alert alert-success d-flex align-items-center mb-3" role="alert">
          <i class="bi bi-check-circle-fill me-2 flex-shrink-0"></i>
          <div>
            <strong class="tech-text">Success!</strong> File uploaded and processed.
          </div>
        </div>
        
        <!-- Simple parser response (file content) -->
        <div v-if="fileContent && !isAdvancedParser">
          <h5 class="mb-2">File Content:</h5>
          <div class="code-container">
            <pre class="code-block"><code class="language-python" v-html="highlightCode(fileContent)"></code></pre>
          </div>
        </div>
        
        <!-- Advanced parser response (AST data) -->
        <div v-if="parsingResult && isAdvancedParser">
          <h5 class="mb-2">AST Parsing Results:</h5>
          <div class="mb-3">
            <div v-if="parsingResult.success" class="parsing-results">
              <pre class="code-block"><code class="language-python">{{ parsingResult }}</code></pre>
            </div>
            <div v-else class="alert alert-danger">
              <strong>Parsing Error:</strong> {{ parsingResult.error }}
            </div>
          </div>
        </div>
      </div>
    </div>
    
    <div class="mt-4 pt-3 border-top endpoint-details">
      <h6 class="mb-2 tech-subheading">API Endpoint Details:</h6>
      <div class="d-flex align-items-center endpoint-code-block">
        <code class="p-2 rounded flex-grow-1 endpoint-url">{{ endpointUrl }}</code>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.python-file-uploader {
  
  .endpoint-details {
    .tech-subheading {
      opacity: 0.9;
      color: var(--text-primary);
      font-weight: 600;
    }
  }
}
</style>
