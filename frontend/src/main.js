import * as Vue from 'vue'
import App from './App.vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
import PrimeVue from 'primevue/config';

const app = Vue.createApp(App)
app.use(VueAxios, axios)
app.provide('axios', app.config.globalProperties.axios) 
app.use(PrimeVue)

app.mount('#app')
