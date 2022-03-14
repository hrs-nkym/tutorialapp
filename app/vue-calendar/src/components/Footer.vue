<template>
  <footer>
    <ul>
      <li>
        <a href="https://github.com/hrs-nkym" target="_blank">Github</a>
      </li>
      <li>
        <a href="https://twitter.com/leafhub" target="_blank">Twitter</a>
      </li>
    </ul>
  </footer>
</template>

<script>
export default {
  name: "site-footer",
};
</script>

<style scoped>
footer {
  display: flex;
  position: absolute;
  bottom: 0;
  background: #000;
  width: 100%;
  color: #fff;
}
ul {
  list-style: none;
  display: flex;
}
li {
  padding: 0 10px;
  text-align: center;
}
a {
  color: #fff;
}
</style>
