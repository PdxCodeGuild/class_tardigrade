

//    Authorization: Token token="15bcef41b1ec53efab73ce5f67267269"

const authToken = "15bcef41b1ec53efab73ce5f67267269"


console.log("test")



Vue.createApp({

  data() {
    return {
      response: {},
      quotesData: [],
      quoteList: [],

      searchText: "",

      qotdQuote: {},
      qotdAuthor: {},
      keywordSearch: "",

      searchList:[],
      responseSearch: {},
      quoteSearch:[],
      searchData: [],

      selected: "",

    }
  },

  mounted() { // automatically runs on page load 
    axios
      .get('https://favqs.com/api/quotes/', {
        headers: {
          Authorization: "Token 15bcef41b1ec53efab73ce5f67267269"
        }
      })
      .then(response => (this.response = response.data,
        this.quotesData = response.data.quotes
      )),



      //Quote of the day
  axios
  .get('https://favqs.com/api/qotd', {
    headers: {
     
    }
  })
  .then(response1 => (this.qotdQuote = response1.data.quote.body,
    this.qotdAuthor = response1.data.quote.author
  ))
  console.log(this.qotd)
 
  },

  methods: {

    getQuotes() {
      console.log("start load")
      let len = this.quotesData.length

      for (let i = 0; i < 1; i++){
        

        //adds quote and author name to list
        this.quoteList.push({name: this.quotesData[i].author, quote: this.quotesData[i].body})

    }
    },


    searchQuotes(){



      console.log(this.selected)
      if(this.selected == "Keyword"){
      searchKeyword = this.searchText
        // Search for quotes containing the word "funny":
        // GET https://favqs.com/api/quotes/?filter=funny

        axios
      .get(`https://favqs.com/api/quotes/?filter=${searchKeyword}`, {
        headers: {
          Authorization: "Token 15bcef41b1ec53efab73ce5f67267269"
        }
      })
      .then(responseSearch => (this.responseSearch = responseSearch,
        this.searchData = responseSearch.data.quotes
      )).finally(() => {

        //delays first
       this.searchDisplay()
      
      })
    }
    

    //    console.log(this.searchData)


    //  let len = this.searchData.length

   //   for (let i = 0; i < len; i++){
        

        //adds quote and author name to list
    //    this.searchList.push({name: this.searchData[i].author, quote: this.searchData[i].body})


    //  }

        // Get quotes that are tagged with "funny":        
        // GET https://favqs.com/api/quotes/?filter=funny&type=tag

        // Get quotes by Mark Twain:        
        // GET https://favqs.com/api/quotes/?filter=Mark+Twain&type=author
      },

      //pagination
    numPages(){
  // quotesData[i].        

      },

      //waits for axios and then displays results
      searchDisplay(){

        this.searchList = []

        let len = this.searchData.length
  
        for (let i = 0; i < len; i++){
          
  
          //adds quote and author name to list
          this.searchList.push({name: this.searchData[i].author, quote: this.searchData[i].body})
  
        }











    }


    }

  



}).mount('#app')