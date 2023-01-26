<template>
  <div id="wrapper">
  <div class="navbar is-black">
    <div class="navbar-brand">
      <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu" @click="showMobileMenu= !showMobileMenu">
      <span aria-hidden="true"></span>
      <span aria-hidden="true"></span>
      <span aria-hidden="true"></span>
      </a>
      <router-link to="/" class="navbar-item"><strong>E Store</strong></router-link>
    </div>

    <div class="navbar-menu" id="navbar-menu" v-bind:class="{'is-active':showMobileMenu}">
      <div class="navbar-start">
        <div class="navbar-item" style="width:30rem;">
          <form action="/search" class="search-group">
  <svg class="icon-search" aria-hidden="true" viewBox="0 0 24 24"><g><path d="M21.53 20.47l-3.66-3.66C19.195 15.24 20 13.214 20 11c0-4.97-4.03-9-9-9s-9 4.03-9 9 4.03 9 9 9c2.215 0 4.24-.804 5.808-2.13l3.66 3.66c.147.146.34.22.53.22s.385-.073.53-.22c.295-.293.295-.767.002-1.06zM3.5 11c0-4.135 3.365-7.5 7.5-7.5s7.5 3.365 7.5 7.5-3.365 7.5-7.5 7.5-7.5-3.365-7.5-7.5z"></path></g></svg>
  <input placeholder="Search" type="search" name="query" style="width:30rem;" class="search-input">
</form>
        </div>
      </div>
      <div class="navbar-end">
        <div class="buttons mr-3">
          <router-link to="/cart" class="button is-black">
            <span class="icon"><svg class="svg-icon-cart" color="white" viewBox="0 0 20 20">
            <path d="M17.72,5.011H8.026c-0.271,0-0.49,0.219-0.49,0.489c0,0.271,0.219,0.489,0.49,0.489h8.962l-1.979,4.773H6.763L4.935,5.343C4.926,5.316,4.897,5.309,4.884,5.286c-0.011-0.024,0-0.051-0.017-0.074C4.833,5.166,4.025,4.081,2.33,3.908C2.068,3.883,1.822,4.075,1.795,4.344C1.767,4.612,1.962,4.853,2.231,4.88c1.143,0.118,1.703,0.738,1.808,0.866l1.91,5.661c0.066,0.199,0.252,0.333,0.463,0.333h8.924c0.116,0,0.22-0.053,0.308-0.128c0.027-0.023,0.042-0.048,0.063-0.076c0.026-0.034,0.063-0.058,0.08-0.099l2.384-5.75c0.062-0.151,0.046-0.323-0.045-0.458C18.036,5.092,17.883,5.011,17.72,5.011z"></path>
            <path d="M8.251,12.386c-1.023,0-1.856,0.834-1.856,1.856s0.833,1.853,1.856,1.853c1.021,0,1.853-0.83,1.853-1.853S9.273,12.386,8.251,12.386z M8.251,15.116c-0.484,0-0.877-0.393-0.877-0.874c0-0.484,0.394-0.878,0.877-0.878c0.482,0,0.875,0.394,0.875,0.878C9.126,14.724,8.733,15.116,8.251,15.116z"></path>
            <path d="M13.972,12.386c-1.022,0-1.855,0.834-1.855,1.856s0.833,1.853,1.855,1.853s1.854-0.83,1.854-1.853S14.994,12.386,13.972,12.386z M13.972,15.116c-0.484,0-0.878-0.393-0.878-0.874c0-0.484,0.394-0.878,0.878-0.878c0.482,0,0.875,0.394,0.875,0.878C14.847,14.724,14.454,15.116,13.972,15.116z"></path>
          </svg></span>
            <span> {{ cartTotalLength }}</span>
          </router-link>
          <a @click="showSignUp=!showSignUp" class="button is-info" v-if="!isAuthenticated">Sign Up</a>
          <button @click="showLogin=!showLogin" aria-haspopup="true" class="button is-light modal-button" v-if="!isAuthenticated">Login</button>
          <div class="dropdown is-hoverable" v-bind:class="{'is-active':showDropdown}" v-if="isAuthenticated">
            <div class="dropdown-trigger">
              <button class="button is-black" aria-haspopup="true" aria-controls="dropdown-menu2">
                <span>Hello, {{ user_name }}</span>
                <span class="icon is-small">
                  <i class="fas fa-angle-down" style="" aria-hidden="true"></i>
                </span>
              </button>
            </div>
            <div class="dropdown-menu" id="dropdown-menu2" role="menu">
              <div class="dropdown-content" style="position: relative;left: -18%;">
                <a class="dropdown-item" href="/myAccount">
                  My Account
                </a>
                <hr class="dropdown-divider">
                <a class="dropdown-item" href="/orders">
                  Orders
                </a>
                <hr class="dropdown-divider">
                <a @click="logout" class="dropdown-item">
                  Logout
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="navbar is-dark height-size" style="z-index: 0;"> 
    <div class="navbar-brand is-flex is-align-items-center height-size">
      <button class="navbar-burger navbar-item columns is-flex height-size" aria-label="menu" aria-expanded="false" @click="showSideBar = !showSideBar">
        <div class="column">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </div>
        <div class="">All</div>
      </button>
    </div>
    <div class="navbar-start ml-4 height-size">
      <router-link class="navbar-item" v-for="category in navSubCategories" v-bind:key="category.id" v-bind:to="category.get_products_relative">{{ category.name }}</router-link>
    </div>
  </div>

  <div class="modal modal-styles" id="sidebar-modal" v-bind:class="{'is-active':showSideBar}">
  <div class="modal-background" @click="showSideBar = !showSideBar"></div>
  <aside class="modal-content sidebar-styles menu">
    <p class="menu-label" @click="returnToCategories">
    <span>Categories</span>
  </p>
  <ul class="menu-list" id="menu-list-1">
    <li v-for="category in categories" v-bind:key="category.key" @click="showSubCategories(category.name,category.slug)"><a>{{ category.name }} <span class="icon"><i class="fas fa-angle-right"></i></span></a></li>
    
  </ul>
  <ul class="menu-list is-hidden" id="menu-list-2">

  </ul>
  
  </aside>
