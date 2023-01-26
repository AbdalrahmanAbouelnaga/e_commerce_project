<template>
<div class="login-page">
    <div class="columns is-multiline">
        <div class="column is-4 is-offset-4">
            <form @submit.prevent="submitForm" class="box p-4">
                <h2 class="title has-text-centered">Login</h2>
                <div class="field">
                    <label for="username">Username</label>
                    <div class="control">
                        <input type="text" class="input" name="username" v-model="username">
                    </div>
                </div>
                <div class="field">
                    <label for="password">Password</label>
                    <div class="control">
                        <input type="password" id="password-login" class="input" name="password" v-model="password">
                        <div>
                            <input type="checkbox" name="showPass" id="showPass1" @click="showPass">
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
            <p class="subtitle">Don't have an account? <a href="/signup">Sign Up</a>.</p>
        </div>
    </div>
</div>
</template>


<script>
import axios from 'axios'
import {toast} from 'bulma-toast'
export default{
    name:'Login',
    data(){
        return {
            username:'',
            password: '',
            errors:[],
        }
    },
    methods:{
        submitForm(){
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
            const show_pass = document.querySelector('#showPass1')
            const pass = document.querySelector('#password-login')
            if (show_pass.checked === true){
                pass.type='text'
            }else{
                pass.type = 'password'
            }
        }
    }
}
</script>