<template>
  <ul>
    <base-language-link nihonPath="hg" mode="ひらがな"></base-language-link>
    <base-language-link nihonPath="kt" mode="カタカナ"></base-language-link>
    <!-- <base-language-link nihonPath="kj" mode="漢字"></base-language-link> -->
  </ul>
</template>

<script>
import BaseLanguageLink from "../ui/BaseLanguageLink.vue";

export default {
  components: {
    "base-language-link": BaseLanguageLink,
  },
};
</script>

<style scoped>
ul {
  list-style: none;
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 0;
  padding: 0;
}
</style>
