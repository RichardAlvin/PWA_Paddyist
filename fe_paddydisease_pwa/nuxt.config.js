const AxiosInstance = {
  baseURL: process.env.BASE_URL,
  withCredentials: false,
  retry: true,
  headers: {
    Accept: 'application/json',
    'Content-Type': 'application/json',
  },
}

export default {
  ssr: false,
  target: 'static',
  env: {
    BASE_URL: process.env.BASE_URL,
    API_URL: process.env.API_URL,
    GTAG_ID: process.env.GTAG_ID,
  },

  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    title: 'Paddyist',
    htmlAttrs: {
      lang: 'en',
    },
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' },
      { name: 'format-detection', content: 'telephone=no' },
    ],
    link: [{ rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }],
  },

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: ['~/assets/stylesheets/main.scss'],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [{ src: './plugins/vue-slick.js' }, { src: './plugins/helpers.js' }, { src: '@/plugins/bootstrap-vue'}],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [
    // https://go.nuxtjs.dev/eslint
    '@nuxtjs/eslint-module',
    '@nuxtjs/style-resources',
    '@nuxtjs/pwa',
  ],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    // https://go.nuxtjs.dev/axios
    '@nuxtjs/axios',
    '@nuxtjs/gtm',
    'nuxt-lazy-load',
  ],

  // Axios module configuration (https://go.nuxtjs.dev/config-axios)
  axios: {
    proxy: true,
    AxiosInstance,
  },

  privateRuntimeConfig: {
    axios: {
      baseURL: process.env.BASE_URL,
    },
  },

  proxy: {
    '/api': {
      target: process.env.API_URL,
      pathRewrite: { '^/api/': '' },
      changeOrigin: true,
      onProxyReq(request) {
        request.setHeader('origin', process.env.API_URL)
      },
    },
  },

  router: {
    middleware: ['redirection'],
  },

  pwa: {
    icon: {
      fileName: 'icon.png',
      size: [64, 120, 144, 152],
    },
    manifest: {
      name: 'Paddyist',
      short_name: 'Paddyist',
      lang: 'id',
      display: 'standalone',
    },
    workbox: {
      dev: false,
    },
  },

  styleResources: {
    scss: ['./assets/stylesheets/partials/_variables.scss'],
  },

  publicRuntimeConfig: {
    gtm: {
      id: process.env.GTAG_ID,
    },
  },

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {
    extend(config, ctx) {},
    postcss: {
      preset: {
        autoprefixer: {
          overrideBrowserslist: ['last 2 versions'],
        },
      },
    },
    optimizecss: true,
    splitChunks: {
      pages: true,
      vendor: true,
      commons: true,
      runtime: true,
      layouts: false,
    },
    optimization: {
      splitChunks: {
        minSize: 20000,
        maxSize: 500000,
      },
    },
  },
}
