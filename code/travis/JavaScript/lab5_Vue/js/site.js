
Vue.createApp({

  data() {
    return {

      newTodo: "",
      selectedRadio: "",
      id_num: 0,
      items: [],
      is_completed: false,

    }
  },
  methods: {

    addToList() {
      
      this.is_completed = false

      this.items.push({ id: this.id_num, todo: this.newTodo, completed: this.is_completed })

      this.newTodo = "";
      this.id_num += 1

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

