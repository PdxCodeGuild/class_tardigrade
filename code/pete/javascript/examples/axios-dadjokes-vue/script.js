const App = {
	data() {
		return {
			term: '',
			randomJoke: '',
			jokes: [],
		}
	},
	created() { // the created hook is a method that runs automatically when the page is first loaded
		this.getRandomJoke()
	},
	methods: {
		getRandomJoke() { // part 1 from the python lab
			axios({
				method: 'get',
				url: 'https://icanhazdadjoke.com',
				headers: { Accept: 'application/json' }
			})
			.then(response => { // arrow function response is the parameter, what comes after the arrow is the body of the function
				console.log(response.data) //[Log] {id: "kqcFBlGJYDd", joke: "You know what they say about cliffhangers...", status: 200}
				this.randomJoke = response.data.joke 
				console.log(this)
			})
			// alert('i am the line after the .then of the promise')
		},

		getJokes() { // part 2 from the python lab
			axios({
				method: 'get',
				url: 'https://icanhazdadjoke.com/search',
				headers: { Accept: 'application/json' },
				params: { term: this.term }
			})
			.then(response => { // arrow function response is the parameter, what comes after the arrow is the body of the function
				console.log(response.data)
				this.jokes = response.data.results
			})
			// alert('i am the line after the .then of the promise')
		}
	}
}

Vue.createApp(App).mount('#app')