<script setup>
import { ref, onMounted, watch } from 'vue';

// State for theme
const isDarkMode = ref(false);

// Function to toggle theme
const toggleTheme = () => {
  isDarkMode.value = !isDarkMode.value;
  
  if (isDarkMode.value) {
    document.documentElement.classList.add('dark-theme');
    localStorage.setItem('theme', 'dark');
  } else {
    document.documentElement.classList.remove('dark-theme');
    localStorage.setItem('theme', 'light');
  }
};

// Initialize theme based on user's preference
onMounted(() => {
  // Check if user has a saved preference
  const savedTheme = localStorage.getItem('theme');
  
  if (savedTheme === 'dark') {
    isDarkMode.value = true;
    document.documentElement.classList.add('dark-theme');
  } else if (savedTheme === 'light') {
    isDarkMode.value = false;
    document.documentElement.classList.remove('dark-theme');
  } else {
    // Check for system preference if no saved preference
    const prefersDarkMode = window.matchMedia('(prefers-color-scheme: dark)').matches;
    isDarkMode.value = prefersDarkMode;
    
    if (prefersDarkMode) {
      document.documentElement.classList.add('dark-theme');
      localStorage.setItem('theme', 'dark');
    } else {
      localStorage.setItem('theme', 'light');
    }
  }
});
</script>

<template>
  <div class="theme-toggle" @click="toggleTheme" title="Toggle dark/light mode">
    <i v-if="isDarkMode" class="bi bi-sun-fill"></i>
    <i v-else class="bi bi-moon-fill"></i>
  </div>
</template>

<style lang="scss" scoped>
.theme-toggle {
  width: 40px;
  height: 40px;
  cursor: pointer;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
  background-color: var(--bg-secondary);
  color: var(--text-secondary);
  box-shadow: 0 2px 5px var(--shadow-color);
  
  &:hover {
    background-color: var(--bg-tertiary);
    transform: rotate(15deg);
  }
  
  i {
    font-size: 1.25rem;
  }
}
</style>
