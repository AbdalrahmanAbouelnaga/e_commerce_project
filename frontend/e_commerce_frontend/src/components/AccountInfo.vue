<template>
    <div class="column is-8" v-if="!change">
        <h2 class="title">Account Information</h2>
        <hr>
        <h2><span class="subtitle">Username</span>: {{ username }}</h2>
        <h2><span class="subtitle">First Name</span>: {{ first_name }}</h2>
        <h2><span class="subtitle">Last Name</span>: {{ last_name }}</h2>
        <h2><span class="subtitle">Email Address</span>: {{ email }}</h2>
        <hr>
        <button class="button is-info" @click="change = true">
            Change Account Information
        </button>
    </div>
    <div class="column is-8" v-else>
        <h1 class="title">Change Account Information</h1>
        <hr>
        <div class="field">
            <label for="username">Username:</label>
            <div class="control">
                <input id="username" name="username" type="text" class="input" v-model="username">
            </div>
        </div>
        <div class="field">
            <label for="first_name">First Name:</label>
            <div class="control">
                <input id="first_name" name="first_name" type="text" class="input" v-model="first_name">
            </div>
        </div>
        <div class="field">
            <label for="last_name">Last Name:</label>
            <div class="control">
                <input id="last_name" name="last_name" type="text" class="input" v-model="last_name">
            </div>
        </div>
        <div class="field">
            <label for="email">Email Address:</label>
            <div class="control">
                <input id="email" name="email" type="email" class="input" v-model="email">
            </div>
        </div>
        <hr>
        <button class="button is-success" @click="submitInfo">Submit</button>
    </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'
export default{
    name:'AccountInfo',
    data(){
        return{
            username:'',
            first_name:'',
            last_name:'',
            email:'',
            change:false
        }
    },
    mounted(){
        this.getInfo()
    },
    methods:{
        getInfo(){
            axios.get('/user/')
            .then(response=>{
                this.username = response.data.username
                this.first_name = response.data.first_name
                this.last_name = response.data.last_name
                this.email = response.data.email
            }).catch(err=>console.log(err))
        },
        submitInfo(){
            axios.patch('/user/',{
                username:this.username,
                first_name:this.first_name,
                last_name:this.last_name,
                email:this.email
            }).then(response=>{
                this.username = response.data.username
                this.first_name = response.data.first_name
                this.last_name = response.data.last_name
                this.email = response.data.email
                this.change = false
                toast({
                    message:'Account Information Changed',
                    duration:2000,
                    position:'bottom-right',
                    dismissible:true,
                    pauseOnHover:true,
                    type:'is-success'
                })
            }).catch(err=>{
                toast({
                    message:err.response.data.message,
                    duration:2000,
                    position:'bottom-right',
                    dismissible:true,
                    pauseOnHover:true,
                    type:'is-danger'
                })
                console.log(err)})
        }
    }
}
</script>