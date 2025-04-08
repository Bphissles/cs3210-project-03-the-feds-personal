<script setup>
import ContentCard from '../components/ContentCard.vue'
import PythonFileUploader from '../components/PythonFileUploader.vue'
import HelloWorld from '../components/HelloWorld.vue'
</script>

<template>
  <div class="container py-5">
    <h1 class="text-center mb-5">The Tests</h1>

     <!-- API Demo Section -->
     <section class="py-3">
      <div class="row justify-content-center">
        <div class="col-md-10">
          <ContentCard title="API Integration Demo" subtitle="Test the connection to the Python backend">
            <HelloWorld />
          </ContentCard>
        </div>
      </div>
    </section>

    <!-- Python File Uploader Section -->
    <section class="py-3">
      <div class="row justify-content-center">
        <div class="col-md-10">
          <ContentCard 
            title="Python File Analyzer - Simple" 
            subtitle="Upload and view Python file contents"
            wellTitle="Python File Analyzer - Simple"
            wellSubtitle="Upload a Python (.py) file to view its contents. The file will be sent to the backend for processing."
          >
            <PythonFileUploader endpoint="python-file" endpointUrl="http://localhost:5000/api/python-file"/>
          </ContentCard>
        </div>
      </div>
    </section>

    <!-- Python File Uploader Section -->
    <section class="py-3">
      <div class="row justify-content-center">
        <div class="col-md-10">
          <ContentCard 
            title="Python File Analyzer - Advanced" 
            subtitle="Upload and view Python file contents"
            wellTitle="Python File Analyzer - Advanced"
            wellSubtitle="Upload a Python (.py) file to view its contents. The file will be sent to the backend for processing."
          >
            <PythonFileUploader endpoint="file-parser" endpointUrl="http://localhost:5000/api/file-parser"/>
          </ContentCard>
        </div>
      </div>
    </section>
  </div>
</template>