import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      '/api': 'http://127.0.0.1:5000',
      '/login': 'http://127.0.0.1:5000',
      '/signup': 'http://127.0.0.1:5000',
      '/logout': 'http://127.0.0.1:5000'
    }
  }
})
