<template>
    <div class="columns">
        <div class="column is-6">
            <figure class="image">
                <img v-for="(image,index) in product.images" :key="image.id" :src="image.get_image" :class="{'is-hidden': index!==0}">
            </figure>
        </div>
        <div class="column is-6">
            <h1 class="title">{{ product.title }}</h1>
            <p class="subtitle is-size-6" v-html="product.description"></p>
            <div class="box">
                <h2 class="subtitle">Information</h2>
                <p><strong>Price: </strong>$ {{ totalPrice.toFixed(2) }}</p>
                <div class="field">
                    <label>Quantity</label>
                    <div class="control mb-4">
                        <input type="number" class="input" name="quantity" v-model="quantity" min="1">
                    </div>
                    <div class="control">
                        <a class="button is-dark" @click="addToCart">Add to Cart</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import {toast} from 'bulma-toast'
export default{
    name:'Detail',
    data(){
        return {
            product: {},
            quantity: 1
        }
    },
    mounted(){
        this.getProduct()
    },
    methods:{
        getProduct(){
            axios.get(this.$route.path)
            .then(response=>this.product = response.data)
            .catch(error => console.log(error))
        },
        addToCart(){
            if (isNaN(this.quantity) || this.quantity<0){
                this.quantity = 1
            }
            if (Number(this.quantity)){
            this.$store.commit('addToCart',{product:this.product,quantity:this.quantity})
            toast({
                message:`${this.quantity} ${this.product.title} has been added to your cart succesfully.`,
                duration:1500,
                position:'bottom-right',
                pauseOnHover:true,
                dismissible:true,
                type:'is-success'
            })
            }
        }
    },
    computed:{
        totalPrice(){
            return this.product.price * this.quantity
        }
    }
}
</script>