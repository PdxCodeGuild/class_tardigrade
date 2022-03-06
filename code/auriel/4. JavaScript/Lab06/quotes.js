const App = {
    data () {
        return {
            message: 'Welcome To Quote Search',
            random: '',
            searchTerm: '',
            searchResults: [],
            pageCounter: 0,
        }
    },

    methods: {

        randomQuotes() {
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes',
                headers: {
                    'Authorization': 'Token token="881fdd4c7756328328ec3545c4508c6a"',
                }
            }).then(response => {
                this.random = response.data.quotes
            })
        },

        searchQuotes() {
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes',
                headers: {
                    'Authorization': 'Token token="881fdd4c7756328328ec3545c4508c6a"',
                },
                params: {
                    filter: this.searchTerm,
                    type: this.searchType,
                    page: this.pageCounter,
                },
            }).then(response => {
                this.searchResults = response.data.quotes
            })
        },
 

        nxtPage() {
            this.pageCounter++
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes/',
                headers: {
                    'Authorization': 'Token token="881fdd4c7756328328ec3545c4508c6a"',
                },
                params: {
                    filter: this.searchTerm,
                    type: this.searchType,
                    page: this.pageCounter,
                },
            }).then(response => {
                this.searchResults = response.data.quotes
            })
        },

        prevPage() {
            this.pageCounter--
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes/',
                headers: {
                    'Authorization': 'Token token="881fdd4c7756328328ec3545c4508c6a"',
                },
                params: {
                    filter: this.searchTerm,
                    type: this.searchType,
                    page: this.pageCounter,
                },
            }).then(response => {
                this.searchResults = response.data.quotes
            })
        },



    },
    
    created() {
        this.randomQuotes()
    }
}

Vue.createApp(App).mount('#app')