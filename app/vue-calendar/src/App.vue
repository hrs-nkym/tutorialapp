<template>
  <body>
    <div id="app">
      <Header />
      <router-view />
      <Footer />
    </div>
  </body>
</template>

<script>
import Header from "./components/Header.vue";
import Footer from "./components/Footer.vue";
export default {
  components: {
    Header,
    Footer,
  },
};
</script>

<style>
* {
  margin: 0;
  padding: 0;
}
#app {
  text-align: center;
  color: #2c3e50;
}
</style>
