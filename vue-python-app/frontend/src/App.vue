<template>
  <AppLayout>
    <router-view />
  </AppLayout>
</template>

<script setup>
import { onMounted } from 'vue';
import AppLayout from './components/AppLayout.vue'

// Initialize theme based on user's preference when the app loads
onMounted(() => {
  // Check if user has a saved preference
  const savedTheme = localStorage.getItem('theme');
  
  if (savedTheme === 'dark') {
    document.documentElement.classList.add('dark-theme');
  } else if (savedTheme === 'light') {
    document.documentElement.classList.remove('dark-theme');
  } else {
    // Check for system preference if no saved preference
    const prefersDarkMode = window.matchMedia('(prefers-color-scheme: dark)').matches;
    
    if (prefersDarkMode) {
      document.documentElement.classList.add('dark-theme');
      localStorage.setItem('theme', 'dark');
    } else {
      localStorage.setItem('theme', 'light');
    }
  }
});
</script>

<style lang="scss">
@import './styles/main.scss';

.logo {
  // animation: spin 10s linear infinite;
}

@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

// Add some spacing between sections
section {
  margin-bottom: 2rem;
  
  h2 {
    position: relative;
    padding-bottom: 0.5rem;
    font-weight: 600;
    
    &::after {
      content: '';
      position: absolute;
      bottom: 0;
      left: 50%;
      transform: translateX(-50%);
      width: 50px;
      height: 3px;
      background-color: var(--primary);
      border-radius: 3px;
    }
  }
}

// Hero section styles
.hero-description {
  color: var(--text-secondary);
  
  .dark-theme & {
    color: var(--text-secondary);
    opacity: 0.9;
  }
}
</style>
