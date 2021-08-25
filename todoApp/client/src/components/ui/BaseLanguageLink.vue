<template>
  <li class="base-link">
    <!-- <h1>{{ nihongoMode }}</h1> -->
    <router-link :to="nihongoPathGet">{{ nihongoMode }}</router-link>
  </li>
</template>

<script>
import { computed, ref } from "vue";
export default {
  props: { mode: String, nihonPath: String },
  setup(props) {
    const nihongoPath = ref("/");
    const nihongoMode = computed(() => {
      return props.mode;
    });
    const nihongoPathGet = computed(() => {
      if (props.nihonPath === "hg") {
        return "/hiragana";
      }
      if (props.nihonPath === "kt") {
        return "/katakana";
      }
      if (props.nihonPath === "kj") {
        return "/kanji";
      }
      return "/";
    });
    return { nihongoMode, nihongoPath, nihongoPathGet };
  },
};
</script>

<style scoped sass>
h1 {
  color: #edf5e1;
}
li {
  display: inline-block;
  background: #05386b;
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 12px;
  box-shadow: 0 2px 8px #05386b7c;
  padding: 1rem;
  margin: 0 2rem;
  transition: 0.75s;
}

.base-link:hover {
  transform: scale(1.2);
  background: #379683;
  transition: 0.75s;
}

a {
  text-decoration: none;
  color: #edf5e1;
  font-size: 2rem;
  transition: 0.75s;
}
</style>