</div>
  
  <section class="section">
    <div class="modal" id="login-modal" v-bind:class="{'is-active':showLogin}">
      <div class="modal-background" @click="showLogin = !showLogin"></div>
      <LoginModal/>
      <button class="modal-close is-large" aria-label="close" @click="showLogin=!showLogin"></button>
    </div>
    <div class="modal" id="signup-modal" v-bind:class="{'is-active':showSignUp}">
      <div class="modal-background" @click="showSignUp = !showSignUp"></div>
      <SignupModal/>
      <button class="modal-close is-large" aria-label="close" @click="showSignUp=!showSignUp"></button>
    </div>
    <router-view/></section>
  <footer class="footer">
    <p class="has-text-centered">Copyright (c) 2023</p>
    
  </footer>
  </div>
</template>

<script>
import axios from 'axios'
import LoginModal from './components/LoginModal.vue'
import SignupModal from './components/SignupModal.vue'
export default{
  components:{
    LoginModal,
    SignupModal
  },
  data(){
    return {
      showMobileMenu:false,
      showSideBar:false,
      showLogin:false,
      showSignUp:false,
      showDropdown:false,
      user_name:'',
      cart:{
        items:[]
      },
      token:'',
      isAuthenticated:false,
      categories:[],
      navSubCategories:[],

    }
  },
  mounted(){
    this.$store.commit('initializeStore')
    this.cart = this.$store.state.cart
    this.token = this.$store.state.token
    this.isAuthenticated = this.$store.state.isAuthenticated
    this.user_name = this.$store.state.user_name
    this.getCategories()
  },
  methods:{
    getCategories(){
      axios.get('/categories')
      .then(response=>this.categories=response.data)
      .catch(error=>console.log(error))


      axios.get('/navCategories')
      .then(response => {
        this.navSubCategories =[]
        console.log(response.data)
        const data = response.data
        for (let i=0;i<data.length;i++){
          for(let j=0;j<2;j++){
          this.navSubCategories.push(response.data[i].subCategories[j])
          }
        }
        console.log(this.navSubCategories)
      })
      .catch(error=>console.log(error))
    },
    showSubCategories(name,slug){
      const menuList1 = document.querySelector('#menu-list-1')
      const menuList2 = document.querySelector('#menu-list-2')
      const menuLabel = document.querySelector('.menu-label')
      menuLabel.innerHTML = `<a class="has-text-grey"><span class="icon"><i class="fas fa-angle-left"></i></span> ${name}</a>`
      menuList1.classList.toggle('is-hidden')
      menuList2.classList.toggle('is-hidden')
      menuList2.innerHTML = ''
      axios.get(`/categories/${slug}/subCategories/`)
      .then(response=>{
        for (let i=0;i<response.data.length;i++){
          menuList2.innerHTML += `<li><a href=${response.data[i].get_products_relative}>${response.data[i].name}</a></li>`
        }
      })
    },returnToCategories(){
      const menuList1 = document.querySelector('#menu-list-1')
      const menuList2 = document.querySelector('#menu-list-2')
      const menuLabel = document.querySelector('.menu-label')
      menuList1.classList.toggle('is-hidden')
      menuList2.classList.toggle('is-hidden')
      menuLabel.innerHTML = '<span>Categories</span>'
    },
    logout(){
      axios.post('/token/logout/')
      .then(response=>{
        this.$store.commit('removeToken')
        window.location.href = '/'
      }).catch(error=>console.log(error))
    },
  },
  computed:{
    cartTotalLength(){
      return this.cart.items.reduce((acc,curVal)=>{
        return acc += curVal.quantity
      },0)
    }
  }
}
</script>

