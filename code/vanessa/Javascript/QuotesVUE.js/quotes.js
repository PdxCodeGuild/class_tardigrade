const App = {

    data() {
        return {
            message: 'Hello World!',
            quotes: [],
            searchTypes: '',
            authorSearches: '',
            tagsSearches: '',
            filter: '',
            pages: 1,
            nextPg: '',
            prevPg: '',
            results: [],
        }
    },

    created() {
        this.rQuote()
    },
    methods: {

        rQuote() {
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes',
                //url will not work with end written as quotes. get access error. qotd works 
                headers: {
                    "Accept": "application/json",'Authorization': 'Token token="6e5ddc77bb286cc39e07c4ffcd0f0db8"'

                }
            }).then(response => {
                
                console.log(response, "this is it")
                this.quotes = response.data.quotes
                console.log("quote",response.data)
            
            })
        },

        searchType() {
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes',
                headers: {
                    "Accept": "application/json",
                    'Authorization': 'Token token="6e5ddc77bb286cc39e07c4ffcd0f0db8"',
                },
                params: {
                    filter: this.searchTypes, page: this.pages
                },
            }).then(response => {
                this.results = response.data.quotes
                this.pages = response.data.page
            })
        },

        authorSearch() {
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes',
                headers: {
                    "Accept": "application/json",
                    'Authorization': 'Token token="6e5ddc77bb286cc39e07c4ffcd0f0db8"',
                },
                params: {
                    filter: this.author, page: 1, type: 'author'
                },
            }).then(response => {
                this.results = response.data.quotes
                this.pages = response.data.page
            })
        },

        tagsSearch() {
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes',
                headers: {
                    "Accept": "application/json",
                    'Authorization': 'Token token="6e5ddc77bb286cc39e07c4ffcd0f0db8"',
                    params: {
                        filter: this.tag, page: 1, type: 'tag'
                    }
                },

            }).then(response => {
                this.results = response.data.quotes
                this.pages = response.data.page
            })
        },

    nextP() {
        this.pages += 1
        // alert("test")

        if (this.searchTypes != '') {
            this.nextPg = 'https://favqs.com/api/quotes/?'
            this.filter = this.searchTypes
        }
        else if (this.tagsSearches != '') {
            this.nextPg = 'https://favqs.com/api/quotes/?filter=filter&type=tag'
            this.filter = this.tagsSearches
        }
        else if (this.authorSearches != '') {
            this.nextPg = 'https://favqs.com/api/quotes/?filter=filter&type=author'
            this.filter = this.authorSearches
        }
        axios({
            method: 'get',
            url: this.nextPg,
            headers: {
                "Accept": "application/json",
                'Authorization': 'Token token="6e5ddc77bb286cc39e07c4ffcd0f0db8"',
            },
            params: {
                filter: this.filter,
                page: this.pages
            },

        }).then(response => {
            this.results = response.data.quotes
            this.pages = response.data.page
            console.log(response.data)

        })
    },

    previous() {
        this.pages -= 1

        if (this.searchTypes != '') {
            this.nextPg = 'https://favqs.com/api/quotes/?'
            this.filter = this.searchTypes
        }
        else if (this.tagsSearches != '') {
            this.nextPg = 'https://favqs.com/api/quotes/?filter=filter&type=tag'
            this.filter = this.tagsSearches
        }
        else if (this.authorSearches != '') {
            this.nextPg = 'https://favqs.com/api/quotes/?filter=filter&type=author'
            this.filter = this.authorSearches
        }

        axios({
            method: 'get',
            url: this.nextPg,
            headers: {
                "Accept": "application/json",
                'Authorization': 'Token token="6e5ddc77bb286cc39e07c4ffcd0f0db8"',
            },
            params: {
                filter: this.filter,
                page: this.pages
            },
        }).then(response => {
            this.results = response.data.quotes
            this.pages = response.data.page

        })
    }
}


}

Vue.createApp(App).mount('#app')