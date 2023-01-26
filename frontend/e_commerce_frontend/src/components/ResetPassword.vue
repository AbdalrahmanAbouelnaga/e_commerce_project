<template>
    <form class="column is-8" @submit.prevent="changePassword">
        <h1 class="title">Change Password</h1>
        <hr>
        <div class="field">
            <label for="currentPassword">Current Password</label>
            <div class="control">
                <input type="password" class="input" id="currentPassword" name="currentPassword" v-model="currentPassword">
            </div>
        </div>
        <div class="field">
            <label for="newPassword1">New Password</label>
            <div class="control">
                <input type="password" class="input" id="newPassword1" name="newPassword1" v-model="newPassword1">
            </div>
        </div>
        <div class="field">
            <label for="newPassword2">Repeat new password</label>
            <div class="control">
                <input type="password" class="input" id="newPassword2" name="newPassword2" v-model="newPassword2">
            </div>
        </div>
        <hr>
        <button class="button is-success">Change Password</button>
    </form>
</template>

<script>
import axios from 'axios';
import {toast} from 'bulma-toast';
export default{
    name:"ResetPassword",
    data(){
        return {
            currentPassword:'',
            newPassword1:'',
            newPassword2:'',
        }
    },
    methods:{
        changePassword(){
            if (this.currentPassword === ''){
                return toast({
                    message: 'Please enter your current password',
                    duration:2000,
                    dismissible:true,
                    pauseOnHover:true,
                    position:'bottom-right',
                    type:'is-warning'
                })
            }
            if (this.newPassword1 === ''){
                return toast({
                    message: 'Please enter your new password',
                    duration:2000,
                    dismissible:true,
                    pauseOnHover:true,
                    position:'bottom-right',
                    type:'is-warning'
                })
            }
            if (this.newPassword2 === ''){
                return toast({
                    message: 'Please repeat your new password',
                    duration:2000,
                    dismissible:true,
                    pauseOnHover:true,
                    position:'bottom-right',
                    type:'is-warning'
                })
            }
            if (this.newPassword1 !== this.newPassword2){
                return toast({
                    message: 'Your new passwords do not match. Please enter matching passwords',
                    duration:2000,
                    dismissible:true,
                    pauseOnHover:true,
                    position:'bottom-right',
                    type:'is-warning'
                })
            }
            axios.patch('/account/reset-pass',{
                currentPassword:this.currentPassword,
                newPassword:this.newPassword1,
            }).then(response=>{
                toast({
                    message:'Password changed successfully',
                    duration:2000,
                    position:'bottom-right',
                    type:'is-success',
                    dismissible:true,
                    pauseOnHover:true
                })
                setInterval(() => {
                    this.$emit('changePass')
                }, 2000);
            }).catch(error=>{
                console.log(error.response.data.message)
                toast({
                    message:error.response.data.message,
                    duration:2000,
                    position:'bottom-right',
                    type:'is-warning',
                    dismissible:true,
                    pauseOnHover:true
                })
            })
        }
    }
}
</script>