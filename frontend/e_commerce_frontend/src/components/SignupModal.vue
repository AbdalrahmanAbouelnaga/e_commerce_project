<template>
    <div class="modal-content signup-width">
      <div class="box p-6">
          <form @submit.prevent="submitSignUp">
          <h2 class="title">Sign Up</h2>
          <div class="field">
              <label for="username">Username</label>
              <div class="control">
                  <input type="text" class="input" v-model="username" required>
              </div>
          </div>
          <div class="field">
              <label for="email">Email Address</label>
              <div class="control">
                  <input type="email" class="input" v-model="email" required>
              </div>
          </div>
          <div class="field">
              <label for="first_name">First Name</label>
              <div class="control">
                  <input type="text" class="input" v-model="first_name" required>
              </div>
          </div>
          <div class="field">
              <label for="last_name">Last Name</label>
              <div class="control">
                  <input type="text" class="input" v-model="last_name" required>
              </div>
            </div>
          <div class="field">
              <label for="password1">Password</label>
              <div class="control">
                  <input type="password" class="input" v-model="password1" id="password1" name="password1" required>
                  <div class="control">
                      <input type="checkbox" name="showPass" id="showPass-signup" @click="showPass">
                      <label for="showPass" class="is-size-7"> Show Password</label>
                  </div>
              </div>
          </div>
          <div class="field">
              <label for="password2">Repeat Password</label>
              <div class="control">
                  <input type="password" id="password2" class="input" v-model="password2" required>
              </div>
          </div>
          <div class="has-text-centered"><button class="button is-dark" type="submit">Sign Up</button></div>
                  <div class="has-text-centered pt-4" v-if="errors.length">
                      <p class="has-text-danger is-size-6" v-for="error,index in errors" v-bind:key="index">{{ error }}</p>
                  </div>
          </form>
          <hr>
          <p class="is-size-6">Already have an account? <a href="/login">Login</a>.</p>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios'
  import {toast} from 'bulma-toast'
  export default{
      name:'SignUpModal',
      data(){
          return {
              username:'',
              email:'',
              first_name:'',
              last_name:'',
              password1:'',
              password2:'',
              errors:[],
          }
      },
      methods:{
          submitSignUp(){
              if (this.password1 !== this.password2){
                return this.errors.push('Please enter matching passwords.')
              }
              axios.post('/user/',{
                                    username:this.username,
                                    email:this.email,
                                    first_name:this.first_name,
                                    last_name:this.last_name,
                                    password:this.password1})
              .then(response=>{
                  toast({
                      message:'SignUp Succesfull,Redirecting to Home Page.',
                      type:'is-success',
                      dismissible:true,
                      pauseOnHover:true,
                      duration:2000,
                      position:'bottom-right'
                  })
                  axios.post('/token/login',{username:this.username,password:this.password1})
                        .then(response=>{
                            let token = response.data.auth_token
                            this.$store.commit('setToken',token)
                            window.location.href = '/'
                        }).catch(error=>console.log(error))
              })
              .catch(error=>{
                  console.log(error)
                  toast({
                      message: "Invalid Credentials. Please enter a valid username and password",
                      type:'is-danger',
                      dismissible:true,
                      pauseOnHover:true,
                      duration:2000,
                      position:'bottom-right'
                  })
              })
          },
          showPass(){
              const show_pass = document.querySelector('#showPass-signup')
              const pass1 = document.querySelector('#password1')
              const pass2 = document.querySelector('#password2')
              if (show_pass.checked === true){
                  pass1.type='text'
                  pass2.type='text'
              }else{
                  pass1.type = 'password'
                  pass2.type = 'password'
              }
          }
      }
  }
  </script>
  
  <style scoped>
  .signup-width{
      width: 500px;
  }
  </style>