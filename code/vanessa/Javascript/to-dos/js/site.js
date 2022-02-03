const App = {
    data() {
        return {
            message: 'Enter your to do list here:',
            itemsToDo: [],
            newItem: '',
            itemsComplete: [],
            completedItem: '',
           
        }

    },
    methods: {
     
        buttonClick () {
            
            this.itemsToDo.push(this.newItem)
            this.newItem = ''
            
        },
        buttonDelete (item) {
           let index = this.itemsToDo.indexOf(item)
           this.itemsToDo.splice(index,1);
        },

        buttonComplete (item) {
            this.buttonDelete(item)
            console.log(item)

            this.itemsComplete.push(item)
            // console.log(cItem)
            // console.log(this.itemsComplete)
            // console.log(typeof(cItem))


        },
        buttonIncomplete (item) {
            this.itemsToDo.push(item)
            let index = this.itemsComplete.indexOf(item)
           this.itemsComplete.splice(index,1);
            
            // this.itemsComplete.push(item)
            // console.log(cItem)
            // console.log(this.itemsComplete)
            // console.log(typeof(cItem))


        },


    }

}


Vue.createApp(App).mount('#app')
// ttps://reactgo.com/vue-toggle-class/
