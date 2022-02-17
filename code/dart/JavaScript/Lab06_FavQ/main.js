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
                this.randomQuote = response.data.quote
            })
        },
        searchKeyword() {
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes/?',
                headers: { 'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"' },
                params: { filter: this.Keyword, type: 'keyword' },
            }).then(response => {
                this.foundQuotes = response.data.quotes
                this.pageNumber = response.data.page
            })
        },
        searchTag() {
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes/?',
                headers: { 'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"' },
                params: { filter: this.Tag, type: 'tag' },
            }).then(response => {
                this.foundQuotes = response.data.quotes
                this.pageNumber = response.data.page
            })
        },
        searchAuthor() {
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes/?',
                headers: { 'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"' },
                params: { filter: this.Author, type: 'author'},
            }).then(response => {
                this.foundQuotes = response.data.quotes
                this.pageNumber = response.data.page
            })
        },
        nextPage: function() {
            this.pageNumber += 1
            if (this.userKeyword != '') {
                this.nextPageUrl = 'https://favqs.com/api/quotes/?'
                this.myFilter = this.userKeyword
            } 
            else if (this.userTag != '') {
                this.nextPageUrl = 'https://favqs.com/api/quotes/?filter=filter&type=tag'
                this.myFilter = this.userTag
            }
            else if (this.userAuthor != '') {
                this.nextPageUrl = 'https://favqs.com/api/quotes/?filter=filter&type=author'
                this.myFilter = this.userAuthor
            }
            axios({
                method: 'get',
                url: this.nextPageUrl,
                headers: {
                    'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"',
                },
                params: {
                    filter: this.myFilter,
                    page: this.pageNumber
                },
            }).then(response => {
                this.foundQuotes = response.data.quotes
                this.pageNumber = response.data.page
            })
        },
        previousPage: function() {
            this.pageNumber -= 1
            if (this.userKeyword != '') {
                this.nextPageUrl = 'https://favqs.com/api/quotes/?'
                this.myFilter = this.userKeyword
            } 
            else if (this.userTag != '') {
                this.nextPageUrl = 'https://favqs.com/api/quotes/?filter=filter&type=tag'
                this.myFilter = this.userTag
            }
            else if (this.userAuthor != '') {
                this.nextPageUrl = 'https://favqs.com/api/quotes/?filter=filter&type=author'
                this.myFilter = this.userAuthor
            }
            axios({
                method: 'get',
                url: this.nextPageUrl,
                headers: {
                    'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"',
                },
                params: {
                    filter: this.myFilter,
                    page: this.pageNumber
                },
            }).then(response => {
                this.foundQuotes = response.data.quotes
                this.pageNumber = response.data.page
            })

        }

    },
}

Vue.createApp(App).mount('#app')