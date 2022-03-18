

//    Authorization: Token token="15bcef41b1ec53efab73ce5f67267269"

const authToken = "15bcef41b1ec53efab73ce5f67267269"


console.log("test")



Vue.createApp({

  data() {
    return {
      response: {},
      quotesData: [],
      quoteList: [],
      paginationArray: [],

      searchText: "",

      qotdQuote: {},
      qotdAuthor: {},
      keywordSearch: "",

      searchList: [],
      responseSearch: {},
      quoteSearch: [],
      searchData: [],

      selected: "",

      lastPage: false,
      quotesPage: "",
      pageCount: 1,
      pageNum: 1,
      setPageNum: 1,
      quotesLength: 0,
      searchEntry: ""
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

      for (let i = 0; i < 1; i++) {

        //adds quote and author name to list
        this.quoteList.push({ name: this.quotesData[i].author, quote: this.quotesData[i].body })

      }
    },


    //Searches API
    searchQuotes(setPageNum) {


      // Search for quotes containing the word "funny":
      // GET https://favqs.com/api/quotes/?filter=funny
      if (this.selected == "Keyword") {

        this.searchEntry= this.searchText
      }


      // Get quotes by Mark Twain:        
      // GET https://favqs.com/api/quotes/?filter=Mark+Twain&type=author

      else if (this.selected == "Author") {
        this.searchEntry = this.searchText + "&type=author"

      }


      // Get quotes that are tagged with "funny":        
      // GET https://favqs.com/api/quotes/?filter=funny&type=tag

      else if (this.selected == "Tag") {
        this.searchEntry = this.searchText + "&type=tag"

      }

      axios
        .get(`https://favqs.com/api/quotes/?filter=${this.searchEntry}&page=${setPageNum}`, {
          headers: {
            Authorization: "Token 15bcef41b1ec53efab73ce5f67267269"
          }
        })
        .then(responseSearch => (this.responseSearch = responseSearch,
          this.searchData = responseSearch.data.quotes,
          
          //pagation test
          this.lastPage = responseSearch.data.last_page,
          this.quotesPage = responseSearch.data.page,
          this.quotesLength = responseSearch.data.quotes.length   


        )).finally(() => {
          console.log(this.responseSearch)
          this.searchDisplay()

          if (this.pageCount === 1){

            this.numPages()

          }

  
        })
    },




  numPages() {

    

    if (this.lastPage === true){
      
      this.pageNum = 0

    //  console.log("last page check: " + this.lastPage)
      this.pagination(this.pageCount)

    }

    else if(this.pageCount > 50){

     // console.log("pagecount > 10")

    }

   // else if(this.quotesLength < 25){

    //  console.log("no Quotes")
  // }

    else if (this.lastPage === false){

    //  console.log("Not last page")

    axios
    .get(`https://favqs.com/api/quotes/?filter=${this.searchEntry}&page=${this.pageCount}`, {
      headers: {
        Authorization: "Token 15bcef41b1ec53efab73ce5f67267269"
      }
    })
    .then(responseLastPage => (this.lastPage = responseLastPage.data.last_page,
      
      this.quotesPage = responseLastPage.data.page
     // this.quotesLength = response.data.quotes.length     
    )
      
    ).finally(() =>{
      

      this.pageCount += 1
      this.numPages()

    })   


}


  },

    //pagination
    pagination(pageCount){

      this.paginationArray = []

      for (let i = 1; i < pageCount; i++){

        this.paginationArray.push({pageNum: i, })

      }
      


    },

  //waits for axios response and then displays results
  searchDisplay() {

    this.searchList = []

    let len = this.searchData.length

    for (let i = 0; i < len; i++) {


      //adds quote and author name to list
      this.searchList.push({ name: this.searchData[i].author, quote: this.searchData[i].body })

    }

  },




  }

}).mount('#app')