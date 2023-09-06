export default defineNuxtConfig({
  extends: '@nuxt-themes/alpine',
  app: {
    head: {
      titleTemplate: 'Parch Linux Blog',
      charset: 'utf-8',
      viewport: 'width=device-width, initial-scale=1',
      meta: [
        { name: 'application-name', content: 'Parch Linux Blog' },
        { name: 'twitter:title', content: 'Parch Linux Blog' },
        { property: 'og:site_name', content: 'Parch Linux Blog' },
        { property: 'og:title', content: 'Parch Linux Blog' },
        { name: 'description', content: 'Parch Linux is an open-source, Arch-based Linux distribution, that tried to be pretty, easy to use, light, fast and stable.' },
        { name: 'twitter:description', content: 'Parch Linux is an open-source, Arch-based Linux distribution, that tried to be pretty, easy to use, light, fast and stable.' },
        { property: 'og:description', content: 'Parch Linux is an open-source, Arch-based Linux distribution, that tried to be pretty, easy to use, light, fast and stable.' },
        { name: 'keywords', content: 'parch linux, parchlinux, parch, linux' },
        { property: 'og:image', content: 'https://blog.parchlinux.ir/img/logo.png' },
        { name: 'twitter:image', content: 'https://blog.parchlinux.ir/img/logo.png' },
        { property: 'og:type', content: 'website' },
        { property: 'og:url', content: 'https://blog.parchlinux.ir' },
        { name: 'google-site-verification', content: 'l9uMrT1nBJ_BEbB86DofFIMYcbQgbxE7PCKJOMZpVSI' },
      ],
      link: [
        { rel: 'apple-touch-icon', type: 'image/png', sizes: '180x180', href: '/img/apple-touch-icon.png' },
        { rel: 'icon', type: 'image/png', sizes: '32x32', href: '/img/favicon-32x32.png' },
        { rel: 'icon', type: 'image/png', sizes: '16x16', href: '/img/favicon-16x16.png' },
      ]
    }
  },
})
