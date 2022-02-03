

//    Authorization: Token token="15bcef41b1ec53efab73ce5f67267269"

const authToken = "15bcef41b1ec53efab73ce5f67267269"


console.log("test")



Vue.createApp({

  data() {
    return {
      response: {},

      quotesData: [],

      quoteList: []
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
      ))
 
  },

  methods: {

    getQuotes() {

      let len = this.quotesData.length

      for (let i = 0; i < 1; i++){
        

        //adds quote and author name to list
        this.quoteList.push({name: this.quotesData[i].author, quote: this.quotesData[i].body})

    }
    }

    }


  



}).mount('#app')