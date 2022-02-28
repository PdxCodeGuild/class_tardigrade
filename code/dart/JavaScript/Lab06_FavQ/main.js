const App = {
    data () {
        return {
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
                    'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"',
                }
            }).then(response => {
                this.random = response.data.quotes
            })
        },

        searchKeyword() {
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes',
                headers: {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'},
                params: { filter: this.searchKeywords, type: 'searchKeywords' },
            }).then(response => {
                this.searchResults = response.data.quotes
                this.pages = response.data.page
            })
        },

        searchAuthor() {
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes',
                headers: {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'},
                params: { filter: this.searchAuthors, type: 'searchAuthors' },
            }).then(response => {
                this.searchResults = response.data.quotes
                this.pages = response.data.page
            })
        },

        searchTag() {
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes',
                headers: {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'},
                params: { filter: this.searchTags, type: 'searchTags' },
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
            else if (this.searchTags != '') {
                this.nextPage = 'https://favqs.com/api/quotes/?filter=filter&type=tag'
                this.searchFilter = this.searchTags
            }
            else if (this.searchAuthors != '') {
                this.nextPage = 'https://favqs.com/api/quotes/?filter=filter&type=author'
                this.searchFilter = this.searchAuthors
            }

            axios({
                method: 'get',
                url: this.nextPage,
                headers: {
                    'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"',
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
            else if (this.searchTags != '') {
                this.nextPage = 'https://favqs.com/api/quotes/?filter=filter&type=tag'
                this.searchFilter = this.searchTags
            }
            else if (this.searchAuthors != '') {
                this.nextPage = 'https://favqs.com/api/quotes/?filter=filter&type=author'
                this.searchFilter = this.searchAuthors
            }

            axios({
                method: 'get',
                url: this.nextPage,
                headers: {
                    'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"',
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