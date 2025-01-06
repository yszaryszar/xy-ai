import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueDevTools from 'vite-plugin-vue-devtools'
import Inspector from 'vite-plugin-vue-inspector' // OR vite-plugin-vue-inspector

// https://vite.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    Inspector(),
    // vueDevTools(),
    vueDevTools({
      launchEditor: 'webstorm',
    }),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    },
  },
})
