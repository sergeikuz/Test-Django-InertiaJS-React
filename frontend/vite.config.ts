import { resolve }  from 'path';

module.exports = {
 plugins: [],
 root: resolve('src'),
 base: '/static/',
 server: {
   host: 'localhost',
   port: 3000,
   open: false,
   watch: {
     usePolling: true,
     disableGlobbing: false,
   },
 },
 resolve: {
   extensions: ['.js', '.json'],
 },
 build: {
   outDir: resolve('static/dist'),
   assetsDir: '',
   manifest: true,
   emptyOutDir: true,
   target: 'es2015',
   rollupOptions: {
     input: {
       main: resolve('src/main.js'),
     },
     output: {
       chunkFileNames: undefined,
     },
   },
 },
};