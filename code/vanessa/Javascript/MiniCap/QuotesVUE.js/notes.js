const App = {
    data () {
        return {
            message: 'Hello',
            type: '',
            authorSearch: '',
            tagsSearch: '',
            quote: '',
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
                    'Authorization': 'Token token="881fdd4c7756328328ec3545c4508c6a"',
                }
            }).then(response => {
                this.quote = response.data.quotes
            })
        },

        type() {
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes',
                headers: {
                    'Authorization': 'Token token="881fdd4c7756328328ec3545c4508c6a"',
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
                    'Authorization': 'Token token="881fdd4c7756328328ec3545c4508c6a"',
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
                // headers: {
                //     'Authorization': 'Token token="881fdd4c7756328328ec3545c4508c6a"',
                // },
                headers = {
                    'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'
                },
                
            }).then(response => {
                this.results = response.data.quotes
                this.pages = response.data.page
            })
        },
//----------------------------------------------------------------------------
       


    },
    
    created() {
        this.quotes()
    }
}

Vue.createApp(App).mount('#app')