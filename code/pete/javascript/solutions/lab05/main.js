const App = {
	data () {
		return {
			todos: [
				{
					text: 'wash the car',
					completed: true
				},
				{
					text: 'butter the cat',
					completed: false
				}
			],
			newTodo: '',
		}
	},
	computed: { // computed properties are functions that return a value like the ones in the data object
		// the computed property function runs every time any data inside the function changes
		incompleteTodos () {
			return this.todos.filter(todo => todo.completed === false)
		},
		completedTodos () {
			return this.todos.filter(todo => todo.completed === true)
		}
	},
	methods: {
		addNewTodo () {
			this.todos.push({
				text: this.newTodo,
				completed: false
			})
			this.newTodo = ''
		},
		toggleComplete (todo) {
			// shorthand for toggling a boolean in JS
			todo.completed = !todo.completed
		},
		deleteTodo (todo) {
			console.log(todo)
			console.log(this.todos.indexOf(todo))
			const index = this.todos.indexOf(todo)
			this.todos.splice(index, 1)
		}
	}
}

const app = Vue.createApp(App)
app.mount('#app')