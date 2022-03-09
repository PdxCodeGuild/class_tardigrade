const App = {
	data () {
		return {
			todos: [
				{
					text: 'Eat',
					completed: true
				},
				{
					text: 'Sleep',
					completed: false
				}
			],
			newTodo: '',
		}
	},
	computed: { 
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

