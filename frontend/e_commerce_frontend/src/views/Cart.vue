<template>
    <div class="page-cart">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">
                    Cart
                </h1>
            </div>

            <div class="column is-12 box">
                <table class="table is-fullwidth" v-if="cartTotalLength">
                    <thead>
                        <tr>
                            <th>Product</th>
                            <th>Price</th>
                            <th>Quantity</th>
                            <th>Total</th>
                            <th></th>
                        </tr>
                    </thead>
                    <tbody>
                        <CartItem v-for="item in cart.items" 
                        v-bind:key="item.product.id" 
                        v-bind:initialItem="item"
                        v-on:removeFromCart="removeFromCart(item)"
                        v-bind:deleteOption="true"
                        />
                    </tbody>
                </table>
                <p v-else>You don't have any products in the cart yet...</p>
            </div>
            
            <div class="column is-12 box" v-if="cartTotalLength">
                <h2 class="subtitle">Summary</h2>
                <strong>$ {{ CartTotalPrice.toFixed(2) }}</strong>, {{ cartTotalLength }} items.
                <hr>
                <RouterLink to="/cart/checkout" class="button is-dark">Procced to Checkout</RouterLink>
            </div>

        </div>
    </div>
</template>


<script>
import CartItem from '@/components/CartItem.vue'
export default {
    name:'Cart',
    components:{
        CartItem
    },
    data(){
        return {
            cart:{
                items:[]
            }
        }
    },
    mounted(){
        this.cart = this.$store.state.cart
    },
    methods:{
        removeFromCart(item){
            this.cart.items = this.cart.items.filter(i=>i.product.id !==item.product.id)
            localStorage.setItem('cart',JSON.stringify(this.cart.items))
        }
    },
    computed:{
        cartTotalLength(){
            return this.cart.items.reduce((acc,curVal)=>{
                return acc+=curVal.quantity
            },0)
        },
        CartTotalPrice(){
            return this.cart.items.reduce((acc,curVal)=>{
                return acc += curVal.quantity * curVal.product.price
            },0)
        }
    }
}
</script>