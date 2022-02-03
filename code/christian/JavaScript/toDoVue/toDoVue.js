const App = {
    data() {
        return {
            message: 'Hello world!',
            taskList: [],
            newTask: '',
            completeList: []
        }
    },

    methods: {
        addTask() {
            this.taskList.push(this.newTask)

            this.newTask = ''
        },
        logEvent(event) {
            console.log(event, 'event')
            console.log(this.taskList)
        },
        removeTask(task) {
            let finished = this.taskList.indexOf(task)
            this.taskList.splice(finished)
            console.log(finished)
            console.log(task)
            console.log(this.taskList)
        },
        deleteTask(delete) {
            let done = this.completeList.indexOf(delete)
            this.completeList.splice(done)
        },

        completeTask() {
        this.completeList.push(this.newTask)
}
}







Vue.createApp(App).mount('#app')