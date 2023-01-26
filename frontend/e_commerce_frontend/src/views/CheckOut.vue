<template>
<div class="checkout-page">
    <div class="columns is-multiline">
        <div class="column is-12">
            <h2 class="title">Checkout</h2>
        </div>
        <div class="column is-12 box">

            <table class="table is-fullwidth">
                <thead>
                    <tr>
                        <th>Product</th>
                        <th>Quantity</th>
                        <th>Price</th>
                        <th>Total</th>
                    </tr>
                </thead>
                <tbody>
                    <CartItem v-for="item in cart.items" 
                              :key="item.product.id"
                              :initialItem="item"
                              :deleteOption="false"
                              />
                </tbody>
                <tfoot>
                    <tr>
                        <td>Total</td>
                        <td></td>
                        <td></td>
                        <td>$ {{ cartTotalPrice }}</td>
                    </tr>
                </tfoot>
            </table>
        </div>
        <div class="column is-12">
            <form @submit.prevent="saveShipping" class="box" id="shipping-form">
                <h1 class="title">Shipping Details</h1>
                <p class="is-size-7">All fields are required</p>
                <hr>
                <div class="columns is-multiline">
                    <div class="field column is-half">
                        <label for="first_name">First Name</label>
                        <div class="control">
                            <input type="text" class="input" id="first_name" v-model="first_name" required>
                        </div>
                    </div>
                    <div class="field column is-half">
                        <label for="last_name">Last Name</label>
                        <div class="control">
                            <input type="text" class="input" id="last_name" v-model="last_name" required>
                        </div>
                    </div>
                    <div class="field column is-half">
                        <label for="email">Email</label>
                        <div class="control">
                            <input type="email" class="input" id="email" v-model="email" required>
                        </div>
                    </div>
                    <div class="field column is-half">
                        <label for="address">address</label>
                        <div class="control">
                            <input type="text" class="input" id="address" v-model="address" required>
                        </div>
                    </div>
                    <div class="field column is-half">
                        <label for="zipcode">Zip Code</label>
                        <div class="control">
                            <input type="text" class="input" id="zipcode" v-model="zipcode" required>
                        </div>
                    </div>
                    <div class="field column is-half">
                        <label for="place">Place</label>
                        <div class="control">
                            <input type="text" class="input" id="place" v-model="place" required>
                        </div>
                    </div>
                    <div class="field column is-half">
                        <label for="phone">Phone number</label>
                        <div class="control">
                            <input type="text" class="input" id="phone" v-model="phone" required>
                        </div>
                    </div>
                </div>
                <div class="has-text-centered pt-4" v-if="errors.length">
                    <p class="has-text-danger is-size-6" v-for="error,index in errors" v-bind:key="index">{{ error }}</p>
                </div>
                <hr>
                <button class="button is-dark">Procced to payment</button>
            </form>
            <div class="columns is-multiline is-hidden box" id="shipping-details">
                <div class="column is-half">
                    <h1 class="subtitle">First Name: {{ first_name }}</h1>
                </div>
                <div class="column is-half">
                    <h1 class="subtitle">Last Name: {{ last_name }}</h1>
                </div>
                <div class="column is-half">
                    <h1 class="subtitle">Email: {{ email }}</h1>
                </div>
                <div class="column is-half">
                    <h1 class="subtitle">Address: {{ address }}</h1>
                </div>
                <div class="column is-half">
                    <h1 class="subtitle">Place: {{ place }}</h1>
                </div>
                <div class="column is-half">
                    <h1 class="subtitle">Zip Code: {{ zipcode }}</h1>
                </div>
                <div class="column is-half">
                    <h1 class="subtitle">Phone Number: {{ phone }}</h1>
                </div>
                <div class="buttons column is-12 is-hidden" id="payment-choice" v-if="!useStripe && !usePaymob">
                    <a class="button is-primary" @click="payWithStripe">
                        Pay using Stripe
                    </a>
                    <a class="button is-primary" @click="paymobHandler">
                        Pay using Paymob
                    </a>
                </div>
            </div>
            
            <form @submit.prevent="submitForm" class="box columns" :style="{'height: 700px;':usePaymob}" :class="{'is-hidden':!useStripe && !usePaymob}">
                <div id="card-element" class="mb-5 columns column is-fullwidth"></div>
                <hr>
                <button class="button is-dark" @click="submitForm" :class="{'is-hidden':!useStripe}">Pay with Stripe</button>
            </form>
        </div>
    </div>
