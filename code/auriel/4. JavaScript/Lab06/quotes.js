const App = {
    data () {
        return {
            message: 'Welcome To The Quote Search',
            searchKeywords: '',
            searchAuthors: '',
            searchTags: '',
            random: '',
            searchFilter: '',
            pages: '',
            searchResults: [],
            nextPage: ''
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

        searchKeyword() {
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes',
                headers: {
                    'Authorization': 'Token token="881fdd4c7756328328ec3545c4508c6a"',
                },
                params: {
                    filter: this.searchKeywords,
                },
            }).then(response => {
                this.searchResults = response.data.quotes
                this.pages = response.data.page
            })
        },

        searchAuthor() {
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes/?filter=filter&type=author',
                headers: {
                    'Authorization': 'Token token="881fdd4c7756328328ec3545c4508c6a"',
                },
                params: {
                    filter: this.searchAuthors,
                },
            }).then(response => {
                this.searchResults = response.data.quotes
                this.pages = response.data.page
            })
        },

        searchTag() {
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes/?filter=filter&type=tag',
                headers: {
                    'Authorization': 'Token token="881fdd4c7756328328ec3545c4508c6a"',
                },
                params: {
                    filter: this.searchTags,
                },
            }).then(response => {
                this.searchResults = response.data.quotes
                this.pages = response.data.page
            })
        },

        nxtPage() {
            this.pages += 1

            if (this.searchrKeywords != '') {
                this.nextPage = 'https://favqs.com/api/quotes/?'
                this.searchFilter = this.searchKeywords
            } 
            if (this.searchTags != '') {
                this.nextPage = 'https://favqs.com/api/quotes/?filter=filter&type=tag'
                this.searchFilter = this.searchTags
            }
            if (this.searchAuthors != '') {
                this.nextPage = 'https://favqs.com/api/quotes/?filter=filter&type=author'
                this.searchFilter = this.searchAuthors
            }

            axios({
                method: 'get',
                url: this.nextPage,
                headers: {
                    'Authorization': 'Token token="881fdd4c7756328328ec3545c4508c6a"',
                },
                params: {
                    filter: this.searchFilter,
                    page: this.pages
                },
            }).then(response => {
                this.searchResults = response.data.quotes
                this.pages = response.data.page

            })
        },

        prevPage() {
            this.pages -= 1

            if (this.searchrKeywords != '') {
                this.nextPage = 'https://favqs.com/api/quotes/?'
                this.searchFilter = this.searchKeywords
            } 
            if (this.searchTags != '') {
                this.nextPage = 'https://favqs.com/api/quotes/?filter=filter&type=tag'
                this.searchFilter = this.searchTags
            }
            if (this.searchAuthors != '') {
                this.nextPage = 'https://favqs.com/api/quotes/?filter=filter&type=author'
                this.searchFilter = this.searchAuthors
            }

            axios({
                method: 'get',
                url: this.nextPage,
                headers: {
                    'Authorization': 'Token token="881fdd4c7756328328ec3545c4508c6a"',
                },
                params: {
                    filter: this.searchFilter,
                    page: this.pages
                },
            }).then(response => {
                this.searchResults = response.data.quotes
                this.pages = response.data.page

            })
        }



    },
    
    created() {
        this.randomQuotes()
    }
}

Vue.createApp(App).mount('#app')