<template>
  <the-header></the-header>
  <router-view></router-view>
</template>

<script>
import TheHeader from "./components/layout/TheHeader.vue";
document.title = "Learn 日本語";
export default {
  components: {
    "the-header": TheHeader,
  },
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap");

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

html {
  font-family: "Roboto", sans-serif;
  color: #05386b;
  font-size: 2vw;
}

body {
  margin: 0;
  background-color: #5cdb95;
  display: flex;
  justify-content: center;
  align-items: center;
}

.drop-shadow {
  
}
</style>