<style lang="scss">
@import '../node_modules/bulma';
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  // -webkit-font-smoothing: antialiased;
  // -moz-osx-font-smoothing: grayscale;
  // text-align: center;
  // color: #2c3e50;
}

// nav {
//   padding: 30px;

//   a {
//     font-weight: bold;
//     color: #2c3e50;

//     &.router-link-exact-active {
//       color: #42b983;
//     }
//   }
// }
.height-size{
  min-height: 2rem;
  height: 2rem;
  font-size: 0.8rem;
}
.sidebar-styles{
  background-color: white;
margin: 0;
padding: 20px 20px; 
width:19rem;
max-height: calc(100vh - 40px);
height: calc(100vh - 40px);
}
.modal-styles{
  top: 5.5rem;
align-items: inherit;
}
.svg-icon-cart{
  filter: invert(100%) sepia(0%) saturate(0%) hue-rotate(276deg) brightness(104%) contrast(101%);
}



.search-group {
 display: flex;
 line-height: 28px;
 align-items: center;
 position: relative;
 min-width: 190px;
}

.search-input {
 width: 100%;
 height: 40px;
 line-height: 28px;
 padding: 0 1rem;
 padding-left: 2.5rem;
 border: 2px solid transparent;
 border-radius: 8px;
 outline: none;
 background-color: #f3f3f4;
 color: #0d0c22;
 transition: .3s ease;
}

.search-input::placeholder {
 color: #9e9ea7;
}

.search-input:focus, input:hover {
 outline: none;
 border-color: rgba(234,76,137,0.4);
 background-color: #fff;
 box-shadow: 0 0 0 4px rgb(234 76 137 / 10%);
}

.icon-search {
 position: absolute;
 left: 1rem;
 fill: #9e9ea7;
 width: 1rem;
 height: 1rem;
}






</style>
