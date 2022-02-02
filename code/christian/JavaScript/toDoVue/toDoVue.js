const App = {
    data() {
        return {
            message: 'Hello world!',
            taskList: [],
            newTask: ''
        }
    },

    methods: {
        addTask() {
            this.taskList.push(this.newTask)
            
            this.newTask = ''
        },
        
        completeTask: completeTask(event){

        }


    },
}

Vue.createApp(App).mount('#app')