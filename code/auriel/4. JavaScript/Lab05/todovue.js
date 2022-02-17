const App = {
    data () {
        return {
            message: 'My Todo App',
            addTaskInput: '',
            lists: [],
        }
    },

    methods:{
        addTask () {
            this.lists.push({
                id: this.lists.length+1,
                title: this.addTaskInput,
                isComplete: false
            });
            this.addTaskInput = '';
        },

        completeTask (list) {
            list.isComplete = !list.isComplete;
        },

        removeTask (list) {
            const index = this.lists.indexOf(list)
            this.lists.splice(index, 1)
        }
    }
}

Vue.createApp(App).mount('#app')