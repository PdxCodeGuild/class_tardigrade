const App = {
    data() {
        return {
            message: 'hello',
            randomQuote: '',
            quote: []

           
        }

    },
    methods: {
        getRandomJoke() { 
			axios({
				method: 'get',
				url: 'https://favqs.com/api/qotd',
				headers: { Accept: 'application/json' }
			})
			.then(response => { 
				console.log(response.data) 
				this.randomJoke = response.data.joke 
				console.log(this)
			})
			
		}
    },
}


Vue.createApp(App).mount('#app')

// empty git folder fixing