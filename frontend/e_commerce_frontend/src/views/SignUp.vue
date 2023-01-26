<template>
    <div class="login-page">
    <div class="columns is-multiline">
        <div class="column is-8 is-offset-2">
            <form @submit.prevent="submitForm" class="columns is-multiline box">
                <h2 class="column is-12 has-text-centered title">Sign Up</h2>
                <div class="column is-half field">
                    <label for="username">Username</label>
                    <div class="control">
                        <input type="text" class="input" name="username" v-model="username">
                    </div>
                </div>
                <div class="column is-half field">
                    <label for="email">Email Address</label>
                    <div class="control">
                        <input type="email" class="input" name="email" v-model="email">
                    </div>
                </div>
                <div class="column is-half field">
                    <label for="first_name">First Name</label>
                    <div class="control">
                        <input type="text" class="input" name="first_name" v-model="first_name">
                    </div>
                </div>
                <div class="column is-half field">
                    <label for="last_name">Last Name</label>
                    <div class="control">
                        <input type="text" class="input" name="last_name" v-model="last_name">
                    </div>
                </div>
                <div class="column is-half field">
                    <label for="password1">Password</label>
                    <div class="control">
                        <input type="text" class="input" name="password1" v-model="password1">
                    </div>
                </div>
                <div class="column is-half field">
                    <label for="password2">Repeat Password</label>
                    <div class="control">
                        <input type="text" class="input" name="password2" v-model="password2">
                    </div>
                </div>
                <div class="column is-12 has-text-centered">
                    <button class="button is-success" type="submit">Sign Up</button>
                </div>
                <div class="has-text-centered column is-12" v-if="errors.length">
                    <p class="has-text-danger is-size-6" v-for="error,index in errors" :key="index">{{ error }}</p>
                </div>
            </form>
            <div class="information">
                <p class="subtitle">Already have an account? <a href="/login">Login</a>.</p>
            </div>
        </div>
    </div>
</div>
</template>

<script>
import axios from 'axios';
import {toast} from 'bulma-toast'

export default{
    name:'SignUp',
    data(){
        return {
            username:'',
            email:'',
            first_name:'',
            last_name:'',
            password1:'',
            password2:'',
            errors:[]
        }
    },
    methods:{
        submitForm(){
            this.errors =[]
            if(this.username===''){
                this.errors.push('Please enter your username')
            }
            if(this.email===''){
                this.errors.push('Please enter your Email Address')
            }
            if(this.first_name===''){
                this.errors.push('Please enter your First Name')
            }
            if(this.last_name===''){
                this.errors.push('Please enter your Last Name')
            }
            if(this.password1===''){
                this.errors.push('Please enter your Password')
            }
            if(this.password2===''){
                this.errors.push('Please confirm your password')
            }else if(this.password1 !== this.password2){
                this.errors.push('Passwords do not match')
            }
            if(!this.errors.length){
                axios.post('/signup/',{
                    username:this.username,
                    email:this.email,
                    first_name:this.first_name,
                    last_name:this.last_name,
                    password:this.password1,
                }).then(response=>{
                    toast({
                        message:"Sign up successfull.Redirecting to login page",
                        type:"is-success",
                        dismissible:true,
                        pauseOnHover:true,
                        duration:2000,
                        position:'bottom-right'
                    })
                    setInterval(()=>{
                        window.location.href='/login'
                    },1500)
                })
                .catch(error=>{
                    console.log(error)
                    toast({
                        message:error.response.data.message,
                        type:"is-danger",
                        dismissible:true,
                        pauseOnHover:true,
                        duration:5000,
                        position:'bottom-right'
                    })
                })
            }
        }
    }
}
</script>