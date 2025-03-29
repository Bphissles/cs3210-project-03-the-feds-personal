<script setup>
import Navbar from './Navbar.vue'
import Footer from './Footer.vue'
</script>

<template>
  <div class="app-layout d-flex flex-column min-vh-100">
    <!-- Navbar component -->
    <Navbar />
    
    <!-- Main content area -->
    <main class="flex-grow-1 py-4">
      <slot></slot>
    </main>
    
    <!-- Footer component -->
    <Footer />
  </div>
</template>

<style lang="scss" scoped>
.app-layout {
  background-color: var(--bg-primary);
  transition: background-color 0.3s ease, color 0.3s ease;
}

main {
  background-color: var(--bg-primary);
  transition: background-color 0.3s ease;
}
</style>
