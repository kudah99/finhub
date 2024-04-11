/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */

module.exports = {
  content: [
    /**
     * HTML. Paths to Django template files that will contain Tailwind CSS classes.
     */

    /*  Templates within theme app (<tailwind_app_name>/templates), e.g. base.html. */
    "../templates/**/*.html",

    /*
     * Main templates directory of the project (BASE_DIR/templates).
     * Adjust the following line to match your project structure.
     */
    "../../templates/**/*.html",

    /*
     * Templates in other django apps (BASE_DIR/<any_app_name>/templates).
     * Adjust the following line to match your project structure.
     */
    "../../**/templates/**/*.html",

    "../../**/components/**/*.html",

    /**
     * JS: If you use Tailwind CSS in JavaScript, uncomment the following lines and make sure
     * patterns match your project structure.
     */
    /* JS 1: Ignore any JavaScript in node_modules folder. */
    // '!../../**/node_modules',
    /* JS 2: Process all JavaScript files in the project. */
    // '../../**/*.js',

    /**
     * Python: If you use Tailwind CSS classes in Python, uncomment the following line
     * and make sure the pattern below matches your project structure.
     */
    // '../../**/*.py'
  ],
  media: false,
  darkMode: "class",
  theme: {
    extend: {
      colors: {
        current: '#d0195b',
        primary: {
          50: "rgb(var(--color-primary-50) / <alpha-value>)",
          100: "rgb(var(--color-primary-100) / <alpha-value>)",
          200: "rgb(var(--color-primary-200) / <alpha-value>)",
          300: "rgb(var(--color-primary-300) / <alpha-value>)",
          400: "rgb(var(--color-primary-400) / <alpha-value>)",
          500: "#d0195b",
          600: "rgb(var(--color-primary-600) / <alpha-value>)",
          700: "rgb(var(--color-primary-700) / <alpha-value>)",
          800: "rgb(var(--color-primary-800) / <alpha-value>)",
          900: "rgb(var(--color-primary-900) / <alpha-value>)",
          950: "rgb(var(--color-primary-950) / <alpha-value>)",
        },
      },
      fontSize: {
        0: [0, 1],
        xxs: ["11px", "14px"],
      },
      fontFamily: {
        sans: ["Inter", "sans-serif"],
      },
      height: {
        9.5: "2.375rem",
      },
      minWidth: {
        sidebar: "18rem",
      },
      spacing: {
        68: "17rem",
        128: "32rem",
      },
      transitionProperty: {
        height: "height",
        width: "width",
      },
      width: {
        4.5: "1.125rem",
        9.5: "2.375rem",
        sidebar: "18rem",
      },
    },
  },
  variants: {
    extend: {
      borderColor: ["checked", "focus-within", "hover"],
      display: ["group-hover"],
      overflow: ["hover"],
      textColor: ["hover"],
    },
  },
  plugins: [require("@tailwindcss/typography")],
  safelist: [
    "md:border-0",
    "md:border-r",
    "md:w-48",
    {
      pattern: /gap-+/,
      variants: ["lg"],
    },
    {
      pattern: /w-(1\/2|1\/3|2\/3|1\/4|2\/4|3\/4|1\/5|2\/5|3\/5|4\/5)/,
      variants: ["lg"],
    },
  ],
};