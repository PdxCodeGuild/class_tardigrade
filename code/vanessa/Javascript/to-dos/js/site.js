const App = {
    data() {
        return {
            message: 'Enter your to do list here:',
            itemsToDo: [],
            newItem: '',
            itemsComplete: [],
            completedItem: ''
        }


    },
    methods: {
     
        buttonClick () {
            
            this.itemsToDo.push(this.newItem)
            this.newItem = ''
            
        },
        buttonComplete () {
            this.buttonComplete.push(itemsCompleted),
            this.completedItem = ''


        },
        buttonDelete () {
           //need to fill in.


    }

},


Vue.createApp(App).mount('#app')