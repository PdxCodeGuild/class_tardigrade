const App = {
    // delimiters: ['[[', ']]'],
    data () {
        return {
            message: 'Hello World!',
            type: '',
            authorSearch: '',
            tagsSearch: '',
            quote: [],
            filter: '',
            pages: '',
            nextPg: '',
            results: [],
        }
    },

    methods: {

        quotes() {
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes',
                headers: {
                    'Authorization': 'Token token="	855df50978dc9afd6bf86579913c9f8b"',
                }
            }).then(response => {
                this.quote = response.data.quotes
                console.log(response.data.quotes)
            })
        },

        type() {
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes',
                headers: {
                    'Authorization': 'Token token="	855df50978dc9afd6bf86579913c9f8b"',
                },
                params: {
                    filter: this.type,
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
                    'Authorization': 'Token token="	855df50978dc9afd6bf86579913c9f8b"',
                },
                params: {
                    filter: this.authorSearch,
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
                headers:  {
                    'Authorization': 'Token token="	855df50978dc9afd6bf86579913c9f8b"'
                },
                
            }).then(response => {
                this.results = response.data.quotes
                this.pages = response.data.page
            })
        },
//----------------------------------------------------------------------------"accept": "application/json",'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'
       


    },
    
    created() {
        this.quotes()
    }
}

Vue.createApp(App).mount('#app')