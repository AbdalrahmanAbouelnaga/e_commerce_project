import axios from 'axios'
import { createStore } from 'vuex'

export default createStore({
  state: {
    cart:{
      items:[]
    },
    user_name:'',
    token:'',
    isAuthenticated:false
  },
  getters: {
  },
  mutations: {
    initializeStore(state){
      if(localStorage.getItem('cart')){
        state.cart = JSON.parse(localStorage.getItem('cart'))
      }else{
        localStorage.setItem('cart',JSON.stringify(state.cart))
      }
      if (localStorage.getItem('token')){
        state.token = JSON.parse(localStorage.getItem('token'))
        state.isAuthenticated = true
        state.user_name = JSON.parse(localStorage.getItem('user_name'))
        axios.defaults.headers.common['Authorization'] = 'Token '+state.token
      }else{
        state.token = ''
        state.isAuthenticated = false
      }
    },
    addToCart(state,item){
      const exists = state.cart.items.filter(i => i.product.id === item.product.id)
      if (exists.length){
        exists[0].quantity = exists[0].quantity + item.quantity 
      }else {
        state.cart.items.push(item)
      }
      localStorage.setItem('cart',JSON.stringify(state.cart))
    },
    removeFromCart(state,item){
      state.cart.items = state.cart.items.filter(i=> i.product.id !== item.product.id)
      localStorage.setItem('cart',JSON.stringify(state.cart))
    },
    setToken(state,token){
      state.token = token
      state.isAuthenticated = true
      localStorage.setItem('token', JSON.stringify(state.token))
      axios.defaults.headers.common['Authorization'] = 'Token '+state.token
      axios.get('/users/me')
            .then(response=>{
              state.user_name = response.data.username
              localStorage.setItem('user_name',JSON.stringify(response.data.username))
            }).catch(error=>console.log(error))
    },
    removeToken(state){
      state.token = ''
      state.isAuthenticated = false
      state.user_name=''
      localStorage.removeItem('user_name')
      localStorage.removeItem('token')
      axios.defaults.headers.common['Authorization'] = ''
    },
    clearCart(state){
      state.cart = {items:[]}
      localStorage.setItem('cart',JSON.stringify(state.cart))
    }
  },
  actions: {
  },
  modules: {
  }
})
