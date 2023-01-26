<template>
  <div class="modal-content login-width">
    <div class="box p-6">
        <form @submit.prevent="submitLogin">
        <h2 class="title">Login</h2>
        <div class="field">
            <label for="username">Username</label>
            <div class="control">
                <input type="text" class="input" v-model="username">
            </div>
        </div>
        <div class="field">
            <label for="password">Password</label>
            <div class="control">
                <input type="password" class="input" v-model="password" id="password" name="password">
                <div class="control">
                    <input type="checkbox" name="showPass" id="showPass" @click="showPass">
                    <label for="showPass" class="is-size-7"> Show Password</label>
                </div>
            </div>
            <a href="/reset-password" class="is-size-7">Forgot your password?</a>
        </div>
        <div class="has-text-centered"><button class="button is-dark" type="submit">Login</button></div>
                <div class="has-text-centered pt-4" v-if="errors.length">
                    <p class="has-text-danger is-size-6" v-for="error,index in errors" v-bind:key="index">{{ error }}</p>
                </div>
        </form>
        <hr>
        <p class="is-size-6">Don't have an account? <a href="/signup">Sign Up</a>.</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import {toast} from 'bulma-toast'
export default{
    name:'LoginModal',
    data(){
        return {
            username:'',
            password:'',
            errors:[],
        }
    },
    methods:{
        submitLogin(){
            if (this.username === ''){
                this.errors.push('Please enter your username')
            }
            if (this.password === ''){
                this.errors.push('Please enter your password')
            }
            axios.post('/token/login',{username:this.username,password:this.password})
            .then(response=>{
                let token = response.data.auth_token
                this.$store.commit('setToken',token)
                toast({
                    message:'Login Succesfull,Redirecting to Home Page.',
                    type:'is-success',
                    dismissible:true,
                    pauseOnHover:true,
                    duration:2000,
                    position:'bottom-right'
                })
                setInterval(() => {
                    window.location.href='/'
                }, 2000);
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
            const show_pass = document.querySelector('#showPass')
            const pass = document.querySelector('#password')
            if (show_pass.checked === true){
                pass.type='text'
            }else{
                pass.type = 'password'
            }
        }
    }
}
</script>

<style scoped>
.login-width{
    width: 500px;
}
</style>