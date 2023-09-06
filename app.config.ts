export default defineAppConfig({
  alpine: {
    title: 'Parch Linux Blog',
    description: 'Parch Linux Blog | Parch Linux is an open-source, Arch-based Linux distribution, that tried to be pretty, easy to use, light, fast and stable.',
    image: '/img/logo.png',
    header: {
      position: 'left', // possible value are : | 'left' | 'center' | 'right'
      logo: false,
    },
    footer: {
      credits: {
        enabled: false, // possible value are : true | false
        repository: '' // our github repository
      },
      navigation: false, // possible value are : true | false
      alignment: 'center', // possible value are : 'none' | 'left' | 'center' | 'right'
      message: '© BSS OSF - All Rights Reserved.' // string that will be displayed in the footer (leave empty or delete to disable)
    },
    socials: {
      twitter: 'bssfoss',
      github: 'parchlinux',
      telegram: {
        icon: 'uil:telegram',
        label: 'Telegram',
        href: 'https://t.me/parchlinux'
      }
    },
    form: {
      successMessage: 'Message sent. Thank you!'
    }
  }
})
