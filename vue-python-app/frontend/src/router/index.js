import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../views/HomePage.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomePage
  },
  {
    path: '/architecture',
    name: 'Architecture',
    // Lazy load the architecture page for better performance
    component: () => import('../views/Architecture.vue')
  },
  {
    path: '/components',
    name: 'Components',
    // Lazy load the components page for better performance
    component: () => import('../views/ComponentsLibrary.vue')
  },
  {
    path: '/functionality',
    name: 'Functionality',
    // Lazy load the functionality page for better performance
    component: () => import('../views/Functionality.vue')
  },
  {
    path: '/ui',
    name: 'UI',
    // Lazy load the UI page for better performance
    component: () => import('../views/UI.vue')
  },
  {
    path: '/workflow',
    name: 'Workflow',
    // Lazy load the Workflow page for better performance
    component: () => import('../views/Workflow.vue')
  },
  {
    path: '/report',
    name: 'Report',
    component: () => import('../views/Report.vue')
  },
  {
    path: '/tests',
    name: 'Tests',
    component: () => import('../views/Tests.vue')
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
  linkActiveClass: 'active'
})

export default router
