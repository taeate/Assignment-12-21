module.exports = {
  module: "jit",
  prefix: 't-',
  content: ["./base/templates/*.{html,js}",
            "./accounts/templates/*.{html,js}",
            "./products/templates/**/*.{html,js}"],
  theme: {
    extend: {},
  },
  plugins: [],
}
