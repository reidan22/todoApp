<template>
  <h2>
    ひらがな
  </h2>
  <span>{{ apiResult }} {{ score }}</span>
  <h3>{{ generatedChoices.question }}</h3>
  <div class="choices">
    <h4
      @click="chooseGet(`A`)"
      :class="{
        choice: choicesState.A,
      }"
    >
      {{ generatedChoices.A }}
    </h4>
    <h4 @click="chooseGet(`B`)" :class="{ choice: choicesState.B }">
      {{ generatedChoices.B }}
    </h4>
    <h4 @click="chooseGet(`C`)" :class="{ choice: choicesState.C }">
      {{ generatedChoices.C }}
    </h4>
    <h4 @click="chooseGet(`D`)" :class="{ choice: choicesState.D }">
      {{ generatedChoices.D }}
    </h4>
  </div>
  <div @click="submitAnswer(choicesState)" v-if="timeBarWidth">
    <h5>Submit</h5>
  </div>
  <div @click="timeBar(3000)" v-else><h5>Start</h5></div>

  <div class="testTime" :style="{ width: timeBarWidth + `%` }"></div>
</template>

<script>
import axios from "axios";
import { ref } from "vue";
import wordBank from "../../HiraganaKatakana.json";

const apiURL = "http://localhost:5000/learn/1";
export default {
  mounted() {
    this.getAPIValue();
  },
  setup() {
    const apiResult = ref("");
    const choicesState = ref({
      A: false,
      B: false,
      C: false,
      D: false,
    });
    const generatedChoices = ref({
      A: null,
      B: null,
      C: null,
      D: null,
      question: null,
      correct: null,
      answer: null,
    });

    const score = ref(0);

    const timeBarWidth = ref(0);
    function resetChoices() {
      choicesState.value.A = false;
      choicesState.value.B = false;
      choicesState.value.C = false;
      choicesState.value.D = false;
    }

    const words = wordBank;
    const correctChoice = ref(null);
    function randCorrectChoice() {
      const letters = ["A", "B", "C", "D"];
      correctChoice.value = letters[Math.floor(Math.random() * 4)];

      const rand_a = Math.floor(Math.random() * Object.keys(words).length);
      const rand_b = Math.floor(Math.random() * Object.keys(words).length);
      const rand_c = Math.floor(Math.random() * Object.keys(words).length);
      const rand_d = Math.floor(Math.random() * Object.keys(words).length);
      generatedChoices.value.A = Object.keys(words)[rand_a];
      generatedChoices.value.B = Object.keys(words)[rand_b];
      generatedChoices.value.C = Object.keys(words)[rand_c];
      generatedChoices.value.D = Object.keys(words)[rand_d];
      generatedChoices.value.correct = correctChoice.value;

      const question_char = generatedChoices.value[correctChoice.value];
      generatedChoices.value.question = words[question_char][0]["hg"];
    }
    function generateChoices() {}

    function timeBar(tm) {
      resetChoices();
      randCorrectChoice();

      var setIntName = setInterval(() => {
        timeBarWidth.value += tm / 100 / 100;
        if (timeBarWidth.value > 100) {
          timeBarWidth.value = 100;
          clearInterval(setIntName);
          resetChoices();
          generatedChoices.value.A = null;
          generatedChoices.value.B = null;
          generatedChoices.value.C = null;
          generatedChoices.value.D = null;
          generatedChoices.value.question = null;
          generatedChoices.value.answer = null;
          generatedChoices.value.correct = null;
          timeBarWidth.value = 0;
        }
      }, tm / 100);
    }

    function submitAnswer(choices) {
      timeBarWidth.value = 0;
      Object.keys(choices).forEach((key) => {
        if (choices[key]) {
          generatedChoices.value.answer = key;
          //   console.log("Your answer is " + generatedChoices.value.answer);
          //   console.log("Correct answer is " + generatedChoices.value.correct);

          if (
            generatedChoices.value.answer === generatedChoices.value.correct
          ) {
            score.value += 1;
          } else {
            score.value -= 2;
          }
          randCorrectChoice();
          resetChoices();
        }
      });
    }

    function chooseGet(opt) {
      resetChoices();

      if (opt === "A") {
        choicesState.value.A = true;
      }
      if (opt === "B") {
        choicesState.value.B = true;
      }
      if (opt === "C") {
        choicesState.value.C = true;
      }
      if (opt === "D") {
        choicesState.value.D = true;
      }
    }

    function getAPIValue() {
      axios.get(apiURL).then((response) => {
        apiResult.value = response.data.fname;
      });
    }
    return {
      choicesState,
      chooseGet,
      timeBar,
      timeBarWidth,
      submitAnswer,
      correctChoice,
      randCorrectChoice,
      generatedChoices,
      generateChoices,
      score,
      apiResult,
      getAPIValue,
    };
  },
};
</script>

<style scoped>
* {
  display: flex;
  justify-content: center;
  align-items: center;
}

h2 {
}

h3 {
  background: #379683;
  height: 5rem;
  color: #edf5e1;
  font-size: 3rem;
  border-radius: 12px;
  box-shadow: 0 2px 8px #05386b7c;
  transition: 0.75s;
}

h4 {
  background: #379683;
  color: #edf5e1;
  display: inline-flex;
  border-radius: 50%;
  margin: 1rem 2rem;
  width: 3rem;
  height: 3rem;
  transition: 0.25s;
}

h4:hover,
h5:hover {
  background: #256e60;
  transform: scale(1.1);
}

.correct,
.correct:hover {
  background: #469134;
}

.choice-wrong,
.choice-wrong:hover {
  background: #da6f61;
}

.choice {
  background: #256e60;
}

h5 {
  background: #379683;
  color: #edf5e1;
  width: 20%;
  border-radius: 12px;
  box-shadow: 0 2px 8px #05386b7c;
  transition: 0.75s;
}

.testTime {
  background: #256e60;
  height: 1rem;
  width: 0%;
  margin: 0.5rem;
  border-radius: 12px;
  box-shadow: 0 2px 8px #05386b7c;
}
</style>
