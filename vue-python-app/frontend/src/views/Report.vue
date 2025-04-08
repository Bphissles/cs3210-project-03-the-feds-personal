<script setup>
import { computed } from 'vue';
import '@/styles/views/report.scss';

const tempData = [
  {
    variable: "MAX_COUNT",
    scope: "Global",
    line: 1,
    issue: "Should be UPPERCASE",
    status: 'warning'
  },
  {
    variable: "x",
    scope: "Local",
    line: 4,
    issue: "Naming OK",
    status: 'success'
  },
  {
    variable: "MAX_COUNT",
    scope: "Global",
    line: 5,
    issue: "Correct global usage",
    status: 'success'
  },
  {
    variable: "global_var",
    scope: "Local",
    line: 8,
    issue: "Warning: Global-like name but not declared global",
    status: 'warning'
  },
  {
    variable: "tempVar",
    scope: "Local",
    line: 9,
    issue: "Naming Violation: Use snake_case (suggestion: temp_var)",
    status: 'error'
  }
];

const totalIssues = computed(() => tempData.length);
const issuesByScope = computed(() => {
  const result = {};
  tempData.forEach(item => {
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
  
  tempData.forEach(item => {
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
    <h1 class="text-center mb-5">Scope Analysis Report</h1>

    <!-- Summary Cards Section -->
    <div class="row mb-4">
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
    <div class="row">
      <div class="col-md-12">
        <div class="card h-100 border-0 shadow-sm report-card">
          <div class="py-3 ps-3">
            <h4 class="card-title mb-0">Detailed Analysis</h4>
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
                <tr v-for="(item, index) in tempData" :key="index" :class="getRowClass(item.status)">
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