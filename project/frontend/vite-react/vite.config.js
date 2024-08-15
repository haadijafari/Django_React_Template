import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  build: {
    // generate manifest.json in outDir
    manifest: true,
    rollupOptions: {
      // overwrite default .html entry
      // input: '/path/to/main.js'

      // Set deterministic output names
      output: {
        assetFileNames: (assetInfo) => {
          if (assetInfo.name === 'style.css') {
            // For CSS files
            return 'assets/css/index.min.css';
          }
          // Default behavior for other assets
          return 'assets/[ext]/[name].[ext]';
        },
        entryFileNames: (chunkInfo) => {
          // For JavaScript entry files
          return `assets/js/${chunkInfo.name}.min.js`;
        },
        chunkFileNames: (chunkInfo) => {
          // For additional chunks
          return `assets/js/${chunkInfo.name}.chunk.js`;
        }
      }
    }
  }
});
