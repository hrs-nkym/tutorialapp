import { createRouter, createWebHistory } from 'vue-router'
// import HomeView from '../views/HomeView.vue'
import Calendar from '@/components/Calendar.vue'

const routes = [
  {
    path: '/',
    name: 'django-calendar',
    component: {
      default: Calendar,
    }
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
