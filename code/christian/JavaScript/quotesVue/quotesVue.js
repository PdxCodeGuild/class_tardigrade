const App = {
    data (){
        
        return {
            message: 'Quotes',
            keyWord: '',
            authorSearch: '',
            Tagsearch: '',
            randomQuote: '',
            ether: []

           }
    },
    created() {
        this.getRandomQuote()
        
    },
    methods: {

        getRandomQuote() {
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes/',
                // headers: {'Authorization: Token token="5510ab1b4e8a619951eeb35eb4025603"' },
                headers: { Authorization: `Token token="5510ab1b4e8a619951eeb35eb4025603"` }

            })
            .then(response => {
                console.log(response)
                this.randomQuote = response.data
                console.log(this.randomQuote)

            })
        },
        getWord(){
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes',
                headers: {'Authorization': 'Token token= "5510ab1b4e8a619951eeb35eb4025603"' },
                params: { filter: this.keyWord },
            })
            .then(response => {
                console.log(response.data)
                this.ether = response.data.quotes
            })
        },
        getAuthor(){
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes',
                headers: {'Authorization': 'Token token= "5510ab1b4e8a619951eeb35eb4025603"' },
                params: { filter: this.authorSearch },
            })
            .then(response => {
                console.log(response.data)
                this.ether = response.data.quotes
            })
        },
        getTag(){
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes',
                headers: {'Authorization': 'Token token= "5510ab1b4e8a619951eeb35eb4025603"' },
                params: { filter: this.Tagsearch },

            })
            .then(response => {
                console.log(response.data)
                this.ether = response.data.quotes
            })

        }

    }
}

Vue.createApp(App).mount('#app')