</div>
</template>
<script>
import CartItem from '@/components/CartItem.vue';
import axios from 'axios';

export default {
    name: 'Checkout',
    data() {
        return {
            cart: {
                items: []
            },
            useStripe:false,
            usePaymob:false,
            stripe: {},
            paymobToken:'',
            card: {},
            first_name: '',
            last_name: '',
            email: '',
            phone: '',
            address: '',
            zipcode: '',
            place: '',
            errors: []
        }
    },
    components:{
        CartItem
    },
    mounted() {
        document.title = 'Checkout'
        this.cart = this.$store.state.cart
    },
    methods: {
        saveShipping(){
            document.querySelector('#shipping-form').classList.toggle('is-hidden')
            document.querySelector('#shipping-details').classList.toggle('is-hidden')
            document.querySelector('#payment-choice').classList.toggle('is-hidden')
        },
        payWithStripe(){
            this.useStripe=true
            this.stripe = Stripe('pk_test_51MTY9CIsoTfkmXN4V0SZPZvKE6KcHfsbcGcKZ1yciQUB5CHHQsfyeVZqxfnxHSga6Fuu8RlD30rewbGLkM5JdUmy00cYsQz4br')
            const elements = this.stripe.elements();
            this.card = elements.create('card', { hidePostalCode: true })
            this.card.mount('#card-element')
        },
        payWithPaymob(){
            axios.get('/payWithPaymob/token')
                .then(response=>{
                    this.paymobToken = response.data.token
                    this.usePaymob = true
                    
                })
        },
        getItemTotal(item) {
            return item.quantity * item.product.price
        },
        submitForm() {
            if (this.payWithStripe){
            const buttons = document.querySelectorAll('button')
            const stripe_button = buttons[buttons.length-1]
            stripe_button.disabled = true
            this.errors = []
            if (!this.errors.length) {
                this.stripe.createToken(this.card).then(result => {                    
                    if (result.error) {
                        this.errors.push('Something went wrong with Stripe. Please try again')
                        console.log(result.error.message)
                        stripe_button.disabled = false
                    } else {
                        this.stripeTokenHandler(result.token)
                    }
                })
            }
        }
        },
        async paymobHandler(){
            this.usePaymob = true
            const items = []
            for (let i = 0; i < this.cart.items.length; i++) {
                const item = this.cart.items[i]
                const obj = {
                    product: item.product.id,
                    quantity: item.quantity,
                    price: item.product.price * item.quantity
                }
                items.push(obj)
            }
            const data = {
                'first_name': this.first_name,
                'last_name': this.last_name,
                'email': this.email,
                'address': this.address,
                'zipcode': this.zipcode,
                'place': this.place,
                'phone': this.phone,
                'items': items,
            }
            await axios.post('/pay/paymob/',data)
            .then(response=>{
                const token = response.data.token
                console.log(token)
                const frame = document.createElement('iframe')
                frame.src = `https://accept.paymob.com/api/acceptance/iframes/648418?payment_token=${token}`
                frame.classList.add('column','is-fullwidth')
                this.usePaymob = true
                document.querySelector('#card-element').appendChild(frame)
                document.querySelector('#card-element').style.height = '700px'
                this.cart.items = []
                this.$store.commit('clearCart')
            }).catch(error=>{
                console.log(error)
            })
        },
        async stripeTokenHandler(token) {
            const items = []
            for (let i = 0; i < this.cart.items.length; i++) {
                const item = this.cart.items[i]
                const obj = {
                    product: item.product.id,
                    quantity: item.quantity,
                    price: item.product.price * item.quantity
                }
                items.push(obj)
            }
            const data = {
                'first_name': this.first_name,
                'last_name': this.last_name,
                'email': this.email,
                'address': this.address,
                'zipcode': this.zipcode,
                'place': this.place,
                'phone': this.phone,
                'items': items,
                'stripe_token': token.id
            }
            await axios
                .post('/checkout/', data)
                .then(response => {
                    this.$store.commit('clearCart')
                    this.$router.push('/cart/success')
                })
                .catch(error => {
                    this.errors.push('Something went wrong. Please try again')
                    console.log(error)
                })
        }
    },
    computed: {
        cartTotalPrice() {
            return this.cart.items.reduce((acc, curVal) => {
                return acc += curVal.product.price * curVal.quantity
            }, 0)
        },
        cartTotalLength() {
            return this.cart.items.reduce((acc, curVal) => {
                return acc += curVal.quantity
            }, 0)
        }
    }
}
</script>