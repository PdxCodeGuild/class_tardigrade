const App = {
	data() {
		return {
            randomQuote: '',
			quotes: [],
            lastPage: true,
            authorPage: 1,
            keywordPage: 1,
            tagPage: 1,
            tag: '', // User Input for Tag Search
            author: '', // User Input for Author Search
			keyword: '', //User Input for Keyword
            type: '',
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
                console.log(response.data)
                this.randomQuote = response.data.quote.body
            })
        },

        getQuoteByKeyword() {
            this.type = 'keyword'
            axios({
                method: 'get',
                url: `https://favqs.com/api/quotes/`,
                headers: {Accept: 'application/json', Authorization: 'Token token="855df50978dc9afd6bf86579913c9f8b"'},
                params: { filter: this.keyword, page: 1 }
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
                params: { filter: this.tag, type: 'tag', page: 1 }
            })
            .then(response => {
                // console.log(response.data.last_page)
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
                params: { filter: this.author, type: 'author', page: 1 }
            })
            .then(response => {
                // console.log(response.data)
                this.lastPage = response.data.last_page
                this.quotes = response.data.quotes
            })
        },

                        // Use Template literal to compare type & tag

        nextPage() {
            let myParams = {}
            if (this.type === 'tag') {
                myParams = { filter: this.tag, type: this.type, page: this.tagPage +=1 }
            }

            else if (this.type === 'author') {
                myParams = { filter: this.author, type: this.type, page: this.authorPage +=1 }
            }

            else if (this.type === 'keyword') {
                myParams = { filter: this.keyword, type: this.type, page: this.keywordPage +=1 }
            }

                axios({
                    method: 'get',
                    url: `https://favqs.com/api/quotes/`,
                    headers: {Accept: 'application/json', Authorization: 'Token token="855df50978dc9afd6bf86579913c9f8b"'},
                    params: myParams
                })
                .then(response => {
                    this.quotes = response.data.quotes
                    this.lastPage = response.data.last_page
                })
        }
    }
}

Vue.createApp(App).mount('#app')