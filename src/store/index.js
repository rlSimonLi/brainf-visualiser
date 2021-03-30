import Vue from 'vue';
import Vuex from "vuex";

Vue.use(Vuex);

const state = {
  output: ""
}

const mutations = {
  setOutput(state, payload) {
    state.output = payload
  }
}


const getters = {
  getOutput(state) {
    return state.output;
  }
}

export default new Vuex.Store({
  state,
  mutations,
  getters
})