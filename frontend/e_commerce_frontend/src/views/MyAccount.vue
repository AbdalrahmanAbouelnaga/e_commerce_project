<template>
    <div class="myaccount-page">
        <div class="columns is-multiline">
            <div class="column is-8 is-offset-2 columns">
                <div class="column is-4 right-border">
                    <ul>
                        <li><a class="has-text-dark" @click="page='AccountInfo'">Account Information</a></li>
                        <li><a class="has-text-dark" @click="page='ResetPassword'">Reset Password</a></li>
                    </ul>
                </div>
                <AccountInfo v-if="page === 'AccountInfo'"></AccountInfo>
                <ResetPassword v-if="page === 'ResetPassword'" v-on:changePass="page = 'AccountInfo'" />
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import AccountInfo from '@/components/AccountInfo.vue';
import ResetPassword from '@/components/ResetPassword.vue'
export default {
    name:'MyAccount',
    components:{
        AccountInfo,
        ResetPassword
    },
    data(){
        return {
            page:'AccountInfo'
        }
    }
}
</script>

<style scoped>
.right-border{
    border-right: 1px solid grey;
}
</style>