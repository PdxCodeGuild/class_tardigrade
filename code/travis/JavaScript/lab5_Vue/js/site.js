
Vue.createApp({

  data() {
    return {

      newTodo: "",
      selectedRadio: "",
      idNum: 0,
      items: [],
      isCompleted: false,

    }
  },
  methods: {

    addToList() {
      
      this.isCompleted = false

      this.items.push({ id: this.idNum, todo: this.newTodo, completed: this.isCompleted })

      this.newTodo = "";
      this.idNum += 1

    },

    removeFromList() {

      if (this.selectedRadio !== "" ){

      let index = this.items.findIndex(item => item.id === this.selectedRadio)

      this.items.splice((index), 1)

        this.selectedRadio = ""
      }

    },

    completedItem() {

      //line through completed items
      let index_comp = this.items.findIndex(item => item.id === this.selectedRadio)

      if (this.items[index_comp].completed == true) {
        
        this.items[index_comp].completed = false

      }

      else if (this.items[index_comp].completed == false) {

        this.items[index_comp].completed = true

      }
    }

  }

}).mount('#todo-list-app')

