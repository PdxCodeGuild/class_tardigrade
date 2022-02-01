const App = {
    data() {
        return {
            favQuote: '',
            Keyword: '',
            Tag: '',
            Author: '',
            randomQuote: '',
            foundQuotes: [],
            pageNumber: '',
            nextPageUrl: '',
            myFilter: '',
            message: 'Hello World!'
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
            }).then(response => { 
                this.randomQuote = response.data.quotes 
            })
        },
        searchKeyword() {
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes/?',
                headers: { 'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"' },
                params: { filter: this.Keyword },
            }).then(response => {
                console.log(response.data)
                this.foundQuotes = response.data.quotes
                this.pageNumber = response.data.page
                console.log(this.pageNumber)
            })
        },
        searchTag() {
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes/?',
                headers: { 'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"' },
                params: { filter: this.Tag },
            }).then(response => {
                console.log(response.data)
                this.foundQuotes = response.data.quotes
                this.pageNumber = response.data.page
            })
        },
        searchAuthor() {
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes/?',
                headers: { 'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"' },
                params: { filter: this.Author },
            }).then(response => {
                console.log(response.data)
                this.foundQuotes = response.data.quotes
                this.pageNumber = response.data.page
            })
        },
    }
}

Vue.createApp(App).mount('#app')