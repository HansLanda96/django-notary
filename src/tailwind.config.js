/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'class', // or 'media' or 'class'
  content: [
    './templates/**/*.html',
    './templates/**/*.js',
    './templates/**/*.jsx',
    './node_modules/flowbite/**/*.js',
  ],
  theme: {

  },
  plugins: [
    require('flowbite/plugin'),
  ],
}
