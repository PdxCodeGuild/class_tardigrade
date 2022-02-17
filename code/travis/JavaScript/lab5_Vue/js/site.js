



Vue.createApp({

    data() {
      return {
        
        newTodo: "",
        selectedRadio : "",
        items: [{ id: 1, todo: 'test1' }, { id: 2, todo: 'test2' }]
      }
    },
    methods: {

      addToList() {
          
          this.items.push({todo: this.newTodo})
          this.newTodo = ""
          },

      removeFromList(){
                    //splice.("start index", "number of elements to remove beginning at start index")
        let len = this.items.length
        console.log(this.selectedRadio)
        console.log(this.items.id)

        for (let i =0; i < len; i++){

          if (this.items.id == this.selectedRadio){


          }

        }
      //  this.items.splice((this.selectedRadio), 1)
      //   console.log(this.selectedRadio)
      //   console.log(this.todo)

      },

      completedItem(){
        //line through completed items


      }


    }
    
    
  }).mount('#todo-list-app')

