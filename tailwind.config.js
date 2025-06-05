/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './src/pages/**/*.{js,ts,jsx,tsx,mdx}',
    './src/components/**/*.{js,ts,jsx,tsx,mdx}',
    // './src/app/**/*.{js,ts,jsx,tsx,mdx}', // If using App Router
  ],
  theme: {
    extend: {
      colors: {
        'god-blue': {
          light: '#3b82f6', // Example light shade
          DEFAULT: '#1e3a8a', // Example default shade
          dark: '#1e293b',  // Example dark shade
        },
        'god-orange': {
          light: '#fb923c', // Example light shade
          DEFAULT: '#f97316', // Example default shade
          dark: '#ea580c',   // Example dark shade
        },
        'delhi-red': '#DC143C', // Crimson
        'india-green': '#138808',
        'saffron': '#FF9933',
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'], // Default sans-serif
        display: ['Poppins', 'Inter', 'system-ui', 'sans-serif'], // For headings
      },
      backgroundImage: {
        'gradient-radial': 'radial-gradient(var(--tw-gradient-stops))',
        'gradient-conic':
          'conic-gradient(from 180deg at 50% 50%, var(--tw-gradient-stops))',
      },
    },
  },
  plugins: [],
};