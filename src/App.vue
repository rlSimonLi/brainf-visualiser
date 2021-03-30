<template>
  <div id="app">
    <h1>Hello world!</h1>
    <div id="output">{{output}}</div>
  </div>
</template>
<script>
import {loadPyodide} from './util/brainf';

export default {
  name: 'App',
  components: {},
  mounted() {
    loadPyodide();
  },
  computed: {
    output() {
      return this.$store.getters.getOutput
    }
  }
};
</script>
<style src="./css/common.css"></style>
<style>
#output {
  border: 1px solid #000;
  padding: 30px;
}
</style>