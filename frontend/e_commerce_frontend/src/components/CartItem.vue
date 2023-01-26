<template>
    <tr>
        <td><RouterLink v-bind:to="item.product.get_relative_url">{{ item.product.title }}</RouterLink></td>
        <td>${{ item.product.price }}</td>
        <td>
            {{ item.quantity }}
            <a v-if="deleteOption" @click="decrementItem(item)">-</a>
            <a v-if="deleteOption" @click="incrementItem(item)">+</a>
        </td>
        <td>$ {{ itemTotalPrice(item).toFixed(2) }}</td>
        <td v-if="deleteOption"><button class="delete"  @click="removeFromCart(item)"></button></td>
    </tr>
</template>

<script>

export default {
    name:'CartItem',
    props:{
        initialItem:Object,
        deleteOption: Boolean,
    },
    data(){
        return {
            item:this.initialItem,
            deleteOption: this.deleteOption
        }
    },
    methods:{
        removeItem(item){
            this.$emit('removeFromCart',item)
        },
        itemTotalPrice(item){
            return item.quantity * item.product.price   
        },
        decrementItem(item){
            item.quantity -=1
            if (item.quantity === 0){
                this.removeFromCart(item)
            }
            this.updateCart()
        },
        incrementItem(item){
            item.quantity += 1
            this.updateCart()
        },
        updateCart(){
            localStorage.setItem('cart',JSON.stringify(this.$store.state.cart))
        },
        removeFromCart(item){
            this.$emit('removeFromCart',item)
        }
    },
    computed:{
    }
}
</script>