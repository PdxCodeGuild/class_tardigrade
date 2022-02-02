const App = {
    data() {
        return {
            message: 'Enter your to do list here:',
            itemsToDo: [],
            newItem: ''
        }


    },
    methods: {
     
        buttonClick () {
            
            this.itemsToDo.push(this.newItem)
            this.newItem = ''
            
        }


    }

}


Vue.createApp(App).mount('#app')

