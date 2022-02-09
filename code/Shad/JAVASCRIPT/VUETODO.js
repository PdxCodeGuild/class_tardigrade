const App = {
    data() {





        return {

            lis: [ 'midori', 'aoi','shiro','kuro'],

            write: '',


        }
    },



    methods: {




        add() {

            this.lis.push(this.write)
            this.write = ''
        },


        cancel(lis) {

            // this.lis.pop(write)
            // this.delete lis[this.write]
            

            this.lis.splice(this.index, 1);

        },

        complete() {
            console.log(lis)
        }

    }



}


Vue.createApp(App).mount('#app')
