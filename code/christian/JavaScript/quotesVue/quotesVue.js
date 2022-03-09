const App = {
    data (){
        return {
            message: 'Quotes',
            searchWord: '',
            randomQuote: '',
            quotes: []

           }
    },
    created() {
        this.getRandomQuote()
    },
    methods: {

        getRandomQuote() {
            axios({
                method: 'get',
                urls: 'https://favqs.com/api/quotes',
                headers: {Accept: 'application/json'}
            })
            .then(response => {
                this.randomQuote = response.data.quotes

            })
        },
        getQuote(){
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes',
                headers: {Accept: 'application/json'},
                params: { searchWord: this.searchWord} 
            })
            .then(response => {
                console.log(response.data)
                this.quotes = response.data.results
            })
        }
    }
}

Vue.createApp(App).mount('#app')