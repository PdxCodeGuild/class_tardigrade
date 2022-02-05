

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

      searchList: [],
      responseSearch: {},
      quoteSearch: [],
      searchData: [],

      selected: "",

      lastPage: false,
      quotesPage: "",

      pageCountTest: 0
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
    searchQuotes() {


      // Search for quotes containing the word "funny":
      // GET https://favqs.com/api/quotes/?filter=funny
      if (this.selected == "Keyword") {

        searchEntry= this.searchText
      }


      // Get quotes by Mark Twain:        
      // GET https://favqs.com/api/quotes/?filter=Mark+Twain&type=author

      else if (this.selected == "Author") {
        searchEntry = this.searchText + "&type=author"

      }


      // Get quotes that are tagged with "funny":        
      // GET https://favqs.com/api/quotes/?filter=funny&type=tag

      else if (this.selected == "Tag") {
        searchEntry = this.searchText + "&type=tag"

      }

      axios
        .get(`https://favqs.com/api/quotes/?filter=${searchEntry}`, {
          headers: {
            Authorization: "Token 15bcef41b1ec53efab73ce5f67267269"
          }
        })
        .then(responseSearch => (this.responseSearch = responseSearch,
          this.searchData = responseSearch.data.quotes,

          //pagation test
          this.lastPage = responseSearch.data.last_page,
          this.quotesPage = responseSearch.data.page

        )).finally(() => {

          this.searchDisplay()

          this.numPages()      



          

        })
    },


  //pagination
  numPages() {



    if(this.lastPage === true){
      console.log("test last page" + this.lastPage)





    // quotesData[i]. 
    // pageCount = 1
    // while(pageCount < 5){


    // axios
    // .get(`https://favqs.com/api/quotes/?page=${pageCount}`, {
    //   headers: {
    //     Authorization: "Token 15bcef41b1ec53efab73ce5f67267269"
    //   }
    // })
    // .then(responseLastPage => (this.lastPage = responseLastPage.data.last_page,
    //   this.quotesPage = responseLastPage.data.page
    // )).finally(() =>{
      
    //   console.log(" finally page num:" + this.quotesPage)
    //   console.log("finally last page:" + this.lastPage)
    //   pageCount += 1
    // })



    //console.log("page num:" + this.quotesPage)
  //  console.log("last page:" + this.lastPage)
 
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


  }

  }


}).mount('#app')