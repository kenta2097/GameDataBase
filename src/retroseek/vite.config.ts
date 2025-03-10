import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import path from 'path'

export default defineConfig({
  plugins: [react()],
  base: '/', // Asegúrate de que la base esté configurada correctamente para GitHub Pages
  build: {
    outDir: 'build', // Asegúrate de que el directorio de salida sea correcto
    rollupOptions: {
      input: {
        main: path.resolve(__dirname, 'index.html')
      },
      external: ['/main.tsx'] // Externaliza el módulo explícitamente
    }
  },
  server: {
    port: 5173,
    host: '0.0.0.0',
    open: true,
  },
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src')
    }
  }
})
