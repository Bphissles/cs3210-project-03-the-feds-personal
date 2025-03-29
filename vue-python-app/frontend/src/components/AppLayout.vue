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
  background-color: #f5f7fa;
}
</style>
