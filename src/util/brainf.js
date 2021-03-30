import store from '../store'

export function loadPyodide() {
  console.log('Loading Python...');
  // eslint-disable-next-line no-undef
  globalThis.languagePluginLoader.
      then(() => importPythonLibrary()).
      catch(() => {
        alert("Rapidly refreshing this page can cause memory issues, please open the visualiser in a new tab.")
      })
}

function importPythonLibrary() {
  fetch('./brainf.py').
      then(res => res.text()).
      then(data => evaluatePython(data));
}

export function evaluatePython(code) {
  // eslint-disable-next-line no-undef
  pyodide.runPythonAsync(code).
      then(output => addToOutput(output)).
      catch((err) => {
        addToOutput(err);
      });
}

function addToOutput(s) {
  store.commit("setOutput", s);
}