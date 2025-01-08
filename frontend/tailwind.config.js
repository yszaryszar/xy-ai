/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  theme: {
    extend: {
      colors: {
        primary: '#009A61',
        secondary: '#00C77A',
        backgroundLight: '#F4F7FA',
        backgroundDark: '#1E2B26',
        textPrimary: '#1A1A1A',
        textSecondary: '#606266',
        error: '#F56C6C',
        success: '#67C23A',
        borderColor: '#D9D9D9',
        buttonHoverLight: '#E6F8F2',
      },
      boxShadow: {
        card: '0px 4px 12px rgba(0, 0, 0, 0.1)',
      },
      backgroundImage: {
        'gradient-primary': 'linear-gradient(to right, #009A61, #00C77A)',
      },
    },
  },
  plugins: ['prettier-plugin-tailwindcss'],
}
