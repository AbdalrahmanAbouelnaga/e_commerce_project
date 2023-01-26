import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ProductList from '../views/ProductList.vue'
import ProductDetail from '../views/ProductDetail.vue'
import Cart from '@/views/Cart.vue'
import CheckOut from '@/views/CheckOut.vue'
import Login from '@/views/Login.vue'
import SignUp from '@/views/SignUp.vue'
import MyAccount from '@/views/MyAccount.vue'
import store from '@/store'
import Success from '@/views/Success.vue'
import Search from '@/views/Search.vue'
const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path:'/search',
    name:'search',
    component:Search,
  },
  {
    path:'/cart/success',
    name:'success',
    component:Success,
    meta:{
      requireLogin:true
    }
  },
  {
    path:'/myaccount/',
    name:'MyAccount',
    component:MyAccount,
    meta:{
      requireLogin:true
    }
  },
  {
    path:'/login',
    name:'login',
    component:Login
  },
  {
    path:'/signup',
    name:'signup',
    component:SignUp
  },
  {
    path:'/categories/:category/subCategories/:subCategory/products',
    name: 'ProductList',
    component:ProductList
  },
  {
    path:'/categories/:category/subCategories/:subCategory/products/:product',
    name: 'ProductDetail',
    component:ProductDetail
  },
  {
    path:'/cart',
    name:'Cart',
    component: Cart,
  },
  {
    path:'/cart/checkout',
    name:'Checkout',
    component:CheckOut,
    meta:{
      requireLogin:true
    }
  },
  
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
    next({ name: 'login', query: { to: to.path } });
  } else {
    next()
  }
})

export default router
