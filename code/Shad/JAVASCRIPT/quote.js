
const axiosInstance = axios.create({
    baseURL: 'https://favqs.com/api/',
    headers: {
        'Accept': 'application/json',
        'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'
    }
})


const App = {
    data() {
        return {
            term: '',
            // QUOTES: '',
            quotes: [],
        }
    },
    async mounted() {
        let data = await this.getQuotes()
        console.log(data.page)
        console.log(data.last_page)
        console.log(data.quotes)
        this.quotes = data.quotes
    },
    methods: {
        getQuotes() { // part 2 from the python lab
            return axiosInstance.get('quotes/').then(response => response.data)
        }
	}
}

Vue.createApp(App).mount('#app')

























// data() {
//     return {
//       posts: [],
//     };
//   },

//   methods: {
//     async getData() {
//       try {
//         let response = await fetch("http://jsonplaceholder.typicode.com/posts");
//         this.posts = await response.json();;
//       } catch (error) {
//         console.log(error);
//       }
//     },
//   },

//   created() {
//     this.getData();
//   },
// };









// <script type="text/javascript">
    
//     var app = new Vue({
//       el: '#app',
//       methods: {
//           onClick() {
//               axios({
//                     url: 'http://localhost:8000/test.pdf',
//                     method: 'GET',
//                     responseType: 'blob',
//                 }).then((response) => {
//                      var fileURL = window.URL.createObjectURL(new Blob([response.data]));
//                      var fURL = document.createElement('a');
    
//                      fURL.href = fileURL;
//                      fURL.setAttribute('download', 'file.pdf');
//                      document.body.appendChild(fURL);
    
//                      fURL.click();
//                 });
//           }
//       }
//     })
   
// </script>














// Headers
// Content Type
// All data is sent and received as JSON.

// Content-Type: application/json
// This must be set in the request headers when the request body contains content.

// Status Codes
// There are three HTTP status codes that you need to check for: 200, 404, and 500.

// SUCCESS
// A successful request returns a 200 response and no error_code.

// VALIDATION ERRORS
// A request containing validation errors will return a 200 response (breaking from 4xx convention) as well as an error_code and message containing the reason (in English) for the validation error. A full list of error codes is available in the last section of this page if you would like to provide translations within your app.

// SUMMARY
// To recap, check for a 200 to see if the server received and understood your request. Then check for the presence of an error_code to make sure there were no validation errors on your request. If there were, a message will be present and can be shown to the user.

// Authorization
// An app token is required to access our API (except for the Quote of the Day).

// For authorized API calls, pass your access token in via the header:

// Authorization: Token token="YOUR_APP_TOKEN"
// For example,

// $ curl -H 'Authorization: Token token="YOUR_APP_TOKEN"'
// Note:  This format will not work:

// Authorization: "YOUR_APP_TOKEN"