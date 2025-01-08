// import './assets/main.css'
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import ElementPlus from 'element-plus'
import './index.css'
import 'element-plus/dist/index.css'
import App from './App.vue'
import router from './router'
import '@/assets/iconfont'
import SvgIcon from '@/components/SvgIcon.vue'

const app = createApp(App)
app.component('svg-icon', SvgIcon)

app.use(createPinia())
app.use(router)
app.use(ElementPlus)

app.mount('#app')
