const App = {
	data() {
		return {
            randomQuote: '',
			quotes: [],
            lastPage: true,
            page: 1,
            tag: '',
            author: '',
			keyword: '',
            term: '',
            type: ''
		}
    },

    created() {
        this.getRandomQuote()
    },

    methods: {
        
        getRandomQuote() {            
            axios({
                method: 'get',
                url: 'https://favqs.com/api/qotd',
                headers: {Accept: 'application/json'}
            })
            .then(response => {
                // console.log(response.data.quote)
                this.randomQuote = response.data.quote.body
            })
        },

        getQuoteByKeyword() {
            this.type = 'keyword'
            axios({
                method: 'get',
                url: `https://favqs.com/api/quotes/`,
                headers: {Accept: 'application/json', Authorization: 'Token token="855df50978dc9afd6bf86579913c9f8b"'},
                params: { filter: this.keyword }
            })
            .then(response => {
                console.log(response.data.last_page)
                this.lastPage = response.data.last_page
                this.quotes = response.data.quotes
            })
        },

        getQuoteByTag() {
            this.type = 'tag'
            axios({
                method: 'get',
                url: `https://favqs.com/api/quotes/`,
                headers: {Accept: 'application/json', Authorization: 'Token token="855df50978dc9afd6bf86579913c9f8b"'},
                params: { filter: this.tag, type: 'tag' }
            })
            .then(response => {
                console.log(response.data.last_page)
                this.lastPage = response.data.last_page
                this.quotes = response.data.quotes

            })
        },
        
        getQuoteByAuthor() {
            this.type = 'author'
            axios({
                method: 'get',
                url: `https://favqs.com/api/quotes/`,
                headers: {Accept: 'application/json', Authorization: 'Token token="855df50978dc9afd6bf86579913c9f8b"'},
                params: { filter: this.author, type: 'author' }
            })
            .then(response => {
                console.log(response.data)
                this.lastPage = response.data.last_page
                this.quotes = response.data.quotes
            })
        },

        nextPage() {
            axios({
                method: 'get',
                url: `https://favqs.com/api/quotes/`,
                headers: {Accept: 'application/json', Authorization: 'Token token="855df50978dc9afd6bf86579913c9f8b"'},
                params: { filter: this.keyword, type: this.type, page: this.page +=1 }
            })
            .then(response => {
                this.quotes = response.data.quotes
                this.lastPage = response.data.last_page
            })
        }
    }
}

Vue.createApp(App).mount('#app')