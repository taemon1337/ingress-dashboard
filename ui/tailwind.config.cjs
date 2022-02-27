module.exports = {
  content: ['./src/**/*.{html,js,svelte,ts}'],
  themes: [
    {
      mytheme: {
        "primary": "#67e8f9",
        "secondary": "#d1fae5",
        "accent": "#a5b4fc",
        "neutral": "#d6d3d1",
        "base-100": "#fecdd3",
        "info": "#cffafe",
        "success": "#86efac",
        "warning": "#fde68a",
        "error": "#db2777",
      },
    },
  ],
  theme: {
    container: {
      center: true,
    },
  },
  daisyui: {
    themes: ["mytheme"],
  },
  plugins: [
    require('@tailwindcss/typography'),
    require("daisyui")
  ],
}
