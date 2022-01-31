



Vue.createApp({

    data() {
      return {
        items: [{ todo: 'test1' }, { todo: 'test2' }]
      }
    },
    methods: {

    addToList() {

        alert("test")
        this.items.push()
        }

    }


    
    
  }).mount('#todo-list')