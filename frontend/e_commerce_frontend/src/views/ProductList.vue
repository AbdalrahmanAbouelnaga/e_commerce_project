<template>
<div class="sub-category-page">

    <div class="hero is-light has-text-centered py-5 mb-5" v-if="!products.length">
        <h2 class="title">
            Sorry, We are out of {{ subCategory }} products.
        </h2>
        <p class="subtitle">Please check again later.</p>
    </div>
    <div class="columns is-multiline">
      <div class="column is-12 my-4 has-text-centered">
        <p class="title">{{ subCategory }}</p>
      </div>
      <div class="column is-10 is-offset-1">
    <div class="columns">
        <ProductBox v-if="products.length" v-for="product in products" v-bind:key="product.id" :product="product"/>

    </div>
    </div>
    </div>
</div>
</template>

<script>
import axios from 'axios'
import ProductBox from '@/components/ProductBox.vue'
export default{
    name:'ProductList',
    components:{
        ProductBox
    },
    data(){
        return {
            category:'',
            subCategory:'',
            products:[]
        }
    },
    mounted(){
        this.getProducts()
    },
    watch:{
        $route(to,from){
        if (to.name === 'ProductList'){
            this.getProducts()
        }
    }
    },
    methods:{
        getProducts(){
            axios.get(`/categories/${this.$route.params.category}/subCategories/${this.$route.params.subCategory}/products`)
            .then(response=>{
                this.products = response.data
                if (response.data.length){
                this.category = response.data[0].get_category
                this.subCategory = response.data[0].get_subCategory
                document.title = this.subCategory
                }
            }).catch(error=>console.log(error))
        }
    }
}
</script>