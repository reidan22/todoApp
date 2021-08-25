import { createRouter, createWebHistory } from "vue-router";

import HiraganaPage from "./components/pages/HiraganaPage.vue";
import KatakanaPage from "./components/pages/KatakanaPage.vue";
import KanjiPage from "./components/pages/KanjiPage.vue";
import LessonChoose from "./components/pages/LessonChoose.vue";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: "/", redirect: "learn" },
    { path: "/learn", component: LessonChoose },
    { path: "/hiragana", component: HiraganaPage },
    { path: "/katakana", component: KatakanaPage },
    { path: "/kanji", component: KanjiPage },
  ],
});

export default router;
