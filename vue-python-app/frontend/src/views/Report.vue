<script setup>
import { ref, computed } from 'vue';
import axios from 'axios';
import { config } from '../config';
import '@/styles/views/report.scss';

// File upload related variables
const pythonFile = ref(null);
const fileName = ref('');
const loading = ref(false);
const error = ref(null);
const success = ref(false);

// Analysis results
const analysisData = ref([]);

// Handle file selection
const handleFileChange = (event) => {
  const file = event.target.files[0];
  if (file) {
    fileName.value = file.name;
    pythonFile.value = file;
  }
};

// Upload and analyze file
const uploadFile = async () => {
  if (!pythonFile.value) {
    error.value = 'Please select a file';
    return;
  }
  
  loading.value = true;
  error.value = null;
  success.value = false;
  
  try {
    const formData = new FormData();
    formData.append('file', pythonFile.value);
    
    const response = await axios.post(`${config.apiBaseUrl}/file-parser`, formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    });
    
    // Process the response
    if (response.data.naming_result && response.data.naming_result.success) {
      analysisData.value = response.data.naming_result.variables || [];
      success.value = true;
    } else {
      error.value = 'Failed to analyze file';
    }
  } catch (err) {
    error.value = err.message || 'Error uploading file';
    console.error('API Error:', err);
  } finally {
    loading.value = false;
  }
};

// Reset the form
const resetForm = () => {
  pythonFile.value = null;
  fileName.value = '';
  error.value = null;
  success.value = false;
  analysisData.value = [];
};

// Computed properties for report statistics
const totalIssues = computed(() => analysisData.value.length);
const issuesByScope = computed(() => {
  const result = {};
  analysisData.value.forEach(item => {
    if (!result[item.scope]) {
      result[item.scope] = 0;
    }
    result[item.scope]++;
  });
  return result;
});

const issueTypes = computed(() => {
  const types = {
    'Naming Violations': 0,
    'Scope Issues': 0,
    'Correct Usage': 0,
    'Other': 0
  };
  
  analysisData.value.forEach(item => {
    if (item.issue.includes('Naming Violation') || item.issue.includes('Should be')) {
      types['Naming Violations']++;
    } else if (item.issue.includes('Global') || item.issue.includes('Scope')) {
      types['Scope Issues']++;
    } else if (item.issue.includes('OK') || item.issue.includes('Correct')) {
      types['Correct Usage']++;
    } else {
      types['Other']++;
    }
  });
  
  return types;
});

const getRowClass = (status) => {
  if (status === 'error') {
    return 'table-danger';
  } else if (status === 'warning') {
    return 'table-warning';
  } else if (status === 'success') {
    return 'table-success';
  }
  return '';
};
</script>

<template>
  <div class="container py-5">
    <h1 class="text-center mb-5">Python Code Analysis Report</h1>
    
    <!-- File Upload Section -->
    <div class="card mb-4 border-0 shadow-sm">
      <div class="card-body">
        <h5 class="card-title mb-3">Upload Python File for Analysis</h5>
        <form @submit.prevent="uploadFile" class="mb-3">
          <div class="mb-3">
            <label for="pythonFile" class="form-label">Select Python File (.py)</label>
            <input 
              type="file" 
              class="form-control" 
              id="pythonFile" 
              accept=".py"
              @change="handleFileChange"
              :disabled="loading"
            >
          </div>
          
          <div class="d-flex gap-2">
            <button 
              type="submit" 
              class="btn btn-primary" 
              :disabled="!pythonFile || loading"
            >
              <span v-if="loading" class="spinner-border spinner-border-sm me-2" role="status" aria-hidden="true"></span>
              {{ loading ? 'Analyzing...' : 'Analyze File' }}
            </button>
            <button 
              type="button" 
              class="btn btn-outline-secondary" 
              @click="resetForm"
              :disabled="loading"
            >
              Reset
            </button>
          </div>
        </form>
        
        <div v-if="error" class="alert alert-danger">
          {{ error }}
        </div>
        
        <div v-if="success" class="alert alert-success">
          Successfully analyzed {{ fileName }}
        </div>
      </div>
    </div>

    <!-- Summary Cards Section -->
    <div v-if="analysisData.length > 0" class="row mb-4">
      <div class="col-md-4 mb-3">
        <div class="card h-100 border-0 shadow-sm summary-card">
          <div class="card-body">
            <h5 class="card-title">Total Issues</h5>
            <p class="display-4 text-accent">{{ totalIssues }}</p>
          </div>
        </div>
      </div>
      
      <div class="col-md-4 mb-3">
        <div class="card h-100 border-0 shadow-sm summary-card">
          <div class="card-body">
            <h5 class="card-title">Issues by Scope</h5>
            <div v-for="(count, scope) in issuesByScope" :key="scope" class="d-flex justify-content-between">
              <span>{{ scope }}:</span>
              <span class="fw-bold">{{ count }}</span>
            </div>
          </div>
        </div>
      </div>
      
      <div class="col-md-4 mb-3">
        <div class="card h-100 border-0 shadow-sm summary-card">
          <div class="card-body">
            <h5 class="card-title">Issue Types</h5>
            <div v-for="(count, type) in issueTypes" :key="type" class="d-flex justify-content-between">
              <span>{{ type }}:</span>
              <span class="fw-bold">{{ count }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Table Section -->
    <div v-if="analysisData.length > 0" class="row">
      <div class="col-md-12">
        <div class="card h-100 border-0 shadow-sm report-card">
          <div class="py-3 ps-3 d-flex justify-content-between align-items-center">
            <h4 class="card-title mb-0">Detailed Analysis</h4>
            <span class="badge bg-primary me-3">{{ analysisData.length }} variables analyzed</span>
          </div>
          <div class="table-responsive">
            <table class="table table-hover mb-0 report-table">
              <thead>
                <tr>
                  <th class="fw-bold">Variable</th>
                  <th class="fw-bold">Scope</th>
                  <th class="fw-bold">Line</th>
                  <th class="fw-bold">Issue</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(item, index) in analysisData" :key="index" :class="getRowClass(item.status)">
                  <td><code>{{ item.variable }}</code></td>
                  <td>{{ item.scope }}</td>
                  <td>{{ item.line }}</td>
                  <td>{{ item.issue }}</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>