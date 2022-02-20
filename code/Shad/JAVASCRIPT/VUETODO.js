const App = {
    data() {
        return {
            lis: [
                {
                    item: 'midori',
                    completed: false
                },
            ],
            write: '',
        }
    },
    methods: {
        add() {
            this.lis.push({
                item: this.write,
                completed: false
            })
            this.write = ''
        },
        cancel(index) {
            this.lis.splice(index, 1);
        },
        complete(li) {
            li.completed = !li.completed
        },
    },
    computed: {
        still() {
            return this.lis.filter(li => li.completed === false)
        },
        done() {
            return this.lis.filter(li => li.completed === true)
        }
    }
}

const app = Vue.createApp(App).mount('#app')
