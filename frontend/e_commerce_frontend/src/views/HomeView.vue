<template>
  <div class="home">

    <div class="columns is-multiline">
      <div class="column is-12 my-4 has-text-centered">
        <p class="title">Latest Products</p>
      </div>
      <div class="column is-10 is-offset-1">
        <div class="columns">
          <ProductBox v-for="product in latestProducts" v-bind:key="product.id" v-bind:product="product"/>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src

import axios from 'axios';
import ProductBox from '@/components/ProductBox.vue'
export default {
  name: 'HomeView',
  components:{
    ProductBox
  },
  data() {
    return {
      latestProducts: [],
    }  
  },
  mounted(){
    this.getLatestProducts()
  },methods:{
    getLatestProducts(){
      axios.get('/latest-products')
      .then(response => this.latestProducts = response.data)
    }
  }
}
</script>

<style scoped>

</style>