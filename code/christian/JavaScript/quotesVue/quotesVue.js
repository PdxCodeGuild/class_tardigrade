const App = {
    data (){
        
        return {
            message: 'Quotes',
            keyWord: '',
            authorSearch: '',
            tagSearch: '',
            randomQuote: [],
            dataBase: [],
            nextPage: '',
            pageUrl: '',
            myFilter: '',


           }
    },
    methods: {
 
        getRandomQuote() {
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes/',
                // headers: {'Authorization: Token token="5510ab1b4e8a619951eeb35eb4025603"' },
                headers: { Authorization: `Token token="5510ab1b4e8a619951eeb35eb4025603"` },

            })
            .then(response => {
                console.log(response.data)
                this.randomQuote = response.data.quotes
                

            })
        },
        getWord(){
            axios({
                method: 'get',
                url: `https://favqs.com/api/quotes/?filter=${this.keyWord}`,
                headers: { Authorization: `Token token="5510ab1b4e8a619951eeb35eb4025603"` },
                params: { filter: this.keyWord },
            })
            .then(response => {
                console.log('!!!!',response.data)
                this.dataBase = response.data.quotes
                alert('heloooooo')
            })
        },
        getAuthor(){
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes',
                headers: { Authorization: `Token token="5510ab1b4e8a619951eeb35eb4025603"` },
                params: { filter: this.authorSearch },
            })
            .then(response => {
                console.log(response.data)
                this.dataBase = response.data.quotes
            })
        },
        getTag(){
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes',
                headers: { Authorization: `Token token="5510ab1b4e8a619951eeb35eb4025603"` },
                params: { filter: this.tagSearch },

            })
            .then(response => {
                console.log(response.data)
                this.dataBase = response.data.quotes
            })

        },
        changePage() {
            this.nextPage += 1
            if (this.getWord != '') {
                this.pageUrl = 'https://favqs.com/api/quotes'
                this.myFilter = this.getWord

            }
            else if(this.getTag != '') {
                this.pageUrl = 'https://favqs.com/api/quotes/?filter=filter&type=tag'
                this.myFilter = this.getTag
            }
            else if (this.getAuthor != '') {
                this.pageUrl = 'https://favqs.com/api/quotes/?filter=filter&type=author'
                this.myFilter = this.getAuthor
            }
            axios({
                methos: 'get',
                url: this.pageUrl,
                headers: { Authorization: `Token token="5510ab1b4e8a619951eeb35eb4025603"`},

                params: {
                    filter: this.myFilter,
                    page: this.nextPage
                },
                
            }).then(response => {
                this.dataBase = response.data.quotes
                this.nextPage = response.data.page

            })

        },
        backPage() {
            this.nextPage -= 1
            if (this.getWord != '') {
                this.pageUrl = 'https://favqs.com/api/quotes/?'
                this.myFilter = this.getWord
            }
            else if(this.getTag != '') {
                this.pageUrl = 'https://favqs.com/api/quotes/?filter=filter&type=tag'
                this.myFilter = this.getTag 
            }
            else if (this.getAuthor != '') {
                this.pageUrl = 'https://favqs.com/api/quotes/?filter=filter&type=author'
                this.myFilter = this.getAuthor 
            }
            axios({
                method: 'get',
                url: this.pageUrl,
                headers: { Authorization: `Token token="5510ab1b4e8a619951eeb35eb4025603"`},
                
                params: {
                    filter: this.myfilter,
                    page: this.nextPage
                },

            }).then(response => {
                this.dataBase = response.data.quotes
                this.nextPage = response.data.page
            })
        }
    },
    mounted() {
        this.getRandomQuote()
    },
}

Vue.createApp(App).mount('#app')