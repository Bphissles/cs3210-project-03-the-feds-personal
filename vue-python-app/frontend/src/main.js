import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

// Import Bootstrap and SASS
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.bundle.min.js'
import './styles/main.scss'

const app = createApp(App)

// Use Vue Router
app.use(router)

// Mount the app
app.mount('#app')
