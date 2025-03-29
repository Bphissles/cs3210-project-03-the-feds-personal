<template>
  <div class="container py-5">
    <h1 class="mb-5 text-center">Components Library</h1>
    
    <!-- Content Cards Section -->
    <section class="mb-5">
      <h2 class="mb-4">Content Cards</h2>
      <div class="row g-4">
        <div class="col-md-4">
          <ContentCard 
            title="Basic Card" 
            subtitle="A simple content card"
          >
            <p>This is a basic content card with title and subtitle.</p>
            <template #footer>
              <button class="btn btn-sm btn-primary">Action</button>
            </template>
          </ContentCard>
        </div>
        
        <div class="col-md-4">
          <ContentCard 
            title="Card with Image" 
            subtitle="Includes a header image"
            image="https://picsum.photos/id/1/500/300"
          >
            <p>This card includes a header image above the title.</p>
            <template #footer>
              <div class="d-flex justify-content-between">
                <button class="btn btn-sm btn-outline-secondary">Cancel</button>
                <button class="btn btn-sm btn-primary">Submit</button>
              </div>
            </template>
          </ContentCard>
        </div>
        
        <div class="col-md-4">
          <ContentCard 
            title="Custom Header" 
            subtitle="With custom header class"
            headerClass="bg-primary text-white"
          >
            <p>This card has a custom header background color.</p>
            <template #footer>
              <button class="btn btn-sm btn-outline-primary w-100">Full Width Button</button>
            </template>
          </ContentCard>
        </div>
      </div>
    </section>
    
    <!-- Alert Messages Section -->
    <section class="mb-5">
      <h2 class="mb-4">Alert Messages</h2>
      
      <div class="row g-4">
        <div class="col-md-6">
          <AlertMessage type="success" title="Success Alert" icon="bi-check-circle-fill">
            This is a success alert with an icon and a title.
          </AlertMessage>
        </div>
        
        <div class="col-md-6">
          <AlertMessage type="danger" title="Error Alert" icon="bi-exclamation-triangle-fill">
            This is an error alert with an icon and a title.
          </AlertMessage>
        </div>
        
        <div class="col-md-6">
          <AlertMessage type="warning" title="Warning Alert" icon="bi-exclamation-circle-fill">
            This is a warning alert with an icon and a title.
          </AlertMessage>
        </div>
        
        <div class="col-md-6">
          <AlertMessage type="info" title="Info Alert" icon="bi-info-circle-fill">
            This is an info alert with an icon and a title.
          </AlertMessage>
        </div>
        
        <div class="col-md-6">
          <AlertMessage type="primary" icon="bi-info-circle-fill">
            This is a primary alert with an icon but no title.
          </AlertMessage>
        </div>
        
        <div class="col-md-6">
          <AlertMessage type="secondary">
            This is a secondary alert with no icon and no title.
          </AlertMessage>
        </div>
      </div>
    </section>
    
    <!-- Toast Notification Section -->
    <section class="mb-5">
      <h2 class="mb-4">Toast Notifications</h2>
      
      <div class="row g-4">
        <div class="col-md-6">
          <ContentCard title="Toast Demo">
            <div class="d-grid gap-2">
              <button class="btn btn-primary" @click="showToast('Information', 'This is a basic toast notification')">
                Show Basic Toast
              </button>
              <button class="btn btn-success" @click="showToast('Success', 'Your action was completed successfully', 5000)">
                Show Success Toast (5s)
              </button>
              <button class="btn btn-danger" @click="showToast('Error', 'An error occurred while processing your request', 8000)">
                Show Error Toast (8s)
              </button>
            </div>
          </ContentCard>
        </div>
        
        <div class="col-md-6">
          <ContentCard title="Toast Usage">
            <p>Import the ToastNotification component:</p>
            <pre><code>import ToastNotification from '../components/ToastNotification.vue';</code></pre>
            <p>Add the component to your template:</p>
            <pre><code>&lt;ToastNotification
  :show="showToast"
  :title="toastTitle"
  :message="toastMessage"
  :duration="3000"
  @close="showToast = false"
/&gt;</code></pre>
          </ContentCard>
        </div>
      </div>
    </section>
    
    <!-- Theme Toggle Section -->
    <section class="mb-5">
      <h2 class="mb-4">Theme Toggle</h2>
      
      <div class="row g-4">
        <div class="col-md-6">
          <ContentCard title="Theme Toggle Demo">
            <div class="d-flex justify-content-center align-items-center py-3">
              <ThemeToggle />
            </div>
            <p class="text-center mt-3">Click the icon above to toggle between light and dark themes.</p>
          </ContentCard>
        </div>
        
        <div class="col-md-6">
          <ContentCard title="Theme Toggle Usage">
            <p>Import the ThemeToggle component:</p>
            <pre><code>import ThemeToggle from '../components/ThemeToggle.vue';</code></pre>
            <p>Add the component to your template:</p>
            <pre><code>&lt;ThemeToggle /&gt;</code></pre>
            <p>The component will automatically handle theme switching and persistence.</p>
          </ContentCard>
        </div>
      </div>
    </section>
  </div>
  
  <!-- Toast component for demo -->
  <ToastNotification
    :show="toastVisible"
    :title="toastTitle"
    :message="toastMessage"
    :duration="toastDuration"
    @close="toastVisible = false"
  />
</template>

<script setup>
import { ref } from 'vue';
import ContentCard from '../components/ContentCard.vue';
import AlertMessage from '../components/AlertMessage.vue';
import ThemeToggle from '../components/ThemeToggle.vue';
import ToastNotification from '../components/ToastNotification.vue';

// Toast state
const toastVisible = ref(false);
const toastTitle = ref('');
const toastMessage = ref('');
const toastDuration = ref(3000);

// Show toast function
const showToast = (title, message, duration = 3000) => {
  toastTitle.value = title;
  toastMessage.value = message;
  toastDuration.value = duration;
  toastVisible.value = true;
};
</script>

<style lang="scss" scoped>
pre {
  background-color: var(--bg-tertiary);
  padding: 1rem;
  border-radius: 0.375rem;
  overflow-x: auto;
  
  code {
    color: var(--text-primary);
    background-color: transparent;
    padding: 0;
  }
  
  .dark-theme & {
    code {
      color: var(--text-primary);
    }
  }
}
</style>
