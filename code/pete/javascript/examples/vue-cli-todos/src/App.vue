<template>
  <div>
    <h1>Todos</h1>
    <ul>
      <Todo
        v-for="todo, i in todos"
        :key="i"
        :todo="todo"
      />
    </ul>
  </div>
</template>

<script>
import Todo from './components/Todo.vue'
export default {
  name: 'App',
  components: {
    Todo
  },
  data () {
    return {
      todos: [
        {text: 'wash the car', completed: false},
        {text: 'walk the dog', completed: false},
        {text: 'butter the cat', completed: false},
      ]
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
