const App = {
    data (){
        
        return {
            message: 'Quotes',
            keyWord: '',
            authorSearch: '',
            tagSearch: '',
            randomQuote: [],
            dataBase: [],
            nextPage: 1,
            pageUrl: '',
            myFilter: '',

            authorCheck: false,
            keyWordCheck: false,
            tagCheck: false,


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
      
            authorCheck = false
            tagCheck = false
            keyWordCheck = true
            axios({
                method: 'get',
                url: `https://favqs.com/api/quotes/?filter=${this.keyWord}`,
                headers: { Authorization: `Token token="5510ab1b4e8a619951eeb35eb4025603"` },
                params: { filter: this.keyWord, page: this.nextPage },
            })
            .then(response => {
                console.log('!!!!',response.data)
                this.dataBase = response.data.quotes
                // alert('heloooooo')
            })
        },
        getAuthor(){
            authorCheck = true
            tagCheck = false
            keyWordCheck = false
            axios({
                method: 'get',
                url: `https://favqs.com/api/quotes/?filter=${this.authorSearch}`,
                headers: { Authorization: `Token token="5510ab1b4e8a619951eeb35eb4025603"` },
                params: { filter: this.authorSearch, type: 'author', page: this.nextPage  },
            })
            .then(response => {
                console.log(response.data)
                this.dataBase = response.data.quotes
                
            })
        },
        getTag(){
            authorCheck = false
            tagCheck = true
            keyWordCheck = false
            axios({
                method: 'get',
                url: `https://favqs.com/api/quotes/?filter=${this.tagSearch}`,
                headers: { Authorization: `Token token="5510ab1b4e8a619951eeb35eb4025603"` },
                params: { filter: this.tagSearch, type: 'tag', page: this.nextPage },

            })
            .then(response => {
                console.log(response.data)
                this.dataBase = response.data.quotes
            })

        },
        addPage() {
            console.log(this.nextPage)
            this.nextPage += 1
            if (authorCheck == true){
                this.getAuthor()

            }
            else if (tagCheck == true){
                this.getTag()
            }
            else if (keyWordCheck == true){
                this.getWord()
            }


        },
        minusPage() {
            this.nextPage -= 1
            if (authorCheck == true){
                this.getAuthor()

            }
            else if (tagCheck == true){
                this.getTag()
            }
            else if (keyWordCheck == true){
                this.getWord()
            }
            
        },
        
        
    },
    mounted() {
        this.getRandomQuote()
    },
}

Vue.createApp(App).mount('#app')